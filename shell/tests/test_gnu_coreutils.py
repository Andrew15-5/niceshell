#!/usr/bin/python3
import sys
from typing import Iterable, Union

import pytest

sys.path.extend([f"{sys.path[0]}/..", f"{sys.path[0]}/../.."])
from shell import gnu_coreutils


class TestGNUcoreutils:
    def test_ls(self):
        ls = gnu_coreutils.ls
        # Errors
        # path must be str or Iterable[str].
        with pytest.raises(TypeError):
            ls(1, test=True)
        with pytest.raises(TypeError):
            ls([1], test=True)

        # Asserts batch=False
        def ls(path: Union[str, Iterable[str]] = '',
               sudo=False,
               short_args: Union[str, Iterable[str]] = [],
               long_args: Iterable[str] = []) -> str:
            return gnu_coreutils.ls(
                path, False, sudo, short_args, long_args, True)
        assert ls() == "ls  --"
        assert ls(()) == "ls  --"
        assert ls(set('')) == "ls  --"
        assert ls("/tmp") == 'ls  -- "/tmp"'
        assert ls("/folder with spaces/dir"
                  ) == 'ls  -- "/folder with spaces/dir"'
        assert ls(["dir1", "dir2", "d i r 3"]
                  ) == 'ls  -- "dir1" "dir2" "d i r 3"'
        assert ls(short_args="a"
                  ) == 'ls -a --'
        assert ls(long_args=["--all"]
                  ) == 'ls --all --'
        assert ls(short_args="ld", long_args=["all"]
                  ) == 'ls -l -d --all --'
        assert ls(short_args=["-l", "-d"], long_args=["all"]
                  ) == 'ls -l -d --all --'
        assert ls(
            ["~/here/*", "~/there/*"], sudo=True,
            short_args=['l', 'd', "-I PATTERN"], long_args=["all"]
        ) == 'sudo ls -l -d -I PATTERN --all -- ~/"here/*" ~/"there/*"'

        # Asserts batch=True
        def ls(path: Union[str, Iterable[str]] = '',
               sudo=False,
               short_args: Union[str, Iterable[str]] = [],
               long_args: Iterable[str] = []) -> str:
            return gnu_coreutils.ls(
                path, True, sudo, short_args, long_args, True)
        assert ls() == "ls  --"
        assert ls(()) == "ls  --"
        assert ls(set('')) == "ls  --"
        assert ls("/tmp") == "ls  -- /tmp"
        assert ls("/folder with spaces/dir"
                  ) == "ls  -- /folder with spaces/dir"
        assert ls(["dir1", "dir2", "d i r 3"]
                  ) == "ls  -- dir1 dir2 d i r 3"
        assert ls(short_args="-a") == "ls -a --"
        assert ls(long_args=["--all"]) == "ls --all --"
        assert ls(short_args="ld", long_args=["all"]
                  ) == "ls -l -d --all --"
        assert ls(short_args=["l", "d"], long_args=["all"]
                  ) == "ls -l -d --all --"
        assert ls(["here/*", "there/*"], sudo=True,
                  short_args=['l', 'd', "I PATTERN"], long_args=["all"]
                  ) == "sudo ls -l -d -I PATTERN --all -- here/* there/*"


if __name__ == "__main__":
    pytest.main()
