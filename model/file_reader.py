# class for reading js files
class FileReader:
    def __init__(self):
        self.file_dir = ""
        self.file_contents = ""
        self.clean_file = ""

    # protected read file method
    def __read_file(self):
        js_file = open(self.file_dir)
        self.file_contents = js_file.readlines()
        for line in self.file_contents:
            self.clean_file += line

    # sets the file directory for the class
    def set_file_dir(self, new_dir):
        self.file_dir = new_dir

    # public get file contents, as well as runs other function
    def get_file_contents(self):
        self.__read_file()
        return self.clean_file
