from model.file_reader import FileReader
from model.js_uml_gen import JavaScriptReader
from model.directory_reader import DirectoryReader
from cmd import Cmd


class View(Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "\nwelcome to this cmd. type help or ? for a list of "\
                     "commands.\n" \
                     "Some commands require others to be completed first. If "\
                     "lost, use the help menu. "
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
        self.dir_reader = DirectoryReader()
        self.js_reader = JavaScriptReader()

    def do_set_name(self, arg):
        """This option allows to set your name, which can be added to the
        produced graphical documents. Type the command, followed by your
        name. Will accept all. """
        if arg != "":
            self.name = arg
            print(str.format("Name set to {}!", self.name))
        else:
            print(
                "Please provide a name! You do not have to do this step if "
                "you do not want to. It's ok, really.")

    def do_exit(self, arg):
        """This command closes the command line."""
        print("Goodbye! Won't miss you.")
        return True

    def do_set_input_dir(self, arg):
        """Type this command, followed by either 'folder' 'or file', then a
        valid directory, to choose the js file(s) to be turned into a
        diagram."""
        if arg == "folder":
            print("Please enter the folder directory of the files desired.")
            folder_dir = input().replace("\\", "/")
            if self.dir_reader.is_valid_js_dir(folder_dir):
                self.dir_reader.set_directory(folder_dir)
                print(str(self.dir_reader.all_my_file_dirs))
                print("Folder has been set to " + folder_dir)
            else:
                print("invalid directory! Please try again.")

        elif arg == "file":
            print("Please enter the directory of the file desired.")
            file_dir = input().replace("\\", "/")
            if self.file_reader.is_valid_file_dir(
                    file_dir) and self.file_reader.is_valid_file(file_dir):
                self.input_file_dir = file_dir
                print("File has been set to " + self.input_file_dir)
            else:
                print("invalid directory or filetype!. Please try again.")

        else:
            print(
                "Invalid syntax. Please type the command followed by "
                "'folder' or 'file'.")

    def do_set_output_dir(self, arg):
        """Type this command, followed by a valid directory, to choose the
        output of the diagram(s). """
        if not self.selected_type:
            print(
                "Please select a file type first before completing this step.")
        else:
            output_dir = arg.replace("\\", "/")
            if self.dir_reader.is_valid_folder_dir(output_dir):
                self.output_file_dir = output_dir
                print(str.format("Output directory set to [{}].",
                                 self.output_file_dir))
            else:
                print("Invalid directory/input. Please try again.")

    def do_set_filetype(self, arg):
        """Use this function to set desired file type for the output
        document. Type the command followed by either -jpg or -j for jpg,
        and -p or -png for png. """
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
            print(
                "incorrect file type. Please type the command followed by "
                "either -jpg or -j for jpg, and -p or -png "
                "for png.")

    def do_instructions(self, arg):
        """Provides instructions for using the program. Complete commands in
        this order for best understanding. """
        print(
            "To start, you can choose to select a name. Example: set_name "
            "Loufeng *OPTIONAL STEP*")
        print(str.format(
            "Next, input the directory of the js files you wish to turn into "
            "a diagram. Example: "
            "set_input_dir {} *NECESSARY STEP*",
            r"C:\Users\Luofeng\Desktop\jsfiles"))
        print(str.format(
            "Next, input the directory of the produced image files. Example: "
            "set_output_dir {} "
            " *NECESSARY STEP*", r"C:\Users\Luofeng\Desktop\umlfiles"))
        print(
            "Next, select your desired file type. Example: set_filetype -jpg "
            "*NECESSARY STEP*")
        print(
            "Finally, you can make the graphical document. Example: "
            "create_uml *NECESSARY STEP*")

    def do_produce_diagram(self, arg):
        """This command uses all the information provided so far and will
        produce a diagram based on input. """
        if self.selected_type is True\
                and self.selected_output_dir is True\
                and self.selected_input_Dir is True:
            print("do this")
        else:
            print(
                "Not all pre conditions met. Please review the instructions "
                "by typing 'instructions' for help.")

    def start(self):
        """Simple function which starts the program."""
        self.cmdloop()
