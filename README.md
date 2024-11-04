# xub - Configuration and Package management for my Linux Desktop

Tools and documentation to help configure Linux-based workstations.  Xub may
have some shell script-based tools, some Python-based tools, and perhaps other
programming languages ​​will be included in the future.

## Getting Started

This project was created with the command:

```
uv init --package xub
```

You should [install uv][uv] before:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

[uv]: https://docs.astral.sh/uv/getting-started/installation/

## Project Folder Structure

- `bin`: executable scripts that can be run directly from the command line.
- `data`: original copies of raw data.
- `docs`: project documentation.
- `notebooks`: Jupyter notebooks (interactive web application for creating and
  sharing computational documents).
- `rc`: resource configuration to configure the shell environment.
- `src`: package source code.
- `tests`: unit tests and integration tests for the code.
