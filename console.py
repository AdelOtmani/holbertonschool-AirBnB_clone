#!/usr/bin/python3
"""Project AirBnB holberton A. Otmani
    """
import cmd
import json
import sys
from models import *
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Console initialisation Hbnb
    """
    prompt = '(hbnb)'
    name_class = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """End Of File
        """
        print()
        return True

    def emptyline(self):
        """"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        quit()

    def do_create(self, arg):
        """"""
        if len(arg) <= 0:
            print("** class name missing **")
        else:
            try:
                line_arg = arg.split()
                new_Create = eval(line_arg[0])()
                new_Create.save()
                print(new_Create.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id"""

        args = line.split()
        if len(args) == 0:
                print("** class name missing **")
        elif args[0] not in HBNBCommand.name_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(
                args[0], args[1]) not in models.storage.all().keys():
            print("** no instance found **")
        else:
            print(models.storage.all()["{}.{}".format(
                args[0], args[1])])


    def do_destroy(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if line is None:
            print("** class name missing **")
        args = line.split()
        try:
            model_class = getattr(sys.modules[__name__], args[0])
        except Exception:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objs = storage.all()
        obj = objs.get('.'.join(args), None)
        if obj is None:
            print("** no instance found **")
        else:
            del objs['.'.join(args)]
            storage.save()

    def do_all(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if line is None:
            print("** class name missing **")
        args = line.split()
        try:
            model_class = getattr(sys.modules[__name__], args[0])
        except Exception:
            print("** class doesn't exist **")
            return False

        objs = storage.all()
        print(
            [str(obj) for obj in objs.values() if type(obj) is model_class]
        )

    def do_update(self, line):
        """

        Args:
            line (_type_): _description_
        """


        args = line.split()
        objs = storage.all()
        try:
            argsLen = len(args)
            obj = objs.get('.'.join([args[0], args[1]]), None)
            if (obj is None or argsLen <= 3):
                raise
        except Exception:
            if argsLen <= 0:
                print("** class name missing **")
            elif args[0] not in str(list(objs.keys())):
                print("** class doesn't exist **")
            elif argsLen == 1:
                print("** instance id missing **")
            elif obj is None:
                print("** no instance found **")
            elif argsLen == 2:
                print("** attribute name missing **")
            elif argsLen == 3:
                print("** value missing **")
            return

        setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]) if args[2] in obj.to_dict() else args[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
