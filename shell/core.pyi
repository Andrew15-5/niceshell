from subprocess import PIPE, Popen
from typing import AnyStr, IO, Iterable, List, Union

from .core import *


def expose_tilde(quoted_path: str) -> str: ...


class ShortArgsOption:
    TOGETHER = 0
    APART = 1
    NO_DASH = 2


def normalize_short_and_long_args(
    short_args: Union[str, Iterable[str]] = [],
    long_args: Iterable[str] = [],
    short_args_option: ShortArgsOption = ShortArgsOption.TOGETHER) -> str: ...


def quotes_wrapper(path: Union[str, Iterable[str]]) -> str: ...


class Shell:
    command: Union[str, Iterable[str]]
    process: Popen
    pid: int
    stdin: IO[AnyStr]
    stdout: IO[AnyStr]
    stderr: IO[AnyStr]

    def __init__(self,
                 command: Union[str, Iterable[str]],
                 stdin: int = PIPE,
                 stdout: int = PIPE,
                 stderr: int = PIPE) -> None: ...

    def error_output(self) -> str: ...
    def exit_code(self) -> int: ...

    def get_lines(self,
                  exclude_last_lf: bool = True,
                  stderr: bool = False) -> List[str]: ...

    def kill(self): ...
    def output(self) -> str: ...
    def poll(self) -> Union[int, None]: ...
    def send_signal(self, signal: int): ...

    def shell(self,
              command: Union[str, Iterable[str]],
              stdin: int = "parent fd",
              stdout: int = PIPE,
              stderr: int = PIPE) -> Shell: ...

    def terminate(self): ...
    def wait(self) -> int: ...
