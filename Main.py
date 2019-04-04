from PyQt5 import QtWidgets
import sys
import QtOutput
import googletrans
import BrowseFileSystem
import ReadURL
import time

class Translator(QtWidgets.QMainWindow, QtOutput.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Translator, self).__init__(parent)
        self.setupUi(self)
        self.LocalFileClass = lambda: BrowseFileSystem.FileSystemWindow()
        self.LocalURLClass = lambda: ReadURL.URLfetch()
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

    def Translate_Function(self):                                               # einfügen von text, anpassen von comboboxen bei übersetzung
        inputText = self.Text_Input.toPlainText()
        self.Text_Output.clear()
        OutputText = self.TranslateText(InputTranslate=inputText, InputLanguage=self.ComboInputValue, OutputLanguage=self.ComboOutputValue)
        self.Combo_Input.setCurrentText(str(self.TranslatedSource))
        self.Text_Output.append(OutputText)

    def TranslateText(self, InputTranslate, InputLanguage, OutputLanguage):     # eigentliche "übersetzung" findet hier statt
        output = self.TranslatorObj.translate(src=InputLanguage, dest=OutputLanguage, text=InputTranslate)
        self.TranslatedSource = str(output.src)
        if self.TranslatedSource == OutputLanguage:
            if OutputLanguage is not "en":
                self.ComboOutputValue = "en"
                self.Combo_Output.setCurrentText("en")
            elif OutputLanguage == "en":
                self.ComboOutputValue = "de"
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
        self.Text_Input.clear()
        self.Text_Input.insertPlainText(self.LocalFileClass().FinalOutputText)

    def ImportURL(self):
        self.Text_Input.clear()
        self.Text_Input.insertPlainText(self.LocalURLClass().ReturnURLContent)

def main():                                                             # mainloop
    app = QtWidgets.QApplication(sys.argv)
    form = Translator()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()