#!/usr/bin/python3
"""Project AirBnB holberton A. Otmani
    """


import json
from models.base_model import BaseModel


class FileStorage():
    """File Storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        obj_json = {}
        with open(FileStorage.__file_path, 'w') as My_file:
            for key, value in self.__dict__.items():
                obj_json.update([key].to_dict(key))
            json.dump(obj_json, My_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as My_file:
                strjsn = json.loads(My_file.read())
                for keyK, keyV in strjsn.items():
                    new_dict = eval("{}(**keyV)".format(keyV["__class__"]))


        except FileNotFoundError:
            pass




