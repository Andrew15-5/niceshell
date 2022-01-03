#!/usr/bin/python3
from shell.core import (
    Shell,
    ShortArgsOption,
    normalize_short_and_long_args,
    quotes_wrapper
)
from shell.gnu_coreutils import ls

__all__ = ["GID", "GROUP", "HOME", "Shell", "ShortArgsOption", "UID", "USER",
           "ls", "normalize_short_and_long_args", "quotes_wrapper"]

GID = Shell("id -g").output()[:-1]
GROUP = Shell("id -gn").output()[:-1]
HOME = Shell("printf ~").output()
UID = Shell("id -u").output()[:-1]
USER = Shell("id -un").output()[:-1]

if __name__ == "__main__":
    print(f"{GID=}")
    print(f"{GROUP=}")
    print(f"{HOME=}")
    print(f"{UID=}")
    print(f"{USER=}")
