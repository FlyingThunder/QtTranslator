from PyQt5 import QtWidgets
import sys
import QtOutput
import googletrans


class ExampleApp(QtWidgets.QMainWindow, QtOutput.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Button_Swap.clicked.connect(lambda: self.ButtonClicked(ButtonType="swap"))
        self.Button_Translate.clicked.connect(lambda: self.ButtonClicked(ButtonType="trans"))
        self.Combo_Input.activated[str].connect(self.ComboBoxInput)
        self.Combo_Output.activated[str].connect(self.ComboBoxOutput)
        self.TranslatorObj = googletrans.Translator()
        self.ComboInputValue = "auto"
        self.ComboOutputValue = "en"

    def ButtonClicked(self, ButtonType):
        if ButtonType == "trans":
            if self.Text_Input.toPlainText():
                self.Translate_Function()
        if ButtonType == "swap":
            if self.Text_Input.toPlainText() and self.Text_Output.toPlainText():
                self.TextBoxSwap()
                self.ComboBoxSwap()

    def Translate_Function(self):
        inputText = self.Text_Input.toPlainText()
        self.Text_Output.clear()
        if not self.ComboOutputValue:
            self.ComboOutputValue = "en"
        if not self.ComboInputValue:
            self.ComboInputValue = "auto"
        OutputText = self.TranslateText(InputTranslate=inputText, InputLanguage=self.ComboInputValue, OutputLanguage=self.ComboOutputValue)
        self.Text_Output.append(OutputText)

    def TranslateText(self, InputTranslate, InputLanguage, OutputLanguage):
        output = self.TranslatorObj.translate(src=InputLanguage, dest=OutputLanguage, text=InputTranslate)
        return self.StringCleaning(inputString=output)

    def StringCleaning(self, inputString):
        print(str(inputString))
        TranslatedText = str(inputString).lstrip("Translated").strip("(").strip(")").split(",")[2].split("=")[1]
        self.TranslatedSource = str(inputString).lstrip("Translated").strip("(").strip(")").split(",")[0].split("=")[1]
        return TranslatedText

    def ComboBoxInput(self):
        self.ComboInputValue = str(self.Combo_Input.currentText())

    def ComboBoxOutput(self):
        self.ComboOutputValue = str(self.Combo_Output.currentText())

    def TextBoxSwap(self):
        InputBox = self.Text_Input.toPlainText()
        OutputBox = self.Text_Output.toPlainText()
        self.Text_Input.clear()
        self.Text_Input.append(OutputBox)
        self.Text_Output.clear()
        self.Text_Output.append(InputBox)

    def ComboBoxSwap(self):
        if self.Combo_Input.currentText() == "Auto":
            InputComboBox = self.TranslatedSource
        else:
            InputComboBox = self.Combo_Input.currentText()

        OutPutComboBox = self.Combo_Output.currentText()
        self.Combo_Input.setCurrentText(OutPutComboBox)
        self.Combo_Output.setCurrentText(InputComboBox)
        self.ComboBoxInput()
        self.ComboBoxOutput()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()