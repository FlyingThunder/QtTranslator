from cx_Freeze import setup, Executable

base = None
executables = [Executable("Main.py", base = "WIN32GUI")]

packages = ["idna","sys","googletrans","tika","odf","docx","QtOutput","BrowseFileSystem","LoadURLContent","multiprocessing"]
options = {
    'build_exe': {
        'packages':packages,
        'includes':["PyQt5","odf","docx","tika"]
    },
}

setup(
    name = "Translator",
    options = options,
    version = "1",
    description = 'Test .exe Build',
    executables = executables
)