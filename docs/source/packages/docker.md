# Docker

```{contents} Table of Content
:local:
:depth: 2
:backlinks: none
```

## Installing Docker

- Visit [Docker][docker-install] documentation page to check how to install
  Docker Engine on Linux.
- Also check the ["Docker Tutorial for Beginners"][yt-tutorial] video.

[docker-install]: https://docs.docker.com/engine/install/
[yt-tutorial]: https://www.youtube.com/watch?v=b0HMimUb4f0

- Install main components:

  ```sh
  xub install docker docker-compose
  ```

- Verify it is installed and gather information about the current version:

  ```sh
  sudo docker version
  ```

- After install, run and enable the service on startup:

  ```
  sudo systemctl start docker.service
  sudo systemctl enable docker.service
  ```

- Run Docker without root:

  ```sh
  sudo usermod -aG docker $USER
  ```

- Reboot your system for those changes to take effect.

- Enable auto completion in bash:

  ```bash
  docker completion bash > \
         $HOME/.local/share/bash-completion/completions/docker
  ```

## Some useful Docker commands

- See how many containers are currently running and some configured options:

  ```sh
  docker info
  ```

- Search Docker hub for images:

  ```sh
  docker search $IMAGE_NAME
  ```

  Set `IMAGE_NAME="hello-world"` for an example.

- Download an image from a registry:

  ```sh
  docker pull $IMAGE_NAME
  ```

- Create and run a new container from an image:

  ```sh
  docker run $IMAGE_NAME
  ```

- Execute a command in a running container:

  ```sh
  CONTAINER_NAME=local-web-server
  docker exec -it --tty $CONTAINER_NAME bash
  ```

- Remove all stopped containers:

  ```sh
  docker container prune
  ```

  To remove automatically a container when it stops, use the `--rm` flag when
  running it.

- Monitor Docker with various commands:

  - See which containers are running and check their current status:

    ```sh
    docker container ls
    ```

  - List all installed images:

    ```sh
    docker images
    ```

  - List network configuration:

    ```sh
    docker network ls
    ```

  - CPU, RAM, and network usage of running images:

    ```sh
    docker stats
    ```

  - Logs of a container running in the background:

    ```sh
    docker logs local-web-server
    ```

   - Check  if a container exists and is started:

     ```sh
     docker ps -q -f name=local-web-server
     ```

## Containers vs Images

- **Images** are templates for containers (a recipe for running an
  application), they specify file-system, users, default command, ... they are
  what you download/share.
- **Containers**, on the other hand, are the group of processes that are
  launched and follow the instructions based on an image.  We can have many
  containers for the same image, even running at the same time.

Use the command `docker image ls` to see the pulled images, and `docker ps -a`
to see the launched containers.

## Docker Networks

[Docker Networking][docker-network] refers to the the ability for containers
to connect to and communicate with each other.

### Some References

- [User-defined networks][ud-nets]
- [Container networks][net-cn]
- [Networking using the host network][net-uh]
- [Published ports][net-pp]
- [IP address and host-name][net-ip-hn]
- [DNS services][net-dns]

[docker-network]: https://docs.docker.com/engine/network/
[ud-nets]: https://docs.docker.com/engine/network/#user-defined-networks
[net-cn]: https://docs.docker.com/engine/network/#container-networks
[net-uh]: https://docs.docker.com/engine/network/tutorials/host/
[net-pp]: https://docs.docker.com/engine/network/#published-ports
[net-ip-hn]: https://docs.docker.com/engine/network/#ip-address-and-hostname
[net-dns]: https://docs.docker.com/engine/network/#dns-services

### Using networks

The `--network host` flag can be used on a local workstation to connect to any
container from any other container and from your Linux host.

In production, you need to create several networks, for example:

```sh
for ntw in infrastructure proxy; do
    docker network create $ntw || true
done
```

Normally,
- the `infrastructure` network is used for data-bases, like `PostgreSQL`,
  `MongoDB`, or `Redis`; and
- the `proxy` network is used to automatically expose each published service
  to a single `nginx` container acting as an `Ingress`, and also to manage
  `SSL` certificates with "Let's Encrypt".

### Port Mapping

To interact with a container server we need to publish the port it's listening
on so the host can see it.  Use the `-p` flag to do that.

```sh
docker run -p 80:80 \
       -d --name="local-web-server" \
       --rm nginx:alpine
```

Flag `-d` is used for detach (run in the background).

## Docker Persistence

To add a mount to a container use `--volume` flag, or the more verbose
`--mount` syntax.

Currently in Docker there are three [kinds of mounts][docker-storage]\ :

- **Volumes**: A name is supplied, managed by Docker daemon.
  - Often better in production.
  - Not dependent on host file-system.
  - Easy to share across containers.
  - Can use remote or cloud storage: AWS EFS, NFS, SSHFS.
  - Containers does not need access to host.
  - Not convenient to share with host.
- **Bind-mounts**: Mounts a host file/directory into a container.
  - Often convenient in development.
  - Quickly share with host: gives container access to host, consider
    read-only mount (`-v ./my-data:/pant/in/container:ro`).
- Tempfs mounts.

"Volumes" and "bind-mounts" are used for persistence, whereas "tempfs" are not
persisted.

To create a [volume] explicitly, use the command:

```sh
docker volume create $VOLUME-NAME
```

A volume can be mounted into multiple containers simultaneously.  When no
running container is using a volume, the volume is still available and is not
removed automatically.  To remove unused volumes use the command:

```sh
docker volume prune
```

To mount a volume with the `run` command, use either the `--mount` or
`--volume` flag:

```sh
 docker run --mount type=volume,src=<volume-name>,dst=<mount-path>
 docker run --volume <volume-name>:<mount-path>
```

[docker-storage]: https://docs.docker.com/engine/storage/
[volume]: https://docs.docker.com/engine/storage/volumes/

## Docker Runtime

To use environmental variables use the `-e` flag:

```sh
docker run \
       -e ABC=123 \
       -e DEF=456 \
       --name="py314" \
       python:3.14-rc-alpine \
       python -c "import os; print(os.environ)"
```

## Custom Docker images

Docker can build images by reading the instructions from a [Dockerfile].

For example, you can define an image based on `nginx` for a front-end server:

```dockerfile
FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html
COPY static /usr/share/nginx/html
```

This example assumes the existence of a folder named `static` that contains at
least an `index.html` file.

## Docker Compose

[Compose] is a tool for defining and running multi-container applications.
See the [Compose file reference][compose-file] for more information.

[compose]: https://docs.docker.com/compose/
[compose-file]: https://docs.docker.com/reference/compose-file/
