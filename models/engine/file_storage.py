#!/usr/bin/python3
import json
import os

class FileStorage():
    __file_path = 'file.json'
    __objects = {}
    
    



    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = None

    def save(self):
        if os.path.exists(FileStorage.__file_path):

            try:
                with open(FileStorage.__file_path, 'w') as file:
                    json.dump(FileStorage.__objects, file, indent = 4)
            except FileNotFoundError:
                pass


    def reload(self):
        if os.path.exists(FileStorage.__file_path):

            try:
                with open(FileStorage.__file_path, 'r') as file:
                    FileStorage.__objects = json.load(file)
            except FileNotFoundError:
                pass


