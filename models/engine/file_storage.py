#!/usr/bin/python3
"""module for storage file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class Attributes
       __file_path: string - path to the JSON file (ex: file.json)
       __objects: dictionary - empty but will store all objects by
       <class name>.id (ex: to store a BaseModel object with id=12121212,
       the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the ictionary __object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objectdict = FileStorage.__objects
        objdict = {obj: objectdict[obj].to_dict() for obj in objectdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing
        """
        try:
            with open(FileStorage.__file_path) as f:
                objectdict = json.load(f)
                for o in objectdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
