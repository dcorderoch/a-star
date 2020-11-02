from PySide2 import QtWidgets
from UI import UI

class UI(UIMain.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = UI()
    qt_app.show()
    app.exec_()
