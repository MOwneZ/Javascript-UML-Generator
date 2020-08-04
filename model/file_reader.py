# class for reading js files
class FileReader:
    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.file_contents = ""
        self.clean_file = ""

    # protected read file method
    def __read_file(self):
        js_file = open(self.file_dir)
        self.file_contents = js_file.readlines()
        for line in self.file_contents:
            self.clean_file += line

    # public get file contents, as well as runs other function
    def get_file_contents(self):
        self.__read_file()
        return self.clean_file
