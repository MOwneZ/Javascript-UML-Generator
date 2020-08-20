from unittest import TestCase
from os import getcwd
from model.js_parser import JsParser
from model.file_reader import FileReader
from model.directory_reader import DirectoryReader


class TestJsParser(TestCase):

    def setUp(self):
        self.js_parser = JsParser()
        self.file_reader = FileReader()
        self.dir_reader = DirectoryReader()
        self.current_dir = getcwd()

    def test_basic_class(self):
        """Tests to see whether it can correctly read a js file with a
        basic class."""
        expected_class = {
            'name': 'TestClass',
            'attributes': ['name', 'allMySports'],
            'methods': ['constructor', 'testFunction']}
        file_dir = str.format("{}/testing_files/test_file_1.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        self.js_parser.set_js_file(js_file)
        self.js_parser.parse_js_file()
        actual_class = self.js_parser.all_my_classes[0]
        self.assertEqual(expected_class, actual_class)

    def test_class_no_methods_attributes(self):
        """Tests to see whether it can correctly read a js file with a class
        with no methods or attributes"""
        expected_class = {
            'name': 'TestClass',
            'attributes': [],
            'methods': []}
        file_dir = str.format("{}/testing_files/test_file_3.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        self.js_parser.set_js_file(js_file)
        self.js_parser.parse_js_file()
        actual_class = self.js_parser.all_my_classes[0]
        self.assertEqual(expected_class, actual_class)

    def test_class_no_methods(self):
        """Tests to see whether it can correctly read a js file with an empty
        constructor."""
        expected_class = {
            'name': 'TestClass',
            'attributes': ['attribute1', 'attribute2'],
            'methods': ['constructor']}
        file_dir = str.format("{}/testing_files/test_file_4.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        self.js_parser.set_js_file(js_file)
        self.js_parser.parse_js_file()
        actual_class = self.js_parser.all_my_classes[0]
        self.assertEqual(expected_class, actual_class)

    def test_multiple_classes(self):
        """Tests to see whether it can correctly read a js file with multiple
        classes."""
        expected_classes = [{
            'name': 'TestClass1',
            'attributes': ['attribute1', 'attribute2'],
            'methods': ['constructor']},
            {
                'name': 'TestClass2',
                'attributes': ['attribute1', 'attribute2'],
                'methods': ['constructor']},
            {
                'name': 'TestClass3',
                'attributes': ['attribute1', 'attribute2'],
                'methods': ['constructor']}]
        file_dir = str.format("{}/testing_files/test_file_2.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        self.js_parser.set_js_file(js_file)
        self.js_parser.parse_js_file()
        actual_classes = self.js_parser.all_my_classes
        self.assertEqual(expected_classes, actual_classes)

    def test_no_classes(self):
        """Tests to see whether it returns an empty list when there are
        no classes."""
        expected_classes = []
        file_dir = str.format("{}/testing_files/test_file_empty.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        self.js_parser.set_js_file(js_file)
        self.js_parser.parse_js_file()
        actual_classes = self.js_parser.all_my_classes
        self.assertEqual(expected_classes, actual_classes)

    def test_entire_class(self):
        """Tests to see whether it returns an empty list when the provided
        file is not compatible."""
        expected_classes = []
        file_dir = str.format("{}/testing_files/test_file_bad.js",
                              self.current_dir).replace("\\", "/")
        js_file = self.file_reader.get_file_contents(file_dir)
        self.js_parser.set_js_file(js_file)
        self.js_parser.parse_js_file()
        actual_classes = self.js_parser.all_my_classes
        self.assertEqual(expected_classes, actual_classes)

    def test_entire_dir(self):
        """Tests to see whether it can read an entire directory and extract
        all the classes."""
        expected_class_count = 4
        dir = str.format("{}/testing_files/test_four_classes",
                         self.current_dir).replace("\\", "/")
        self.dir_reader.set_directory(dir)
        for aDir in self.dir_reader.all_my_file_dirs:
            js_file = self.file_reader.get_file_contents(aDir)
            self.js_parser.set_js_file(js_file)
            self.js_parser.parse_js_file()
        actual_class_count = len(self.js_parser.all_my_classes)
        self.assertEqual(expected_class_count, actual_class_count)
