from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import BrowseFileSystem
import sys
import os


class URLfetch(QWidget):

    def __init__(self):
        self.LocalFileClass = lambda: BrowseFileSystem.FileSystemWindow()
        self.ReturnURLContent = ""
        super().__init__()
        self.importURL()

    def importURL(self):
        i, okPressed = QInputDialog.getText(self, "Import website", "Site to import:", QLineEdit.Normal, "e.g. https://www.google.de")
        if okPressed:
            self.getURLContent(i)

    def getURLContent(self, url):
        LoadURLContent().getWebsite(site=url)
        self.getPDFcontent()

    def getPDFcontent(self):
        self.ReturnURLContent = self.LocalFileClass().getPDF(file = "temp.pdf")
        try:
            os.remove("temp.pdf")
        except:
            print("test2")

class LoadURLContent():



    def getWebsite(self, site):
        loader.setZoomFactor(1)
        loader.page().pdfPrintingFinished.connect(
            lambda *args: print('finished:', args))
        loader.load(QtCore.QUrl(site))

        def emit_pdf(finished):
            loader.page().printToPdf("temp.pdf")

        loader.loadFinished.connect(emit_pdf)

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()

if __name__ == '__main__':
    app.exec()





