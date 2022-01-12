#!/usr/bin/python3
from .core import shell

__all__ = ["force_sudo_password_promt", "get_root_privileges",
           "has_root_privileges"]


def force_sudo_password_promt():
    '''Next shell commands with sudo will prompt a password.'''
    shell("sudo -K").wait()


def get_root_privileges():
    """
    Shows sudo password prompt. Returns True if correct password has been
    entered, otherwise returns False (e.g. Ctrl+C was pressed).
    """
    return not shell("sudo true").exit_code()


def has_root_privileges():
    '''Checks if sudo command can be executed without password prompt.'''
    return not shell("sudo -n true").exit_code()
