#!/usr/bin/python3
from .core import shell

__all__ = ["can_be_root", "force_sudo_password_promt"]


def can_be_root():
    '''Checks if sudo command can be executed without password prompt.'''
    return not shell("sudo -n true").exit_code()


def force_sudo_password_promt():
    '''Next shell commands with sudo will prompt a password.'''
    shell("sudo -K").wait()
