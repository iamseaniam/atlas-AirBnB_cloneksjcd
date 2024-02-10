#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of a specified class.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Update an instance based on the class name and id.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = objs[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_all(self, arg):
        """Prints all string representation of all instances.
        Usage: all <optional_class_name>
        """
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
            return
        class_name = arg.split()[0]
        if class_name not in ["State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objs.items() if class_name in key])

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
