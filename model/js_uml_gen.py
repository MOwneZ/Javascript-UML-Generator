import re
import ast

#   '(\S+)[(].*[)].*{'

class JavaScriptReader:
    def __init__(self, raw_file):
        self.raw_file = raw_file
        self.classes = []
        self.functions = []
        self.string = ""
        self.open_count = int

    def __remove_extras(self):
        self.raw_file = self.raw_file.replace(" ", "")
        self.raw_file = self.raw_file.replace("\n", "")

    def __get_classes(self):
        node = ast.parse(self.raw_file)
        self.classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

    def __get_functions(self):
        node = ast.parse(self.raw_file)
        self.functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]

    def get_raw(self):
        self.__get_classes()
        self.__get_functions()
        return self.raw_file

    def __isolate_func(self):
        for str in self.raw_file:
            while self.open_count != 0:
                if str == "{":
                    self.open_count += 1
                if str == "}":
                    self.open_count -= 1
                self.string += str
