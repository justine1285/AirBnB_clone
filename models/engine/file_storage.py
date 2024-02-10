#!/usr/bin/python3
"""importing standard modules and modules from our packages"""
import json
from datetime import datetime as dt
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """Serializes instances and deserializes JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """
            returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj: dict) -> None:
        """
            sets in __objects the obj with key <obj class name>.id
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self) -> None:
        """
            serializes (save) all __objects to the JSON file
        """
        dict_serial = {}
        with open(self.__file_path, mode="w", encoding="utf-8") as file_obj:
            for key, val in self.__objects.items():
                dict_serial[key] = val.to_dict()
            json.dump(dict_serial, file_obj)

    def reload(self) -> None:
        """
        deserializes a json string into a dictionary of objects,
        `__objects` only if `__file_path` exists.
        """
        try:
            path = self.__file_path
            with open(path, mode="r", encoding="utf-8") as file_obj:
                data_strm = json.load(file_obj)
            for key, val in data_strm.items():
                class_name = key.split(".")[0]
                self.new(eval(class_name + "(**val)"))
        except FileNotFoundError:
            pass
