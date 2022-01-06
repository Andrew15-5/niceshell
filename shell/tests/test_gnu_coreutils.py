#!/usr/bin/python3
import sys
from typing import Iterable, Union

import pytest

sys.path.extend([f"{sys.path[0]}/..", f"{sys.path[0]}/../.."])
from shell import gnu_coreutils


class TestGNUcoreutils:
    def test_ln(self):
        ln = gnu_coreutils.ln
        # Errors
        # source_path's type must be str or Iterable[str].
        with pytest.raises(TypeError):
            ln(1)
        with pytest.raises(TypeError):
            ln([])
        with pytest.raises(TypeError):
            ln([1])

        # destination_path's type must be str.
        with pytest.raises(TypeError):
            ln('', 1)

        # Asserts batch=False
        def ln(source_path: Union[str, Iterable[str]],
               destination_path: str,
               sudo=False,
               short_args: Union[str, Iterable[str]] = [],
               long_args: Iterable[str] = []) -> str:
            return gnu_coreutils.ln(source_path, destination_path, False,
                                    sudo, short_args, long_args, True)
        # Test simple (edge) cases
        assert ln('', '') == 'ln  -- "" ""'
        assert ln([''], '') == 'ln  -- "" ""'
        assert ln(('', ''), '') == 'ln  -- "" "" ""'
        assert ln("/file", "/tmp") == 'ln  -- "/file" "/tmp"'
        # Test short/long arguments
        assert ln('', '', short_args="-s") == 'ln -s -- "" ""'
        assert ln('', '', long_args=["--force"]) == 'ln --force -- "" ""'
        assert ln('', '', short_args="rs", long_args=["force"]
                  ) == 'ln -r -s --force -- "" ""'
        assert ln('', '', short_args=["r", "S bak"], long_args=["all"]
                  ) == 'ln -r -S bak --all -- "" ""'
        # Test everything
        assert ln(
            "/folder with spaces/dir", "/different folder with spaces",
            short_args='s'
        ) == 'ln -s -- "/folder with spaces/dir" "/different folder with spaces"'
        assert ln(["../../tmp/file1", "file2", "f i l e 3"], "~/"
                  ) == 'ln  -- "../../tmp/file1" "file2" "f i l e 3" ~/""'
        assert ln(
            ["tmp/dir1", "dir2", "~/d i r 3/src/"], "~/", sudo=True,
            short_args=['r', 's', 'f', "S .bak"], long_args=["verbose"]
        ) == 'sudo ln -r -s -f -S .bak --verbose -- "tmp/dir1" "dir2" ~/"d i r 3/src/" ~/""'

        # Asserts batch=True
        def ln(source_path: Union[str, Iterable[str]],
               destination_path: str,
               sudo=False,
               short_args: Union[str, Iterable[str]] = [],
               long_args: Iterable[str] = []) -> str:
            return gnu_coreutils.ln(source_path, destination_path, True,
                                    sudo, short_args, long_args, True)
        # Test simple/edge cases
        assert ln('', '') == 'ln  --  ""'
        assert ln([''], '') == 'ln  --  ""'
        assert ln(('', ''), '') == 'ln  --   ""'
        assert ln("/file", "/tmp") == 'ln  -- /file "/tmp"'
        # Test short/long arguments
        assert ln('', '', short_args="-s") == 'ln -s --  ""'
        assert ln('', '', long_args=["--force"]) == 'ln --force --  ""'
        assert ln('', '', short_args="rs", long_args=["force"]
                  ) == 'ln -r -s --force --  ""'
        assert ln('', '', short_args=["r", "S bak"], long_args=["all"]
                  ) == 'ln -r -S bak --all --  ""'
        # Test everything
        assert ln(
            ["tmp/dir1", "dir2", "~/dir3/src/*"], "~", sudo=True,
            short_args=['r', 's', 'f', "S .bak"], long_args=["verbose"]
        ) == 'sudo ln -r -s -f -S .bak --verbose -- tmp/dir1 dir2 ~/dir3/src/* ~'

        # Special cases (hacks)
        # Case #1
        assert ln("file1 file2", "~/dest"
                  ) == 'ln  -- file1 file2 ~/"dest"'
        assert ln(["file1 file2"], "~/dest"
                  ) == 'ln  -- file1 file2 ~/"dest"'

        # Case #2
        assert ln(['"/dir 1" dir2/*'], '~', short_args='s'
                  ) == 'ln -s -- "/dir 1" dir2/* ~'

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
        # Test simple/edge cases
        assert ls() == "ls  --"
        assert ls(()) == "ls  --"
        assert ls(set('')) == "ls  --"
        assert ls(['', '']) == 'ls  -- "" ""'
        assert ls("/tmp") == 'ls  -- "/tmp"'
        assert ls("/folder with spaces/dir"
                  ) == 'ls  -- "/folder with spaces/dir"'
        assert ls(["dir1", "dir2", "d i r 3"]
                  ) == 'ls  -- "dir1" "dir2" "d i r 3"'
        # Test short/long arguments
        assert ls(short_args="a"
                  ) == 'ls -a --'
        assert ls(long_args=["--all"]
                  ) == 'ls --all --'
        assert ls(short_args="ld", long_args=["all"]
                  ) == 'ls -l -d --all --'
        assert ls(short_args=["-l", "-d"], long_args=["all"]
                  ) == 'ls -l -d --all --'
        # Test everything
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
        # Test simple/edge cases
        assert ls() == "ls  --"
        assert ls(()) == "ls  --"
        assert ls(set('')) == "ls  --"
        assert ls("/tmp") == "ls  -- /tmp"
        assert ls("/folder with spaces/dir"
                  ) == "ls  -- /folder with spaces/dir"
        assert ls(["dir1", "dir2", "dir3"]
                  ) == "ls  -- dir1 dir2 dir3"
        # Test short/long arguments
        assert ls(short_args="-a") == "ls -a --"
        assert ls(long_args=["--all"]) == "ls --all --"
        assert ls(short_args="ld", long_args=["all"]
                  ) == "ls -l -d --all --"
        assert ls(short_args=["l", "d"], long_args=["all"]
                  ) == "ls -l -d --all --"
        # Test everything
        assert ls(["here/*", "there/*"], sudo=True,
                  short_args=['l', 'd', "I PATTERN"], long_args=["all"]
                  ) == "sudo ls -l -d -I PATTERN --all -- here/* there/*"

        # Special cases (hacks)
        # Case #1
        assert ls("dir1 dir2 dir3"
                  ) == "ls  -- dir1 dir2 dir3"
        assert ls(["dir1 dir2 dir3"]
                  ) == "ls  -- dir1 dir2 dir3"

        # Case #2
        assert ls(['"dir 1" "dir 2" dir3/*']
                  ) == 'ls  -- "dir 1" "dir 2" dir3/*'


if __name__ == "__main__":
    pytest.main()
