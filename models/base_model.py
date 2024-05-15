#!/usr/bin/python3
import uuid
from datetime  import datetime
"""
A base model that defines
all common attributes/methods for other classes
"""

class BaseModel():
    def __init__(self):
        " creating public instance variables"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = None

    def __str__(self):
        "Class name of the instance"
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        "Gives the time of update"
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        "Output a  serialized dictionary representation of an instance"
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()

        return my_dict
