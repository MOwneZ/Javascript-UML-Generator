import argparse
from model.file_reader import FileReader
from model.file_selector import FileSelect
from model.js_uml_gen import JavaScriptReader
import cmd


class View(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "\nwelcome to this cmd. type help or ? for a list of commands.\n"
        self.prompt = "==>"
        self.name = ""
        self.fileType = ""
        self.file_dir = ""
        self.selectedDir = False
        self.parser = argparse.ArgumentParser()
        self.file_reader = FileReader()
        self.file_selector = FileSelect()
        self.js_reader = JavaScriptReader()

    def __addArgs(self):
        self.parser.add_argument("-j", "--jpg", help="The fileType you wish to select. Use either 'png' or 'jpg'",
                                 type=str)
        self.parser.add_argument("-p", "--png", help="The fileType you wish to select. Use either 'png' or 'jpg'",
                                 type=str)
        self.args = self.parser.parse_args()

    def do_setup(self):
        print("What is your name?")
        self.name = input()

    def do_exit(self):
        print("Goodbye!")
        return True

    def do_file_select(self, line):
        self.file_selector.select_file()

    def do_set_filetype(self, line):
        'Use this function to set desired file type. Use -j for jpeg or -p for png.'
        if line == self.args.j:
            self.fileType = "jpg"
        elif line == self.args.p:
            self.fileType = "png"

    def do_get_filetype(self, line):
        print(self.fileType)

    def start(self):
        self.__addArgs()
        self.cmdloop()


TheView = View()
TheView.start()
