from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from odf import text, teletype
from odf.opendocument import load
from tika import parser
import docx
import sys


class FileSystemWindow(QWidget):
    def __init__(self):
        self.FinalOutputText = ""
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
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py);;Text Files (*.txt);;OpenOffice Files (*.odt);;Microsoft Word Files (*.docx);;PDF Files (*.pdf)", options=options)
        if self.fileName:
            if ".odt" in self.fileName:
                self.getODTText(file = self.fileName)

            elif ".docx" in self.fileName:
                self.getDOCXText(file = self.fileName)

            elif ".txt" in self.fileName:
                self.getTXT(file = self.fileName)

            elif ".pdf" in self.fileName:
                self.getPDF(file = self.fileName)

            else:
                QMessageBox.about(self, "Error", "Invalid file type")


    def getODTText(self, file):
        fileName = file
        textdoc = load(fileName)
        allparas = textdoc.getElementsByType(text.P)
        outputlist = []
        for x in allparas:
            outputlist.append(teletype.extractText(x))
        self.FinalOutputText = "".join(outputlist)

    def getDOCXText(self, file):
        fileName = file
        doc = docx.Document(fileName)
        allText = []
        for docpara in doc.paragraphs:
            print(docpara.text)
            allText.append(docpara.text)
        self.FinalOutputText = allText[0]

    def getTXT(self, file):
        fileName = file
        with open(fileName, "r") as xfile:
            self.FinalOutputText = xfile.read()

    def getPDF(self, file):
        fileName = file
        raw = parser.from_file(fileName)
        self.FinalOutputText = raw['content']
        return self.FinalOutputText

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileSystemWindow()
    sys.exit(app.exec_())