from esprima import parse


class JsToDot:
    def __init__(self):
        self.js_file = ""
        self.js_file_parsed = {}
        self.all_my_classes = []

    def set_js_file(self, new_file):
        self.js_file = new_file

    def parse(self):
        self.js_file_parsed = parse(self.js_file)

    def set_classes(self):
        for key, value in self.js_file_parsed.items():
            if key is "body":
                for aValue in value:
                    self.all_my_classes.append(aValue.id.name)
                    self.set_class_methods(aValue.body.body)
                    self.set_class_attributes(aValue.body.body)

    def set_class_methods(self, new_class_body):
        for value in new_class_body:
            if value.type is "MethodDefinition":
                print(value.key.name)

    def set_class_attributes(self, new_class_body):
        for value in new_class_body:
            if value.type is "MethodDefinition" and value.key.name == "constructor":
                for aValue in value.value.body.body:
                    print(aValue)

    def get_dict(self):
        return self.js_file_parsed
