import unittest
from model.directory_reader import DirectoryReader
from os import getcwd


class TestValidateDirectory(unittest.TestCase):

    def setUp(self):
        self.dir_reader = DirectoryReader()
        self.current_dir = getcwd()

    def test_bad_folder_dir(self):
        """Tests to see whether the DirectoryReader class can correctly invalidate a bad folder directory."""
        invalid_dir = "123123123"
        self.assertFalse(self.dir_reader.is_valid_folder_dir(invalid_dir))

    def test_good_folder_dir(self):
        """Tests to see whether the DirectoryReader class can correctly validate a good folder directory."""
        valid_dir = self.current_dir
        self.assertTrue(self.dir_reader.is_valid_folder_dir(valid_dir))

    def test_forward_slash_folder_dir(self):
        """Tests to see whether the DirectoryReader class can correctly validate a directory with forward slashes."""
        valid_dir = self.current_dir.replace("\\","/")
        self.assertTrue(self.dir_reader.is_valid_folder_dir(valid_dir))

    def test_mixed_dir(self):
        """Tests a half correct directory to see whether the DirectoryReader class can correctly validate a good
        folder directory. """
        invalid_dir = self.current_dir + "@@@INVALID_DIR"
        self.assertFalse(self.dir_reader.is_valid_folder_dir(invalid_dir))

    def test_good_js_dir(self):
        """Tests to see whether a provided correct directory contains at least 1 js file."""
        valid_dir = str.format("{}/testing_files", self.current_dir).replace("\\","/")
        self.assertTrue(self.dir_reader.is_valid_js_dir(valid_dir))

    def test_bad_js_dir(self):
        """Tests to see whether a provided correct directory contains at least no js files."""
        invalid_dir = self.current_dir
        self.assertFalse(self.dir_reader.is_valid_js_dir(invalid_dir))

    def test_select_js_files(self):
        """Tests to see whether the DirectoryReader class can correctly select ONLY js files and ignore all others."""
        valid_dir = str.format("{}/testing_files", self.current_dir).replace("\\","/")
        js_file_dirs = [str.format("{}/testing_files/test_file_1.js", self.current_dir).replace("\\","/"),
                        str.format("{}/testing_files/test_file_2.js", self.current_dir).replace("\\","/")]
        self.dir_reader.set_directory(valid_dir)
        self.assertEqual(self.dir_reader.get_file_dirs(), js_file_dirs)
