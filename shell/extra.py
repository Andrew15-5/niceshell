#!/usr/bin/python3
from .core import shell

__all__ = ["can_be_root"]


def can_be_root():
    '''Checks if sudo command can be executed without password prompt.'''
    return not shell("sudo -n true").exit_code()
