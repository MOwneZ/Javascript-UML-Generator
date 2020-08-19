from esprima import parse


class JsParser:
    def __init__(self):
        self.js_file = ""
        self.js_file_parsed = {}
        self.all_my_classes = []

    def set_js_file(self, new_file):
        self.js_file = new_file

    def parse_js_file(self):
        self.js_file_parsed = parse(self.js_file)
        self.set_classes()

    def set_classes(self):
        for key, value in self.js_file_parsed.items():
            if key == "body":
                for aValue in value:
                    single_class = {"name": (self.set_class_name(aValue)),
                                    "attributes":
                                        (self.get_class_attributes(
                                            aValue.body.body)),
                                    "methods":
                                        self.get_class_methods(
                                            aValue.body.body)}
                    self.add_class(single_class)

    def set_class_name(self, new_value):
        return new_value.id.name

    def add_class(self, new_class):
        if new_class not in self.all_my_classes:
            self.all_my_classes.append(new_class)

    def get_class_attributes(self, new_class_body):
        attributes = []
        for value in new_class_body:
            if value.type == "MethodDefinition" \
                    and value.key.name == "constructor":
                for aValue in value.value.body.body:
                    attributes.append(aValue.expression.left.property.name)
        return attributes

    def get_class_methods(self, new_class_body):
        methods = []
        for value in new_class_body:
            if value.type == "MethodDefinition":
                methods.append(value.key.name)
        return methods
