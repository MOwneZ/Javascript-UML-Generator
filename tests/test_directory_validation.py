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
