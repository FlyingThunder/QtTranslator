from PyQt5 import QtWidgets
import sys
import QtOutput
import googletrans


class ExampleApp(QtWidgets.QMainWindow, QtOutput.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Button_Translate.clicked.connect(self.TextSwap_Function)
        self.Combo_Input.activated[str].connect(self.ComboBoxInput)
        self.Combo_Output.activated[str].connect(self.ComboBoxOutput)
        self.TranslatorObj = googletrans.Translator()

    def TextSwap_Function(self):
        if self.Text_Input.toPlainText():
            inputText = self.Text_Input.toPlainText()
        self.Text_Output.clear()
        OutputText = self.TranslateText(InputTranslate=inputText, InputLanguage=self.ComboInputValue, OutputLanguage=self.ComboOutputValue)
        self.Text_Output.append(OutputText)

    def TranslateText(self, InputTranslate, InputLanguage, OutputLanguage):
        output = self.TranslatorObj.translate(src=InputLanguage, dest=OutputLanguage, text=InputTranslate)
        return self.StringCleaning(inputString=output)

    def StringCleaning(self, inputString):
        TestList = str(inputString).lstrip("Translated").strip("(").strip(")")[:-51].split(",")[2][6:]
        return TestList

    def ComboBoxInput(self):
        self.ComboInputValue = str(self.Combo_Input.currentText())

    def ComboBoxOutput(self):
        self.ComboOutputValue = str(self.Combo_Output.currentText())                #TODO: More languages, more features

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()