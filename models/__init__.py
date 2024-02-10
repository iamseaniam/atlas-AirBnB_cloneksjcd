#!/usr/bin/python3
"""
Package containing the engine of the models
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
