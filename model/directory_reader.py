from os import listdir, path


class DirectoryReader:
    def __init__(self):
        self.all_my_files = []
        self.all_my_file_dirs = []
        self.folder_dir = ""

    def set_directory(self, new_folder_path):
        self.folder_dir = new_folder_path
        self.all_my_files = listdir(new_folder_path)
        self.__set_file_dirs()

    def is_valid_js_dir(self, new_folder_path):
        """Will return true if the provided directory\
         contains at least 1 javascript file. (.js)"""
        files_to_check = listdir(new_folder_path)
        for file in files_to_check:
            if str(file).endswith(".js"):
                return True
        return False

    def is_valid_folder_dir(self, new_folder_path):
        if path.isdir(new_folder_path):
            return True

    def __set_file_dirs(self):
        for file in self.all_my_files:
            if str(file).endswith(".js"):
                self.all_my_file_dirs.append(str.format("{}/{}",
                                                        self.folder_dir,
                                                        file))

    def get_file_dirs(self):
        return self.all_my_file_dirs
