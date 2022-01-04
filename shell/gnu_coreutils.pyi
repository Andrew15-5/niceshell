from typing import Iterable, Union

from core import Shell


def ls(path: Union[str, Iterable[str]] = '',
       batch: bool = False,
       sudo: bool = False,
       short_args: Union[str, Iterable[str]] = [],
       long_args: Iterable[str] = [],
       test: bool = False) -> Union[Shell, str]: ...
