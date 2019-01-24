# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_Mini.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 287)
        MainWindow.setMaximumSize(QtCore.QSize(790, 402))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(663, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(795, 414))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.InputLayout = QtWidgets.QVBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.Label_Input = QtWidgets.QLabel(self.centralwidget)
        self.Label_Input.setObjectName("Label_Input")
        self.InputLayout.addWidget(self.Label_Input, 0, QtCore.Qt.AlignHCenter)
        self.Text_Input = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_Input.setObjectName("Text_Input")
        self.InputLayout.addWidget(self.Text_Input)
        self.Combo_Input = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_Input.setObjectName("Combo_Input")
        self.Combo_Input.addItem("")
        self.Combo_Input.addItem("")
        self.InputLayout.addWidget(self.Combo_Input, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.InputLayout, 0, 0, 1, 1)
        self.ButtonLayout = QtWidgets.QVBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")
        self.Button_Translate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Translate.setObjectName("Button_Translate")
        self.ButtonLayout.addWidget(self.Button_Translate)
        self.Button_Swap = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Swap.setObjectName("Button_Swap")
        self.ButtonLayout.addWidget(self.Button_Swap)
        self.gridLayout.addLayout(self.ButtonLayout, 0, 1, 1, 1)
        self.OutputLayout = QtWidgets.QVBoxLayout()
        self.OutputLayout.setObjectName("OutputLayout")
        self.Label_Output = QtWidgets.QLabel(self.centralwidget)
        self.Label_Output.setObjectName("Label_Output")
        self.OutputLayout.addWidget(self.Label_Output, 0, QtCore.Qt.AlignHCenter)
        self.Text_Output = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_Output.setObjectName("Text_Output")
        self.OutputLayout.addWidget(self.Text_Output)
        self.Combo_Output = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_Output.setObjectName("Combo_Output")
        self.Combo_Output.addItem("")
        self.Combo_Output.addItem("")
        self.OutputLayout.addWidget(self.Combo_Output, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.OutputLayout, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label_Input.setText(_translate("MainWindow", "Input:"))
        self.Text_Input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Combo_Input.setItemText(0, _translate("MainWindow", "en"))
        self.Combo_Input.setItemText(1, _translate("MainWindow", "de"))
        self.Button_Translate.setText(_translate("MainWindow", "=>"))
        self.Button_Swap.setText(_translate("MainWindow", "<->"))
        self.Label_Output.setText(_translate("MainWindow", "Translated result:"))
        self.Text_Output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Combo_Output.setItemText(0, _translate("MainWindow", "de"))
        self.Combo_Output.setItemText(1, _translate("MainWindow", "en"))

