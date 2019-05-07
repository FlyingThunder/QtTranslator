import sys
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["idna","sys","googletrans","tika","odf","docx","re","time", "shutil", "functools","multiprocessing"], 
    "includes": ["QtOutput", "Settings", "BrowseFileSystem"] # <-- Include easy_gui
}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(  name = "Translator",
        version = "0.1",
        description = "Python 3 Translator with PyQt5",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py", base=base)])