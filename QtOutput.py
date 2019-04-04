from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 345)
        MainWindow.setMaximumSize(QtCore.QSize(790, 402))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(663, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(795, 414))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Label_Output = QtWidgets.QLabel(self.centralwidget)
        self.Label_Output.setObjectName("Label_Output")
        self.verticalLayout_2.addWidget(self.Label_Output, 0, QtCore.Qt.AlignHCenter)
        self.Text_Output = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_Output.setObjectName("Text_Output")
        self.verticalLayout_2.addWidget(self.Text_Output)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Combo_Output = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_Output.setObjectName("Combo_Output")
        self.Combo_Output.addItem("")
        self.Combo_Output.addItem("")
        self.Combo_Output.addItem("")
        self.horizontalLayout.addWidget(self.Combo_Output)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Label_Input = QtWidgets.QLabel(self.centralwidget)
        self.Label_Input.setObjectName("Label_Input")
        self.verticalLayout.addWidget(self.Label_Input, 0, QtCore.Qt.AlignHCenter)
        self.Text_Input = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_Input.setUndoRedoEnabled(False)
        self.Text_Input.setObjectName("Text_Input")
        self.verticalLayout.addWidget(self.Text_Input)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Combo_Input = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_Input.setEnabled(True)
        self.Combo_Input.setObjectName("Combo_Input")
        self.Combo_Input.addItem("")
        self.Combo_Input.addItem("")
        self.Combo_Input.addItem("")
        self.Combo_Input.addItem("")
        self.horizontalLayout_2.addWidget(self.Combo_Input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.ButtonLayout = QtWidgets.QVBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")
        self.Button_Clean = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Clean.setObjectName("Button_Clean")
        self.ButtonLayout.addWidget(self.Button_Clean)
        self.Button_Translate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Translate.setObjectName("Button_Translate")
        self.ButtonLayout.addWidget(self.Button_Translate)
        self.Button_Swap = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Swap.setObjectName("Button_Swap")
        self.ButtonLayout.addWidget(self.Button_Swap)
        self.gridLayout.addLayout(self.ButtonLayout, 1, 1, 1, 1)
        #self.ButtonImportFile = QtWidgets.QPushButton(self.centralwidget)
        #self.ButtonImportFile.setObjectName("ImportFile")

        self.menubar = self.menuBar()                                       # initiiere menüleiste
        self.fileMenu = self.menubar.addMenu('&Import...')                  # füge menüpunkt hinzu
        self.fileImport = QtWidgets.QAction('&Import File', self)           # definiere aktion zu unterpunkt
        self.fileMenu.addAction(self.fileImport)                            # füge menü unterpunkt hinzu

        self.URLImport = QtWidgets.QAction('&Import Site', self)
        self.fileMenu.addAction(self.URLImport)

        #self.gridLayout.addWidget(self.ButtonImportFile, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label_Output.setText(_translate("MainWindow", "Translated result:"))
        self.Text_Output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Combo_Output.setItemText(0, _translate("MainWindow", "en"))
        self.Combo_Output.setItemText(1, _translate("MainWindow", "de"))
        self.Combo_Output.setItemText(2, _translate("MainWindow", "ru"))
        self.Label_Input.setText(_translate("MainWindow", "Input:"))
        self.Text_Input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Combo_Input.setItemText(0, _translate("MainWindow", "Auto"))
        self.Combo_Input.setItemText(1, _translate("MainWindow", "en"))
        self.Combo_Input.setItemText(2, _translate("MainWindow", "de"))
        self.Combo_Input.setItemText(3, _translate("MainWindow", "ru"))
        self.Button_Clean.setText(_translate("MainWindow", "Clean"))
        self.Button_Translate.setText(_translate("MainWindow", "=>"))
        self.Button_Swap.setText(_translate("MainWindow", "<->"))
        #self.ButtonImportFile.setText(_translate("MainWindow", "Import File"))

