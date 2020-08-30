from os import path


class FileReader:
    def __init__(self):
        self.__file_dir = ""
        self.__file_contents = ""
        self.__clean_file_contents = ""

    def __read_file(self):
        js_file = open(self.__file_dir)
        self.__file_contents = js_file.readlines()
        for line in self.__file_contents:
            self.__clean_file_contents += line
        js_file.close()

    def is_valid_file(self, new_dir):
        if str(new_dir).endswith(".js"):
            return True

    def is_valid_file_dir(self, new_dir):
        if path.isfile(new_dir):
            return True

    def __set_file_dir(self, new_dir):
        self.__file_dir = new_dir

    def get_file_contents(self, new_dir):
        self.__set_file_dir(new_dir)
        self.__read_file()
        return self.__clean_file_contents
