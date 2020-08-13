import unittest
from model.file_reader import FileReader
from os import getcwd


class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.file_reader = FileReader()
        self.good_dir = getcwd()