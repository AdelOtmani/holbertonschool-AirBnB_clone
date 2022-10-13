#!/usr/bin/python3
"""Project AirBnB holberton A. Otmani
    """
import cmd

class HBNBCommand(cmd.Cmd):
    """Console initialisation Hbnb
    """
    prompt = '(hbnb)'

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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
