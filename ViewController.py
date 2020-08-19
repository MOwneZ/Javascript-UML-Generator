from model.file_reader import FileReader
from model.js_parser import JsParser
from model.directory_reader import DirectoryReader
from model.class_to_dot import ClassToDot
from cmd import Cmd
from os import listdir


class View(Cmd):

    def __init__(self):
        super().__init__()
        self.intro = "\nwelcome to this cmd. type help or ? for a list of " \
                     "commands.\n" \
                     "Some commands require others to be completed first. If " \
                     "lost, use the help menu."
        self.prompt = "==>  "
        self.name = ""
        self.file_type = "jpg"
        self.output_file_dir = ""
        self.selected_output_dir = False
        self.file_reader = FileReader()
        self.dir_reader = DirectoryReader()
        self.js_reader = JsParser()

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

    def do_set_output_dir(self, arg):
        output_dir = arg.replace("\\", "/")
        if self.dir_reader.is_valid_folder_dir(output_dir):
            self.output_file_dir = output_dir
            self.selected_output_dir = True
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
            self.file_type = "jpg"
            print("set file type to jpg!")
        elif arg in valid_png:
            self.file_type = "png"
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
            "Next, input the directory of the produced image files. Example: "
            "set_output_dir {} "
            " *NECESSARY STEP*", r"C:\Users\Luofeng\Desktop\umlfiles"))
        print(
            "Next, select your desired file type. Example: set_filetype -jpg "
            "*OPTIONAL STEP* - by default it's jpg")
        print(
            str.format("Finally, you can make the graphical document by "
                       "providing an input directory of a file or files."
                       " Example: create_uml {}*NECESSARY STEP*"),
            r"C:\Users\Luofeng\Desktop\jsfiles")

    def do_create_uml(self, arg):
        """This command uses all the information provided so far and will
        produce a diagram based on input. """
        directory = arg.replace("\\", "/")
        if self.dir_reader.is_valid_js_dir(directory):
            for file in listdir(directory):
                file_dir = directory + "/" + file
                self.js_reader.set_js_file(
                    self.file_reader.get_file_contents(file_dir))
                self.js_reader.parse_js_file()
            for aClass in self.js_reader.all_my_classes:
                print(aClass)
        else:
            print(
                "Please select an output directory and/or provide a valid "
                "input directory.")

    def start(self):
        """Simple function which starts the program."""
        self.cmdloop()
