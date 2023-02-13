#!/usr/bin/python3
"""module for creating reviews"""

from .base_model import BaseModel


class Review(BaseModel):
    """Creates reviews"""
    place_id = ""
    user_id = ""
    text = ""
