from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import BrowseFileSystem
import sys
import os
import time
from tika import parser

class URLfetch(QWidget):

    def __init__(self):
        self.scriptpath = (os.path.dirname(os.path.realpath(__file__)))
        self.LocalFileClass = lambda: BrowseFileSystem.FileSystemWindow()
        self.ReturnURLContent = ""
        super().__init__()
        self.importURL()

    def getPDF(self, file):
        fileName = file
        raw = parser.from_file(fileName)
        self.FinalOutputText = raw['content']
        return self.FinalOutputText

    def getPDFcontent(self):
        self.ReturnURLContent = self.LocalFileClass().getPDF(file = "temp.pdf")
        # self.getPDF(file = "temp.pdf")
        # self.LocalFileClass().getPDF(file = "temp.pdf")
        # try:
        #     os.remove("temp.pdf")
        # except:
        #     print("test3")

    def importURL(self):
        i, okPressed = QInputDialog.getText(self, "Import website", "Site to import:", QLineEdit.Normal, "e.g. https://www.google.de")
        if okPressed:
            self.getURLContent(i)

    def getURLContent(self, url):
        LoadURLContent().getWebsite(site=url)
        print("test1")

        x = True
        while x == True:
            try:
                self.getPDFcontent()
                print("test6")
                x = False
            except:
                pass
            print("test4") # TODO: LOOP, IMPLEMENT BrowseFileSystem.GetPDF
            time.sleep(1)





class LoadURLContent():

    def getWebsite(self, site):
        print("test2")
        loader.setZoomFactor(1)
        loader.page().pdfPrintingFinished.connect(
            lambda *args: print('finished:', args))
        loader.load(QtCore.QUrl(site))
        print("test3")


        def emit_pdf(finished):
            loader.page().printToPdf("temp.pdf")


        loader.loadFinished.connect(emit_pdf)

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()

if __name__ == '__main__':
    app.exec()





