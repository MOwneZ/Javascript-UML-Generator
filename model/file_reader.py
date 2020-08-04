# class for reading js files
class FileReader:
    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.file_contents = ""

    def __read_file(self):
        jsfile = open(self.file_dir)
        self.file_contents = jsfile.readlines()

    def get_file_contents(self):
        return self.file_contents
