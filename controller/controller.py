from model.file_reader import FileReader
from model.file_selector import FileSelect

TheFileSelector = FileSelect()
dir = TheFileSelector.get_dir()
TheFileReader = FileReader(dir)
print(TheFileReader.get_file_contents())
