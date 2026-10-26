(git-configuration)=
# Git Configuration

This page documents workstation Git settings.

- [Install Git](git-package).
- [](#configure-global-options)
- Generate an SSH key.
- Register the SSH key with GitHub.
- Test SSH authentication.

## Configure Global Options

Global Git options are stored in `~/.gitconfig`.  You can copy this
configuration file from a previous computer, or from a backup of a previous
installation.

The file will look like:

```
[user]
	name = <full-name>
	email = <email>
	useConfigOnly = true
[core]
	editor = emacsclient -n
	excludesfile = ~/.gitignore
	autocrlf = input
[alias]
	st = status
	co = checkout
	br = branch
	logline = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
[gui]
	spellingDictionary = en_US
[rerere]
	enabled = 1
[credential]
	helper = store
[init]
	defaultBranch = main
```

If you want to use `meld` add the following section:

```
[merge]
	tool = meld
```
