
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UIMain
from UI.UIMain import Colors

from game import *


class UI(UIMain.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)
        self.setButtonHandlers()
        self.game = Game()
        self.token_colors = {Board.TOKEN1: Colors.red, Board.TOKEN2: Colors.green,
                             Board.TOKEN3: Colors.blue, Board.TOKEN4: Colors.yellow,
                             Board.FREE_SPACE: Colors.free_space, Board.NOT_USED: Colors.unused_space}

    def setButtonHandlers(self):
        self.btnLeft0.clicked.connect(lambda: self.leftBtnHandler(0))
        self.btnLeft1.clicked.connect(lambda: self.leftBtnHandler(1))
        self.btnLeft2.clicked.connect(lambda: self.leftBtnHandler(2))
        self.btnLeft3.clicked.connect(lambda: self.leftBtnHandler(3))
        self.btnLeft4.clicked.connect(lambda: self.leftBtnHandler(4))

        self.btnRight0.clicked.connect(lambda: self.rightBtnHandler(0))
        self.btnRight1.clicked.connect(lambda: self.rightBtnHandler(1))
        self.btnRight2.clicked.connect(lambda: self.rightBtnHandler(2))
        self.btnRight3.clicked.connect(lambda: self.rightBtnHandler(3))
        self.btnRight4.clicked.connect(lambda: self.rightBtnHandler(4))

        self.btnShuffle.clicked.connect(lambda: self.shuffleBtnHandler())

        for y in range(Board.HEIGTH):
            for x in range(Board.WIDTH):
                self.board_buttons[y][x].clicked.connect(
                    lambda row=y, col=x: self.boardBtnHandler(row, col))

        self.btnLoadInitialConfig.clicked.connect(lambda:
                                                  self.btnLoadFileHandler("init"))
        self.btnLoadFinalConfig.clicked.connect(lambda:
                                                self.btnLoadFileHandler("goal"))
        self.btnSaveFile.clicked.connect(self.btnSaveFileHandler)

    def leftBtnHandler(self, row):
        self.game.rotateRowLeft(row)
        self.redrawBoard()

    def rightBtnHandler(self, row):
        self.game.rotateRowRight(row)
        self.redrawBoard()

    def boardBtnHandler(self, row, col):
        print(row, col)
        self.game.moveFreeSpace(row, col)
        self.redrawBoard()
    # sets the right color on the respective button

    def redrawBoard(self):
        for y in range(Board.HEIGTH):
            for x in range(Board.WIDTH):
                self.board_buttons[y][x].setStyleSheet(
                    self.token_colors[self.game._board[y][x]])
        pass

    def btnLoadFileHandler(self, boardType):
        self.game.loadFile(self, boardType)
        self.redrawBoard()

    def btnSaveFileHandler(self):
        self.game.saveFile()
        print("Saving file")

    def shuffleBtnHandler(self):
        self.game.shuffle()
        self.redrawBoard()


if __name__ == '__main__':
    app = QApplication()
    qt_app = UI()
    qt_app.show()
    # qt_app.game.moveFreeSpaceDown()
    # qt_app.game.moveFreeSpaceDown()
    # qt_app.game.moveFreeSpaceDown()
    # qt_app.game.rotateRowRight(3)
    # qt_app.redrawBoard()
    # print(qt_app.token_colors)
    app.exec_()
