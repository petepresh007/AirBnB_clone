#!/usr/bin/python3
""" Base Model that other models will inherit from"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Main constructor
            Args:
            *args: not used
            **kwargs: key value pairs
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance
        Adds __class__ key with the class name, and formats created_at and
        updated_at to ISO format.
        """
        object_dictionary = self.__dict__.copy()
        object_dictionary['__class__'] = self.__class__.__name__
        object_dictionary['created_at'] = self.created_at.isoformat()
        object_dictionary['updated_at'] = self.updated_at.isoformat()

        return object_dictionary

    def __str__(self):
        """ Provides a human-readable string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
