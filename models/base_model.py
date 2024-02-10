#!/usr/bin/python3
"""
Module containing the BaseModel class
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel class for common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)  # Add this line to link the instance to FileStorage

    def __str__(self):
        """
        Returns string representation of BaseModel instance
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()  # Add this line to save to file

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
