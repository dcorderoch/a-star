from PySide2.QtWidgets import QMainWindow, QApplication
from GUI.window import Ui_MainWindow

class UI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication()
    qt_app = UI()
    qt_app.show()
    app.exec_()
