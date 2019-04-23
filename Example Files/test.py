#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def importPDF(self):
        #app = QtWidgets.QApplication(sys.argv)
        loader = QtWebEngineWidgets.QWebEngineView()
        loader.setZoomFactor(1)
        loader.page().pdfPrintingFinished.connect(
            lambda *args: print('finished:', args))
        loader.load(QtCore.QUrl('https://en.wikipedia.org/wiki/Main_Page'))

        def emit_pdf(finished):
            loader.show()
            loader.page().printToPdf("test.pdf")

        loader.loadFinished.connect(emit_pdf)

        #app.exec()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.importPDF)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())