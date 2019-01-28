from cx_Freeze import setup, Executable

base = None

executables = [Executable("Main.py", base=base)]

packages = ["idna","sys","googletrans","QtOutput","multiprocessing"]
options = {
    'build_exe': {
        'packages':packages,
        'includes':["PyQt5"]
    },
}

setup(
    name = "Translator",
    options = options,
    version = "1",
    description = 'Test .exe Build',
    executables = executables
)