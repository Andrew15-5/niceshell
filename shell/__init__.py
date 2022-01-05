#!/usr/bin/python3
from .core import (
    Shell,
    ShortArgsOption,
    expose_tilde,
    normalize_short_and_long_args,
    quotes_wrapper
)
from .gnu_coreutils import ln, ls

__all__ = ["GID", "GROUP", "HOME", "Shell", "ShortArgsOption", "UID", "USER",
           "expose_tilde", "ln", "ls", "normalize_short_and_long_args",
           "quotes_wrapper"]

GID = Shell("id -g").output()[:-1]
GROUP = Shell("id -gn").output()[:-1]
HOME = Shell("printf ~").output()
UID = Shell("id -u").output()[:-1]
USER = Shell("id -un").output()[:-1]
