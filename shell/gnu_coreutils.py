#!/usr/bin/python3
from typing import Iterable, Union

from core import *

__all__ = ["ls"]


def ls(path: Union[str, Iterable[str]] = '',
       batch=False,
       sudo=False,
       short_args: Union[str, Iterable[str]] = [],
       long_args: Iterable[str] = [],
       test=False) -> Union[Shell, str]:
    """
    Wrapper for ls command from GNU Core Utilities.

    Parameters:
        path (str | Iterable[str]): directory(-ies) of which content is need to
            be gathered. Default is '' (aka present/current working directory).
        batch (bool): wraps path in double quotes if False. Default is False.
        sudo (bool): adds sudo at the begining of ls command. Default is False.
        short_args (str | Iterable[str]): string or array of short arguments.
            Prefix-dash is ignored. Default is [] (no short arguments).
        long_args (Iterable[str]): array of long arguments. Prefix-dashes are
            ignored. Default is [] (no long arguments).
        test (bool): return command itself without its execution (for test
            purposes). Default is False.

    Raises:
        TypeError: path's type isn't (str | Iterable[str]) or type of elements
            of path (Iterable[str]) are not str.

    Returns:
        (Shell | str): Shell object of executing command or the command itself.
    """
    if (not isinstance(path, (str, Iterable)) or
            not all(isinstance(e, str) for e in path)):
        raise TypeError("path must be str or Iterable[str].")
    if list(path) in ([], ['']):  # Edge cases
        path = ''
    if not batch and path != '':  # Don't wrap emptiness in double quotes
        path = quotes_wrapper(path)
    elif not isinstance(path, str):  # Concatenate anything but str (batch)
        path = ' '.join(path)
    sudo = "sudo" if sudo else ''
    args = normalize_short_and_long_args(
        short_args, long_args, ShortArgsOption.APART)
    command = f'{sudo} ls {args} -- {path}'.strip()
    if test:
        return command
    else:
        return Shell(command)
