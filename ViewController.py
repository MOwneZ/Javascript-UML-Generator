import argparse
from model.file_reader import FileReader
from model.file_selector import FileSelect
from model.js_uml_gen import JavaScriptReader
import os
import cmd


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path. Try again.")


class View(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "\nwelcome to this cmd. type help or ? for a list of commands.\n" \
                     "Some commands require others to be completed first, if lost use the help menu."
        self.prompt = "==>"
        self.name = ""
        self.fileType = ""
        self.file_dir = ""
        self.selected_type = False
        self.selected_input_Dir = False
        self.selected_output_dir = False
        self.parser = argparse.ArgumentParser()
        self.file_reader = FileReader()
        self.file_selector = FileSelect()
        self.js_reader = JavaScriptReader()
        self.js_reader = JavaScriptReader()

    # allows the user to set their name.
    def do_set_name(self, arg):
        """This option allows to set your name, which can be added to the produced graphical documents. Type the
        command, followed by your name. Will accept all. """
        if arg != "":
            self.name = arg
            print(str.format("Name set to {}!", self.name))
        else:
            print("Please provide a name! You do not have to do this step if you do not want to.")

    def do_exit(self, arg):
        """This command closes the command line."""
        print("Goodbye! Won't miss you.")
        return True

    def do_set_input_dir(self, arg):
        """Type this command, followed by a valid directory, to choose the js file(s) to be turned into a diagram."""

    def do_set_output_dir(self, arg):
        """Type this command, followed by a valid directory, to choose the output of the diagram(s)."""

    # sets the desired filetype for the output document
    def do_set_filetype(self, arg):
        """Use this function to set desired file type for the output document. Type the command followed by either
        -jpg or -j for jpg, and -p or -png for png."""
        # setting the possible arguments for setting the filetype
        valid_jpg = ["jpg", "-jpg", "-j"]
        valid_png = ["png", "-png", "-p"]
        arg = str.lower(arg)
        if arg in valid_jpg:
            self.fileType = "jpg"
            self.selectedType = True
            print("set filetype to jpg!")
        elif arg in valid_png:
            self.fileType = "png"
            self.selectedType = True
            print("set filetype to png!")
        else:
            print("incorrect file type. Please type the command followed by either -jpg or -j for jpg, and -p or -png "
                  "for png.")

    # function to provide instructions to users as to how to use the program.
    def do_instructions(self, arg):
        """Provides instructions for using the program. Complete commands in this order."""
        print("To start, you can choose to select a name. Example: set_name Loufeng *OPTIONAL STEP*")
        print(str.format("Next, input the directory of the js files you wish to turn into a diagram. Example: "
                         "set_input_dir {} *NECESSARY STEP*", r"C:\Users\Luofeng\Desktop\jsfiles"))
        print(str.format("Next, input the directory of the produced image files. Example: set_output_dir {}"
              " *NECESSARY STEP*", r"C:\Users\Luofeng\Desktop\umlfiles"))
        print("Finally, select your desired file type. Example: set_filetype -jpg *NECESSARY STEP*")

    # starts the class
    def start(self):
        self.cmdloop()


TheView = View()
TheView.start()
