# uv

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and
project manager, written in Rust.

## Installing `uv`

Use `curl` to download the script and execute it with `sh`:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

To update `uv` to the latest version:

```sh
uv self update
```

To generate `uv` shell-completion:

```
BASH_COMPLETION_DIR="$HOME/.local/share/bash-completion/completions"
mkdir -p $BASH_COMPLETION_DIR
uv generate-shell-completion bash > $BASH_COMPLETION_DIR/uv
```

## Useful commands

- Pin a Python version at your home:

  ```sh
  cd ~
  uv python pin <version>
  ```

- Export a `requirements.txt` file that includes only the dependencies for one
  group:

  ```sh
  uv export --format requirements-txt --no-hashes --only-group <group-name>
  ```

## Some references

- [Mastering Python Project Management with `uv`][uv-mastering]

[uv-mastering]: https://bury-thomas.medium.com/mastering-python-project-management-with-uv-part1-its-time-to-ditch-poetry-c2590091d90a
