class FileReader:
    def __init__(self):
        self.file_dir = ""
        self.file_contents = ""
        self.clean_file = ""

    def __read_file(self):
        js_file = open(self.file_dir)
        self.file_contents = js_file.readlines()
        for line in self.file_contents:
            self.clean_file += line

    def is_valid_file(self, new_dir):
        if str(new_dir).endswith(".js"):
            return True

    def set_file_dir(self, new_dir):
        self.file_dir = new_dir

    def get_file_contents(self):
        self.__read_file()
        return self.clean_file
