from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import sys

class LoadURLContent():


    def getWebsite(self, site):
        app = QtWidgets.QApplication(sys.argv)
        loader = QtWebEngineWidgets.QWebEngineView()

        print("test2")
        loader.setZoomFactor(1)
        loader.page().pdfPrintingFinished.connect(
            lambda *args: print('finished:', args))
        loader.load(QtCore.QUrl(site))
        print("test3")


        def emit_pdf(finished):
            loader.show()
            loader.page().printToPdf("temp.pdf")


        loader.loadFinished.connect(emit_pdf)
        print("PDF created")

        if __name__ == '__main__':
            app.exec()

LoadURLContent().getWebsite("http://zetcode.com/gui/pyqt5/menustoolbars/")