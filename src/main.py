from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2 import QtWidgets
from UI import UIMain


from game import *

class UI(UIMain.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.game = Game()
        self.setupUi(self)
        self.set_button_handlers()
    # Handler of the Load Button, to calls the file opener

    def btnLoadFileHandler(self):
        print("Button pressed")
        self.openFileOpener()
    # btnLoadFileHandler

    # File opener function, to open and read the .txt with the configuration
    def openFileOpener(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        if path != '':
            print('file:', path)
            with open(path, "r") as config:
                initialConfig = config.readlines()
                self.game.loadConfig(initialConfig, self)
    # openFileOpener

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = UI()
    qt_app.show()
    app.exec_()
