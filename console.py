#!/usr/bin/python3
"""The entry point of our airBnB Project"""
import cmd
from shlex import split
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """a classthat contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    __my_classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """end of line"""
        print("")
        return True

    def emptyline(self):
        """empty line, do nothing"""
        pass

    def do_create(self, arg):
        """create a class instance and print id"""
        argument_len = parse(arg)

        if len(argument_len) == 0:
            print("** class name missing **")
        elif argument_len[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        else:
            print(eval(argument_len[0])().id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an
            instance based on the class name and id
        """
        argument = parse(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return

        if argument[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
            return

        """instance of id missing"""
        if len(argument) < 2:
            print("** instance id missing **")
            return

        i_ins = argument[1]
        key = "{}.{}".format(argument[0], i_ins)

        """Check if it's in storage"""
        if key not in storage.all():
            print("** no instance found **")
            return

        """Retrieve instance"""
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        argument = parse(arg)
        if len(argument) == 0:
            print("** class name missing **")
            return

        if argument[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
            return

        if len(argument) < 2:
            print("** instance id missing **")
            return

        ins_id = argument[1]
        key = "{}.{}".format(argument[0], ins_id)

        """Check if it's in storage"""
        if key not in storage.all():
            print("** no instance found **")
            return

        """destroy functionality"""
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        argument = parse(arg)

        if len(argument) > 0 and argument[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
            return

        obj_placeh = []
        for obj in storage.all().values():
            if len(argument) > 0 and argument[0] == obj.__class__.__name__:
                obj_placeh.append(obj.__str__())
            elif len(argument) == 0:
                obj_placeh.append(obj.__str__())
        print(obj_placeh)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change in
        o the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        argument = parse(arg)

        if len(argument) == 0:
            print("** class name missing **")
            return False

        if argument[0] not in HBNBCommand().__my_classes:
            print("** class doesn't exist **")
            return False

        if len(argument) < 2:
            print("** instance id missing **")
            return False

        id_ins = argument[1]
        key = "{}.{}".format(argument[0], id_ins)

        """Check if it's in storage"""
        if key not in storage.all():
            print("** no instance found **")
            return False

        if len(argument) == 2:
            print("** attribute name missing **")
            return False

        if len(argument) == 3:
            try:
                if type(eval(argument[2])) == dict:
                    print("** value missing **")
                    return
            except NameError:
                pass

        if len(argument) == 4:
            obj = storage.all()[key]
            if argument[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argument[2]])
                obj.__dict__[argument[2]] = valtype(argument[3])
            else:
                obj.__dict__[argument[2]] = argument[3]
        elif type(eval(argument[2])) == dict:
            obj = storage.all()[key]
            for k, v in eval(argument[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
