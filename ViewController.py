from model.file_reader import FileReader
from model.file_selector import FileSelect
from model.js_uml_gen import JavaScriptReader
import cmd
import os


class View(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "\nwelcome to this cmd. type help or ? for a list of commands.\n" \
                     "Some commands require others to be completed first, if lost use the help menu."
        self.prompt = "==>"
        self.name = ""
        self.fileType = ""
        self.output_file_dir = ""
        self.input_file_dir = ""
        self.input_folder_dir = ""
        self.selected_type = False
        self.selected_input_Dir = False
        self.selected_output_dir = False
        self.file_reader = FileReader()
        self.file_selector = FileSelect()
        self.js_reader = JavaScriptReader()

    # allows the user to set their name.
    def do_set_name(self, arg):
        """This option allows to set your name, which can be added to the produced graphical documents. Type the
        command, followed by your name. Will accept all. """
        if arg != "":
            self.name = arg
            print(str.format("Name set to {}!", self.name))
        else:
            print("Please provide a name! You do not have to do this step if you do not want to.")

    def do_exit(self, arg):
        """This command closes the command line."""
        print("Goodbye! Won't miss you.")
        return True

    def do_set_input_dir(self, arg):
        """Type this command, followed by either 'folder' 'or file', then a valid directory, to choose the js file(s)
        to be turned into a diagram. """
        if arg == "folder":
            print("Please enter the folder directory of the files desired.")
            folder_dir = input()
            if self.check_folder_input_dir(folder_dir):
                self.input_folder_dir = folder_dir
                print(str.format("Folder has been set to {}"), self.input_folder_dir)
            else:
                print("invalid directory. Please try again.")
        if arg == "file":
            print("Please enter the directory of the file desired.")
            file_dir = input()
            if self.check_file_input_dir(file_dir):
                self.input_file_dir = file_dir
                print(str.format("File has been set to {}"), self.input_file_dir)
            else:
                print("invalid directory. Please try again.")
        else:
            print("Invalid syntax. Please type the command followed by 'folder' or 'file'.")


    def do_set_output_dir(self, arg):
        """Type this command, followed by a valid directory, to choose the output of the diagram(s)."""
        if not self.selected_type:
            print("Please select a file type first before completing this step.")
        else:
            if self.check_output_dir(arg):
                self.output_file_dir = arg
                print(str.format("Output directory set to [{}].", self.output_file_dir))
            else:
                print("Invalid directory. Please try again.")

    # sets the desired file type for the output document
    def do_set_filetype(self, arg):
        """Use this function to set desired file type for the output document. Type the command followed by either
        -jpg or -j for jpg, and -p or -png for png."""
        # setting the possible arguments for setting the file type
        valid_jpg = ["jpg", "-jpg", "-j"]
        valid_png = ["png", "-png", "-p"]
        arg = str.lower(arg)
        if arg in valid_jpg:
            self.fileType = "jpg"
            self.selected_type = True
            print("set file type to jpg!")
        elif arg in valid_png:
            self.fileType = "png"
            self.selected_type = True
            print("set file type to png!")
        else:
            print("incorrect file type. Please type the command followed by either -jpg or -j for jpg, and -p or -png "
                  "for png.")

    # function to provide instructions to users as to how to use the program.
    def do_instructions(self, arg):
        """Provides instructions for using the program. Complete commands in this order."""
        print("To start, you can choose to select a name. Example: set_name Loufeng *OPTIONAL STEP*")
        print(str.format("Next, input the directory of the js files you wish to turn into a diagram. Example: "
                         "set_input_dir {} *NECESSARY STEP*", r"C:\Users\Luofeng\Desktop\jsfiles"))
        print(str.format("Next, input the directory of the produced image files. Example: set_output_dir {}"
                         " *NECESSARY STEP*", r"C:\Users\Luofeng\Desktop\umlfiles"))
        print("Next, select your desired file type. Example: set_filetype -jpg *NECESSARY STEP*")
        print("Finally, you can make the graphical document. Example: create_uml *NECESSARY STEP*")

    # starts the class
    def start(self):
        self.cmdloop()

    # checks the output directory provided - returns true if it's a valid directory, and false if it isn't.
    def check_output_dir(self, path):
        if os.path.isdir(path):
            return True

    # checks the input directory to ensure it's a folder. returns true if valid, false if not.
    def check_folder_input_dir(self, path):
        if os.path.isdir(path):
            return True

    # checks the input directory to ensure it's a single file. returns true if valid, false if not.
    def check_file_input_dir(self, path):
        if os.path.isfile(path):
            return True

TheView = View()
TheView.start()
