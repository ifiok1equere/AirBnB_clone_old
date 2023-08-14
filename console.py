#!/usr/bin/python3
''' This module defines the console of this project '''
import cmd
import sys
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    '''
    This class defines the console of our program
    to create, update and destroy objects.
    '''

    prompt = "(hbnb) "
    __model_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print('''Quit command to exit the program\n''')

    def help_EOF(self):
        print('''This command exits a program\n''')

    def do_create(self, line):
        """Creates a new instance of the specified class"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        if len(tokens) == 1 and tokens[0] not in HBNBCommand.__model_list:
            print("** class doesn't exist **")
            return
        if len(tokens) > 1:
            print("** class doesn't exist **")
            return
        obj = eval(tokens[0])()
        storage.new(obj)
        obj.save()
        print("{}".format(obj.id))

    def do_show(self, line):
        """Prints the string representations of an
            instance based on the class name and id"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.__model_list:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        show_obj = tokens[0] + "." + tokens[1]
        storage.reload()
        all_inst = storage.all()
        if show_obj not in all_inst:
            print("** no instance found **")
        else:
            print(str(all_inst[show_obj]))
            return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.__model_list:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        usr_id = tokens[1]
        del_obj = tokens[0] + "." + usr_id
        storage.reload()
        if del_obj not in storage.all():
            print("** no instance found **")
        elif del_obj in storage.all():
            del storage.all()[del_obj]
            storage.save()
            return

    def do_all(self, line):
        """Prints all string representation of all instances
        AOA    based or not on the class name in a list"""
        tokens = line.split()
        storage.reload()
        all_objs = storage.all()
        obj_list = []
        new_obj_dict = {}
        if not tokens and all_objs:
            for key, value in all_objs.items():
                obj_list.append(str(value))
            print(obj_list)
        elif tokens:
            all_instanc = {k: v for k, v in all_objs.items() if tokens[0] in k}
            if not all_instanc:
                print("** class doesn't exist **")
            else:
                for key, value in all_instanc.items():
                    obj_list.append(str(value))
                print(obj_list)
        return

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        tokens = line.split()
        storage.reload()
        all_objs = storage.all()

        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.__model_list:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        if len(tokens) == 2:
            print("** attribute name missing **")
            return
        if len(tokens) == 3:
            print("** valuue missing **")
            return
        cls_name, id_no, attr, val = tokens[0], tokens[1], tokens[2],\
            tokens[3].strip('"')
        usr_id = cls_name + "." + id_no
        if usr_id not in all_objs:
            print("** no instance found **")
            return
        for k, v in all_objs.items():
            if usr_id == k:
                setattr(v, attr, val)
                storage.save()
        return

    def default(self, line):
        """Defines a regex to match '<class name>.all()'"""
        str_to_match = r"(\w+)\.all\(\)"
        match = re.match(str_to_match, line)

        if match:
            cls_name = match.group(1)
            command = "all " + cls_name

            self.onecmd(command)
        else:
            print("*** Unknown syntax: ", line)
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
