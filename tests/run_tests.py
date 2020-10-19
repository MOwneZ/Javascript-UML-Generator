from unittest import TestLoader, TextTestRunner

# Thanks Nick Leslie for this code

loader = TestLoader()
start_directory = "./"
suite = loader.discover(start_directory)
runner = TextTestRunner().run(suite)
