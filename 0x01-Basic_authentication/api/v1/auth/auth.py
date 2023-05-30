#!/usr/bin/env python3
""" manage the API authentication
SE: Mardochee GNERAN
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth method
         - Return False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None
