# -*- coding: utf-8 -*-

# Native Python Modules.

# External Modules.

# Django Modules.

# Project Modules.


class BaseRESTError(BaseException):
    """
    Base error for REST application.
    """
    pass


class AuthenticationFailed(BaseRESTError):
    """
    Exception raised when Authentication fails.
    """
    def __init__(self):
        self.message = "Authentication Failed."


class Exception422(BaseRESTError):
    code = 422

    def __init__(self, message):
        self.message = message
