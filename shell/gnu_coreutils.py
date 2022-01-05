#!/usr/bin/python3
from typing import Iterable, Union

from .core import *

__all__ = ["ln", "ls"]


def ln(source_path: Union[str, Iterable[str]],
       destination_path: str,
       batch=False,
       sudo=False,
       short_args: Union[str, Iterable[str]] = [],
       long_args: Iterable[str] = [],
       test=False) -> Union[Shell, str]:
    """
    Wrapper for ln command from GNU Core Utilities.
    Note: destination_path is always wrapped in quotes. If source_path and/or
    destination_path are/is wrapped in quotes (batch=False), '~' will still
    work (will be expanded).

    Parameters:
        source_path (str | Iterable[str]): file(s) and/or directory(-ies) of
            which (sym)link(s) is/are need to be created.
        destination_path (str): destination directory for source files/dirs.
        batch (bool): wraps source_path in double quotes if False. Default is
            False.
        sudo (bool): adds sudo at the begining of ln command. Default is False.
        short_args (str | Iterable[str]): string or array of short arguments.
            Prefix-dash is ignored. Default is [] (no short arguments).
        long_args (Iterable[str]): array of long arguments. Prefix-dashes are
            ignored. Default is [] (no long arguments).
        test (bool): return command itself without its execution (for test
            purposes). Default is False.

    Raises:
        TypeError: source_path's type isn't (str | Iterable[str]) or type of
            elements of source_path (Iterable[str]) are not str or
            destination_path's type isn't str.
        IndexError: source_path (Iterable[str]) is empty.

    Returns:
        (Shell | str): Shell object of executing command or the command itself.
    """
    if (not isinstance(source_path, (str, Iterable)) or
            not all(isinstance(e, str) for e in source_path)):
        raise TypeError("source_path must be str or Iterable[str].")
    elif not isinstance(source_path, str) and len(source_path) == 0:
        raise IndexError("source_path (Iterable[str]) is empty.")
    if not isinstance(destination_path, str):
        raise TypeError("destination_path must be str.")
    if batch:
        # Concatenate anything but str (batch)
        if not isinstance(source_path, str):
            source_path = ' '.join(source_path)
    else:
        source_path = expose_tilde(quotes_wrapper(source_path))
    destination_path = expose_tilde(quotes_wrapper(destination_path))
    sudo = "sudo" if sudo else ''
    args = normalize_short_and_long_args(
        short_args, long_args, ShortArgsOption.APART)
    command = f'{sudo} ln {args} -- {source_path} {destination_path}'.strip()
    if test:
        return command
    else:
        return Shell(command)


def ls(path: Union[str, Iterable[str]] = '',
       batch=False,
       sudo=False,
       short_args: Union[str, Iterable[str]] = [],
       long_args: Iterable[str] = [],
       test=False) -> Union[Shell, str]:
    """
    Wrapper for ls command from GNU Core Utilities.
    Note: If path is wrapped in quotes (batch=False), '~' will still work (will
    be expanded).

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
    if batch:
        if not isinstance(path, str):  # Concatenate anything but str (batch)
            path = ' '.join(path)
    elif path != '':  # Don't wrap emptiness in double quotes
        path = expose_tilde(quotes_wrapper(path))
    sudo = "sudo" if sudo else ''
    args = normalize_short_and_long_args(
        short_args, long_args, ShortArgsOption.APART)
    command = f'{sudo} ls {args} -- {path}'.strip()
    if test:
        return command
    else:
        return Shell(command)
