import tkinter
from tkinter.filedialog import askopenfilename


class FolderSelect:
    def __init__(self):
        self.js_dir = ""

    def __select_file(self):
        root = tkinter.Tk()
        root.withdraw()
        self.js_dir = askopenfilename()

    def get_dir(self):
        self.__select_file()
        return self.js_dir


theFolderSelect = FolderSelect()
file_dir = theFolderSelect.get_dir()
print(file_dir)
