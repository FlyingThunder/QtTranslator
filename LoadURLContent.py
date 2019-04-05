from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QWidget
import sys
from tika import parser

class LoadHTML(QWidget):

    def __init__(self):
        super().__init__()
        self.printapp = QtWidgets.QApplication(sys.argv)
        self.loader = QtWebEngineWidgets.QWebEngineView()

    def getPDF(self, file):
        fileName = file
        raw = parser.from_file(fileName)
        return raw['content']


    def getWebsite(self, site):
        self.loader.setZoomFactor(1)
        self.loader.page().pdfPrintingFinished.connect(self.pdfCreated)
        self.loader.load(QtCore.QUrl(site))


        def emit_pdf(finished):
            self.loader.page().printToPdf("temp.pdf")


        self.loader.loadFinished.connect(emit_pdf)


    def pdfCreated(self):
        print("pdf generated")
        return(self.getPDF("temp.pdf"))


if __name__ == '__main__':
    LoadHTML().printapp.exec()