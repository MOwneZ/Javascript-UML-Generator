import cmd
import argparse
from model.file_reader import FileReader
from model.file_selector import FileSelect
from model.js_uml_gen import JavaScriptReader
import cmd


class View(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "welcome to this cmd. type help or ? for a list of commands.\n"
        self.prompt = "==>"
        self.name = ""
        self.fileType = ""
        self.selectedDir = False
        self.parser = argparse.ArgumentParser()
        self.file_reader = FileReader()
        self.file_selector = FileSelect()
        self.js_reader = JavaScriptReader()

    def __addArgs(self):
        self.parser.add_argument("filetype", help="The fileType you wish to select. Use either 'png' or 'jpg'",
                                 type=str)

    def do_greet(self, line):
        print("Hello " + line)
        self.name = line

    def do_eof(self, line):
        return True

    def do_file_type(self, line):
        correct_input = ["png", "jpg"]
        print("which file format do you want to use? png or jpg")
        answer = line
        if answer in correct_input:
            print(answer + " selected.")
        else:
            print("wrong syntax. try again")

    def start(self):
        self.__addArgs()
        self.cmdloop()
