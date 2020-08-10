from model.file_reader import FileReader
from model.file_selector import FileSelect
from model.js_uml_gen import JavaScriptReader

TheFileSelector = FileSelect()
dir = TheFileSelector.get_dir()
TheFileReader = FileReader(dir)
TheJSReader = JavaScriptReader(TheFileReader.get_file_contents())
print(TheJSReader.get_raw())
