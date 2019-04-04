import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
loader.page().pdfPrintingFinished.connect(
    lambda *args: print('finished:', args))
loader.load(QtCore.QUrl('https://en.wikipedia.org/wiki/Main_Page'))

def emit_pdf(finished):
    loader.page().printToPdf("test.pdf")

loader.loadFinished.connect(emit_pdf)

app.exec()