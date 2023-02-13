#!/usr/bin/python3
"""module for creating city"""

from .base_model import BaseModel


class City(BaseModel):
    """Creates cities"""
    state_id = ""
    name = ""
