import unittest
from model.file_reader import FileReader
from os import getcwd


class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.file_reader = FileReader()
        self.current_dir = getcwd()

    def test_read_txt_file(self):
        """This test simply tests the basic reader - whether it can correctly
         read a regular .txt file"""
        file_dir = str.format("{}/testing_files/not_a_js_file.txt",
                              self.current_dir).replace("\\", "/")
        file_contents = "This is not a JS file!"
        self.assertEqual(self.file_reader.get_file_contents(file_dir),
                         file_contents)

    def test_read_js_file(self):
        """This tests to ensure it can correctly read a .js file contents"""
        file_dir = str.format("{}/testing_files/test_file_1.js",
                              self.current_dir).replace("\\", "/")
        file_contents = "class TestClass {	  testFunction() {    " \
                        "this.doSomething()   }  } "
        self.assertEqual(self.file_reader.get_file_contents(file_dir),
                         file_contents)
