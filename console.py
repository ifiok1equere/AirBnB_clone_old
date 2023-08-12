#!/usr/bin/python3
''' This module defines the console of this project '''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


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
        # print("line: ", line)
        # print(len(line))
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.__model_list:
            print("** class doesn't exist **")
            return
        #cls_name = tokens[0]
        obj = eval(tokens[0])()
        print(obj)
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
        del_obj = tokens[0] + "." + usr_id
        storage.reload()
        if del_obj not in storage.all():
            print("** no instance found **")
        elif del_obj in storage.all():
            del storage.all()[del_tok]
            storage.save()
            return

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name in a list"""
        tokens = line.split()
        storage.reload()
        all_objs =storage.all()
        if not tokens and all_objs:
            print([value for value in all_objs.values()])
        elif tokens:
            all_instances = [v for k, v in all_objs.items()
                            if tokens[0] in k]
            if len(all_instances) == 0:
                print("** class doesn't exist **")
            else:
                print(all_instances)

    #def do_update(self, line):
    #    """Updates an instance based on the class name
    #        and id by adding or updating attribute"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
