import tkinter
from tkinter.filedialog import askopenfilename


# class for selecting individual js files
class FileSelect:
    def __init__(self):
        self.js_dir = ""

    # selecting a single file
    def select_file(self):
        root = tkinter.Tk()
        root.withdraw()
        self.js_dir = askopenfilename()

    # retrieving the selected file directory
    def get_dir(self):
        self.select_file()
        return self.js_dir
