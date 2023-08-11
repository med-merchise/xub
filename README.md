# xub - configuration tools for my desktop system

Xub is a tool to help you configure a Linux-based workstations.  It creates
interfaces to the selected package management system so that it is transparent
to switch from one to the other.

Xub has some tools based on shell scripts and other based on Python.

After making sure that Python is installed, the first step is to ensure [pip]
as well:

[pip]: https://pip.pypa.io/en/stable/installation/

```sh
python -m ensurepip --user --upgrade
```

## Run Commands

The `rc` folder contains files that serve as startup information for operating
system commands or that when installed need to be configured at the shell
level.
