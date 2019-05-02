from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import sys
import QtOutput
import Settings
import googletrans
import BrowseFileSystem
import re
import os
import time
from tika import parser


class Translator(QtWidgets.QMainWindow, QtOutput.Ui_MainWindow):
    def __init__(self, parent=None):
        try:
            os.remove("temp.pdf")
        except:
            pass
        super(Translator, self).__init__(parent)
        self.setupUi(self)
        self.dialog = ShowSettings(self)
        self.setupUx()

    def setupUx(self):
        self.Button_Swap.clicked.connect(lambda: self.ButtonClicked(ButtonType="swap"))
        self.Button_Translate.clicked.connect(lambda: self.ButtonClicked(ButtonType="trans"))
        self.Button_Clean.clicked.connect(self.Clean_Textbox)
        self.Combo_Input.activated[str].connect(self.ComboBoxInput)
        self.Combo_Output.activated[str].connect(self.ComboBoxOutput)
        self.TranslatorObj = googletrans.Translator()
        self.ComboInputValue = "auto"
        self.ComboOutputValue = "en"
        self.fileImport.triggered.connect(self.ImportFile)
        self.URLImport.triggered.connect(self.ImportURL)
        self.MenuSettings.triggered.connect(self.SettingsMenu)



    def ButtonClicked(self, ButtonType):                                        # funktionsaufrufe bei knopfdruck
        if ButtonType == "trans":
            if self.Text_Input.toPlainText():
                self.Translate_Function()
        if ButtonType == "swap":
            if self.Text_Input.toPlainText() and self.Text_Output.toPlainText():
                self.TextBoxSwap()
                self.ComboBoxSwap()

    def Clean_Textbox(self):
        self.Text_Input.clear()
        self.Text_Output.clear()
        try:
            print(self.dialog.setting1var)
        except:
            print("nicht zugewiesen")

    def saveOutput(self):
        resultname = self.Text_Output.toPlainText()[0:10]
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open(resultname+"_"+timestr+".txt", "w") as x:
            x.write(self.Text_Output.toPlainText())
        x.close()


    def Translate_Function(self):                                               # einfügen von text, anpassen von comboboxen bei übersetzung
        inputText = self.Text_Input.toPlainText()
        self.Text_Output.clear()
        if int(len(inputText))<5000:
            OutputText = self.TranslateText(InputTranslate=inputText, InputLanguage=self.ComboInputValue, OutputLanguage=self.ComboOutputValue)
            self.Combo_Input.setCurrentText(str(self.TranslatedSource))
            self.Text_Output.append(OutputText)
            if self.dialog.setting2var == 1:
                self.saveOutput()

    def TranslateText(self, InputTranslate, InputLanguage, OutputLanguage):      # eigentliche "übersetzung" findet hier statt
        output = self.TranslatorObj.translate(src=InputLanguage, dest=OutputLanguage, text=InputTranslate)
        self.TranslatedSource = str(output.src)
        if self.TranslatedSource == OutputLanguage:             #wenn die sprache des zu übersetzenden textes und die zielsprache identisch ist, dann...
            if OutputLanguage is not "en":                      #wenn die ausgangssprache nicht englisch ist:
                self.ComboOutputValue = "en"                    #ausgangssprache auf englisch setzen
                self.Combo_Output.setCurrentText("en")
            elif OutputLanguage == "en":                        #wenn die ausgangssprache englisch ist:
                self.ComboOutputValue = "de"                    #ausgangssprache auf deutsch setzen
                self.Combo_Output.setCurrentText("de")
            output = self.TranslatorObj.translate(src=InputLanguage, dest=self.ComboOutputValue, text=InputTranslate)
        return str(output.text)

    def ComboBoxInput(self):
        self.ComboInputValue = str(self.Combo_Input.currentText())      # ändert den wert der input sprach-combobox wenn benutzer dies tut

    def ComboBoxOutput(self):
        self.ComboOutputValue = str(self.Combo_Output.currentText())    # ändert den wert der output sprach-combobox wenn benutzer dies tut

    def TextBoxSwap(self):                                              # tauscht den text der linken und rechten textbox miteinander
        InputBox = self.Text_Input.toPlainText()
        OutputBox = self.Text_Output.toPlainText()
        self.Text_Input.clear()
        self.Text_Input.append(OutputBox)
        self.Text_Output.clear()
        self.Text_Output.append(InputBox)

    def ComboBoxSwap(self):                                             # tauscht beim tauschen des texts auch die sprachen aus der combobox
        if self.Combo_Input.currentText() == "Auto":
            InputComboBox = self.TranslatedSource                       # ersetzt "auto" durch die inputsprache, da die output-sprache nicht auto sein darf
        else:
            InputComboBox = self.Combo_Input.currentText()

        OutPutComboBox = self.Combo_Output.currentText()
        self.Combo_Input.setCurrentText(OutPutComboBox)
        self.Combo_Output.setCurrentText(InputComboBox)
        self.ComboBoxInput()
        self.ComboBoxOutput()

    def ImportFile(self):                                               # ruft das BrowseFileSystem modul
        localFileclass = BrowseFileSystem.FileSystemWindow()
        self.Text_Input.clear()
        self.Text_Input.insertPlainText(localFileclass.FinalOutputText[0:4999])         #text auf 5000 zeichen begrenzen (limitation von der google translate API)

    def getPDF(self):                       #pdf auslesen
        raw = parser.from_file("temp.pdf")
        self.output = raw['content']            #plaintext auslesen
        self.Text_Input.clear()
        self.cutOutput = re.sub(r'(\n)\1+', r'\1', self.output)
        if self.dialog.setting1var == 1:                                    #einstellung, um URLs aus dem text zu entfernen
            self.cutURLOutput = re.sub('http[^\n]+\n', '', self.cutOutput)
            self.Text_Input.insertPlainText(self.cutURLOutput[0:4999])
        else:
            self.Text_Input.insertPlainText(self.cutOutput[0:4999])       #plaintext formatieren (leere zeilen und umbrüche formatieren und auf max. 5000 zeichen begrenzen)


    def getWebsite(self, site):             #webseite als pdf speichern
        loader = QtWebEngineWidgets.QWebEngineView()
        loader.setZoomFactor(1)
        loader.load(QtCore.QUrl(site))
        def emit_pdf(finished):
            loader.page().printToPdf("temp.pdf")                #inhalt als PDF datei speichern
            loader.page().pdfPrintingFinished.connect(lambda: self.getPDF())        #wenn PDF datei gespeichert wurde getPDF aufrufen
        loader.loadFinished.connect(emit_pdf)                   #wenn HTML inhalt geladen ist emit_pdf aufrufen

    def ImportURL(self):                     #URL dialog aufrufen
        i, okPressed = QtWidgets.QInputDialog.getText(self, "Import website", "Site to import:", QtWidgets.QLineEdit.Normal, "https://www.google.de")

        if okPressed:
            self.getWebsite(i)

    def SettingsMenu(self):
        self.dialog.show()

    def closeEvent(self, event):            #temporäre datei entfernen
        try:
            os.remove("temp.pdf")
        except:
            pass

class ShowSettings(Settings.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ShowSettings, self).__init__(parent)
        self.setupUi(self)
        self.setting1var = 0
        self.setting2var = 0
        self.checkBox.stateChanged.connect(self.setting1)
        self.checkBox_2.stateChanged.connect(self.setting2)
        self.checkBox_3.stateChanged.connect(self.setting3)
        self.checkBox_4.stateChanged.connect(self.setting4)

    def setting1(self):
        if self.checkBox.isChecked():
            self.setting1var = 1
        else:
            self.setting1var = 0

    def setting2(self):
        if self.checkBox_2.isChecked():
            self.setting2var = 1
        else:
            self.setting2var = 0

    def setting3(self):
        pass

    def setting4(self):
        pass



def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Translator()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
