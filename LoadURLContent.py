from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QWidget
import sys
from tika import parser

class LoadHTML(QWidget):

    def __init__(self):
        super().__init__()
        self.output = ".pdf import failed"

    def getPDF(self):
        raw = parser.from_file("temp.pdf")
        self.output = raw['content']


    def getWebsite(self, site):
        self.app = QtWidgets.QApplication(sys.argv)
        self.loader = QtWebEngineWidgets.QWebEngineView()
        self.loader.setZoomFactor(1)
        self.loader.page().pdfPrintingFinished.connect(self.getPDF)
        self.loader.load(QtCore.QUrl(site))


        def emit_pdf(finished):
            self.loader.page().printToPdf("temp.pdf")


        self.loader.loadFinished.connect(emit_pdf)
        return self.output


if __name__ == '__main__':
    LoadHTML().app.exec()