# models/engine/file_storage.py

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objs = json.load(f)
                for key, obj_dict in serialized_objs.items():
                    class_name = obj_dict['__class__']
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
