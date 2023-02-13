#!/usr/bin/python3
"""module for creating users"""

from .base_model import BaseModel


class User(BaseModel):
    """Creates users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
