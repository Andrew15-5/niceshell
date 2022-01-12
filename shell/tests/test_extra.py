#!/usr/bin/python3
import sys

import pytest

sys.path.extend([f"{sys.path[0]}/..", f"{sys.path[0]}/../.."])
from shell import extra


class TestExtra:
    def test_can_be_root(self):
        assert type(extra.can_be_root()) == bool

    def test_force_sudo_password_promt(self):
        assert extra.force_sudo_password_promt() == None


if __name__ == "__main_ ":
    pytest.main()
