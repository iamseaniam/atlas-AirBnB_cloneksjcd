#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** instance id missing **")
            return
        if len(args) == 1:
            print("** class name missing **")
            return
        obj_dict = storage.all()
        class_name = args[0]
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name == "BaseModel":
            obj = BaseModel()
        elif class_name == "State":
            obj = State()
        elif class_name == "City":
            obj = City()
        elif class_name == "Amenity":
            obj = Amenity()
        elif class_name == "Place":
            obj = Place()
        elif class_name == "Review":
            obj = Review()
        else:
            print("** class doesn't exist **")
            return
        obj.save()
        print(obj.id)

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        class_name = args[0]
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj_dict = storage.all()
        class_name = args[0]
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in obj_dict:
            print("** no instance found **")
            return
        obj = obj_dict[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_all(self, arg):
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            for obj in obj_dict.values():
                print(obj)
            return
        class_name = args[0]
        for key, obj in obj_dict.items():
            if class_name == key.split('.')[0]:
                print(obj)

    def do_EOF(self, arg):
        print("")
        return True

    def do_quit(self, arg):
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
