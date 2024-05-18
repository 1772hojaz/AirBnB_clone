#!/usr/bin/python3
import uuid
from datetime  import datetime
from models import storage
import models
"""
A base model that defines
all common attributes/methods for other classes
"""

class BaseModel():
    def __init__(self, *args, **kwargs):
        "Creating public instance attributes"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = None
        t = '%Y-%m-%dT%H:%M:%S.%f'

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    if v is not None:
                        self.__dict__[k] = datetime.strptime(v,t)
                    else:
                        self.__dict__[k] = v
        else:
            models.storage.new(self)


    def __str__(self):
        "Class name of the instance"
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        "Gives the time of update"
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        "Output a  serialized dictionary representation of an instance"
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()

        return my_dict
