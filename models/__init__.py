#!/usr/bin/python3
"""Modularize module directory"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
