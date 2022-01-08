#!/usr/bin/python3
from .core import (
    expose_tilde,
    normalize_short_and_long_args,
    quotes_wrapper,
    shell,
    Shell,
    ShortArgsOption
)
from .gnu_coreutils import cd, cp, ln, ls, mv, rm

__all__ = ["cd", "cp", "expose_tilde", "GID", "GROUP", "HOME", "ln", "ls",
           "mv", "normalize_short_and_long_args", "quotes_wrapper", "rm",
           "shell", "Shell", "ShortArgsOption", "UID", "USER"]

GID = Shell("id -g").output()[:-1]
GROUP = Shell("id -gn").output()[:-1]
HOME = Shell("printf ~").output()
UID = Shell("id -u").output()[:-1]
USER = Shell("id -un").output()[:-1]
