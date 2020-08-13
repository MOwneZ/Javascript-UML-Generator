from os import listdir


class DirectoryReader:
    def __init__(self):
        self.all_my_files = []
        self.all_my_file_dirs = []
        self.folder_dir = ""

    def set_directory(self, new_folder_path):
        self.folder_dir = new_folder_path
        self.all_my_files = listdir(new_folder_path)
        self.__set_file_dirs()

    def is_valid_dir(self, new_folder_path):
        files_to_check = listdir(new_folder_path)
        for file in files_to_check:
            if not str(file).endswith(".js"):
                return False
        return True

    def __set_file_dirs(self):
        for file in self.all_my_files:
            self.all_my_file_dirs.append(str.format("{}/{}", self.folder_dir, file))

    def get_file_dirs(self):
        return self.all_my_file_dirs
