#!/usr/bin/python3
''' This module defines the console of this project '''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    '''
    This class defines the console of our program
    to create, update and destroy objects.
    '''

    prompt = "(hbnb) "
    __model_list = ["BaseModel"]

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
        #print(storage.all())
        if show_obj not in storage.all():
            print("** no instance found **")
        else:
            print("{}".format(storage.all()[show_obj]))
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
                to_obj = eval(value["__class__"])(**value)
                del value["__class__"]
                obj_list.append(str(to_obj))
            print(obj_list)
        elif tokens:
            all_instances = {k: v for k, v in all_objs.items() if tokens[0] in k}
            if not all_instances:
                print("** class doesn't exist **")
            else:
                for key, value in all_instances.items():
                    to_obj = eval(tokens[0])(**value)
                    obj_list.append(str(to_obj))
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
        cls_name, id_no, attr, val = tokens[0], tokens[1], tokens[2], tokens[3]
        usr_id = cls_name + "." + id_no
        if usr_id not in all_objs:
            print("** no instance found **")
            return
        for k, v in all_objs.items():
            if usr_id == k:
                v[attr] = val
                storage.save()
        """token_0_instances = {k: v for k, v in all_objs.items() if tokens[0] in k}
        if tokens[2] in token_0_instances.keys() and token_0_instnaces[token2[2]]["id"] == tokens[1]:
            new_dict = {}
            new_dict[token[2]] = token[1]
            token_0_instances.update(new_dict)
            print(token_0_intances)
            storage.save()"""
        '''Note: Not finished yet'''

        return




if __name__ == "__main__":
    HBNBCommand().cmdloop()
