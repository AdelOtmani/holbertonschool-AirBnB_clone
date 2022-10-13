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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        obj_json = {}
        for keyK in self.__objects:
            obj_json[keyK] = self.__objects[keyK].to_dict()
        with open(FileStorage.__file_path, 'w') as My_file:
            json.dump(obj_json, My_file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as My_file:
                    strjsn = json.loads(My_file.read())
                    for keyK, keyV in strjsn.items():
                        new_dict = eval((keyV.get("__class__") + "(**keyV)"))
                        FileStorage.__objects[keyK] = new_dict
        except FileNotFoundError:
            pass



