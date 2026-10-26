(ssh-how-to)=
# Work with SSH

This guide covers the everyday SSH tasks on the workstation:

- [](#generate-an-ssh-key)
- [](#configure-and-activate-an-ssh-server)
- [](#connect-to-an-ssh-server)
- [](#map-a-remote-directory-to-a-local-file-system)
- [](#configure-github-with-ssh)

In the examples, `<user>` is the account on the remote host, `<host>` is its
name or IP address, and `<email>` is your e-mail address.

## Prerequisites

Install the OpenSSH client and server, and the tools used later in this
guide:

```bash
sudo pacman -S --needed openssh sshfs gvfs
```

- `openssh` provides `ssh`, `ssh-keygen`, `ssh-agent`, and `sshd`.
- `sshfs` mounts remote directories through FUSE.
- `gvfs` provides the `sftp://` backend used by the file manager.

## Generate an SSH Key

1. Create an Ed25519 key pair.  Use a passphrase; the agent will remember it
   for the session.

   ```bash
   ssh-keygen -t ed25519 -C "<email>"
   ```

   Accept the default location (`~/.ssh/id_ed25519`).  This creates the
   private key `~/.ssh/id_ed25519` and the public key
   `~/.ssh/id_ed25519.pub`.

2. Check the permissions of the `~/.ssh` directory and the private key:

   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/id_ed25519
   chmod 644 ~/.ssh/id_ed25519.pub
   ```

3. Enable the SSH agent as a user service:

   ```bash
   systemctl --user enable --now ssh-agent.socket
   ```

   Then export its socket from your shell profile (for example,
   `~/.bashrc`):

   ```bash
   export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
   ```

4. Let the agent load keys on first use by adding this to `~/.ssh/config`:

   ```
   Host *
       AddKeysToAgent yes
   ```

   Alternatively, load the key manually with `ssh-add ~/.ssh/id_ed25519`.

5. Verify that the agent holds the key:

   ```bash
   ssh-add -l
   ```

## Configure and Activate an SSH Server

Apply these steps on the machine that will accept connections.

1. Enable and start the SSH daemon:

   ```bash
   sudo systemctl enable --now sshd.service
   ```

2. Allow incoming SSH traffic in the firewall.  Omarchy enables `ufw` by
   default:

   ```bash
   sudo ufw allow 22/tcp
   sudo ufw status
   ```

3. From each **client**, authorize its public key on the server.  This step
   still uses password authentication, so do it before hardening:

   ```bash
   ssh-copy-id -i ~/.ssh/id_ed25519.pub <user>@<host>
   ```

   The key is appended to `~/.ssh/authorized_keys` of `<user>` on the
   server.

4. Harden the server.  The default `/etc/ssh/sshd_config` includes every file
   in `/etc/ssh/sshd_config.d/`, so keep local settings in a drop-in file,
   `/etc/ssh/sshd_config.d/10-local.conf`:

   ```
   PermitRootLogin no
   PasswordAuthentication no
   KbdInteractiveAuthentication no
   PubkeyAuthentication yes
   ```

   Optionally, restrict access to specific accounts with
   `AllowUsers <user>`.

5. Validate the configuration and reload the daemon:

   ```bash
   sudo sshd -t
   sudo systemctl reload sshd.service
   ```

   Keep your current session open and test a new connection from a client
   before closing it, so a configuration mistake does not lock you out.

6. Check the service status and the listening socket:

   ```bash
   systemctl status sshd.service
   ss -tlnp | grep ':22'
   ```

## Connect to an SSH Server

### Define a Host Alias

An alias in `~/.ssh/config` shortens every command below.  The terminal,
Emacs TRAMP, `sshfs`, and the file manager all read this file:

```
Host <alias>
    HostName <host>
    User <user>
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 30
```

On the first connection, `ssh` shows the server's host key fingerprint.
Compare it with the output of the following command on the server before
answering `yes`:

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

### From a Terminal

```bash
ssh <user>@<host>
ssh <alias>
```

Useful variations:

```bash
ssh <alias> 'uname -a'                  # Run a single command.
scp file.txt <alias>:~/                 # Copy a file to the remote home.
ssh -L 8080:localhost:80 <alias>        # Forward local port 8080.
```

### From Emacs Using TRAMP

TRAMP is built into Emacs; no extra package is needed.

- Open a remote file or directory with `C-x C-f` and a remote path:

  ```
  /ssh:<user>@<host>:/path/to/file
  /ssh:<alias>:~/
  ```

  Opening a directory starts Dired on the remote host.

- Edit a file as `root` on the remote host by chaining a `sudo` hop:

  ```
  /ssh:<alias>|sudo:<alias>:/etc/hosts
  ```

- Commands such as `M-x shell`, `M-x compile`, and `M-x eshell` run on the
  remote host when the current buffer is remote.

- To speed up TRAMP and reuse connections, add to your Emacs configuration:

  ```elisp
  (setq tramp-default-method "ssh"
        tramp-use-connection-share t)
  ```

- If a connection hangs, run `M-x tramp-cleanup-all-connections`.

### From the Omarchy File Manager

Omarchy uses Nautilus (GNOME Files) as its default file manager.  It accesses
SSH servers through the `sftp://` backend provided by `gvfs`.

1. Open the file manager and press `Ctrl+L` to edit the location bar.
2. Type the server address and press `Enter`:

   ```
   sftp://<user>@<host>/path/to/directory
   sftp://<alias>/
   ```

   Alternatively, select **Other Locations** in the sidebar and enter the
   same address in **Connect to Server**.
3. Press `Ctrl+D` to bookmark the location in the sidebar.

The connection is also available to other applications under
`/run/user/$UID/gvfs/`.  From a terminal, use `gio`:

```bash
gio mount sftp://<alias>/
gio mount -l
gio mount -u sftp://<alias>/
```

## Map a Remote Directory to a Local File System

Use `sshfs` to mount a remote directory so that any local program can use
it.

### Mount on Demand

```bash
mkdir -p ~/mnt/<alias>
sshfs <alias>:/path/to/directory ~/mnt/<alias> \
      -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3
```

Unmount it with:

```bash
fusermount3 -u ~/mnt/<alias>
```

### Mount Automatically

To mount the directory on first access, add a line to `/etc/fstab`.  The
mount runs as `root`, so use the full `<user>@<host>` form and an explicit
identity file instead of the alias:

```
<user>@<host>:/path/to/directory  /home/<local-user>/mnt/<alias>  fuse.sshfs  noauto,x-systemd.automount,_netdev,reconnect,IdentityFile=/home/<local-user>/.ssh/id_ed25519,uid=1000,gid=1000,allow_other,default_permissions  0  0
```

Replace `uid` and `gid` with the output of `id -u` and `id -g`.  Then:

1. Add the server's host key to `root`'s known hosts by connecting once:

   ```bash
   sudo ssh -i /home/<local-user>/.ssh/id_ed25519 <user>@<host> exit
   ```

   The key must not have a passphrase for an unattended mount; otherwise,
   use the on-demand mount.

2. Reload `systemd` and trigger the mount:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart remote-fs.target
   ls ~/mnt/<alias>
   ```

## Configure GitHub with SSH

1. Copy the public key to the clipboard:

   ```bash
   wl-copy < ~/.ssh/id_ed25519.pub
   ```

2. Register the key with GitHub, using either method:

   - In the web interface, open **Settings** → **SSH and GPG keys** →
     **New SSH key**, paste the key, and give it a title that identifies
     the workstation.
   - With the GitHub CLI:

     ```bash
     gh auth refresh -h github.com -s admin:public_key
     gh ssh-key add ~/.ssh/id_ed25519.pub --title "$(hostname)"
     ```

3. Test the authentication:

   ```bash
   ssh -T git@github.com
   ```

   On the first connection, check that the fingerprint matches GitHub's
   published Ed25519 fingerprint
   (`SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU`).  A successful
   test prints:

   ```
   Hi <github-user>! You've successfully authenticated, but GitHub does not provide shell access.
   ```

4. Use SSH URLs for repositories:

   ```bash
   git clone git@github.com:<github-user>/<repository>.git
   ```

   Switch an existing clone from HTTPS to SSH with:

   ```bash
   git remote set-url origin git@github.com:<github-user>/<repository>.git
   git remote -v
   ```

5. If port 22 is blocked by the network, connect through port 443 by adding
   to `~/.ssh/config`:

   ```
   Host github.com
       HostName ssh.github.com
       Port 443
       User git
   ```

See also {ref}`git-configuration`.

## Official Documentation

- [OpenSSH manual pages](https://www.openssh.com/manual.html)
- [ArchWiki: OpenSSH](https://wiki.archlinux.org/title/OpenSSH)
- [ArchWiki: SSHFS](https://wiki.archlinux.org/title/SSHFS)
- [TRAMP manual](https://www.gnu.org/software/tramp/)
- [GitHub: Connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
