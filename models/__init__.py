#!/usr/bin/python3
"""Project AirBnB holberton A. Otmani
    __init__ module
    """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
