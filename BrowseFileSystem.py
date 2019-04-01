from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from odf import text, teletype
from odf.opendocument import load
import sys


class FileSystemWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Filedialog'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py);;Text Files (*.txt);;OpenOffice Files (*.odt);;Microsoft Word Files (*.docx);;PDF Files (*.pdf)", options=options)
        if fileName:
            if ".odt" in fileName:
                self.OutputFinal = self.getODTText()

    def getODTText(self):
        textdoc = load("Test.odt")
        allparas = textdoc.getElementsByType(text.P)
        return teletype.extractText(allparas[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileSystemWindow()
    sys.exit(app.exec_())