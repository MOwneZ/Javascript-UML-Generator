from esprima import parse
from nested_lookup import nested_lookup, get_all_keys


class JsToDot:
    def __init__(self):
        self.js_file = ""
        self.js_file_parsed = {}
        self.all_my_functions = []
        self.all_my_classes = []
        self.all_my_attributes = []

    def set_js_file(self, new_file):
        self.js_file = new_file

    def parse(self):
        self.js_file_parsed = parse(self.js_file)

    def get_parsed(self):
        for key, value in self.js_file_parsed.items():
            print(value)

    def set_classes(self):
        self.all_my_classes.append(self.js_file_parsed.body.get('type'))

    def get_classes(self):
        return self.js_file_parsed.body
