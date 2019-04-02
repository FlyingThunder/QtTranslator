import urllib
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

class URLfetch(QWidget):
    def importURL(self):
        i, okPressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if okPressed:
            self.getURLContent(i)

    def getURLContent(self, i):
        try:
            f = urllib.urlopen(i)
            myfile = f.read()
            print(myfile)
        except:
            print("invalid URL")

