from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

class URLfetch(QWidget):
    def __init__(self):
        self.ReturnURLContent = ""
        super().__init__()
        self.importURL()

    def importURL(self):
        i, okPressed = QInputDialog.getText(self, "Import website", "Site to import:", QLineEdit.Normal, "https://www.google.de")
        if okPressed:
            self.getURLContent(i)

    def getURLContent(self, i):
        self.ReturnURLContent = i



