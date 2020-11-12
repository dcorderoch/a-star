import threading
import time

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Astar import *
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
        self.solved = False
        self.curr_step = 0
        self.last_step = 0
        self.solution = []
        self.playing_solution = False

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

        self.btnShuffle.clicked.connect(self.shuffleBtnHandler)
        self.btnResolve.clicked.connect(self.resolveBtnHandler)
        self.btnNextStep.clicked.connect(self.stepAheadSolution)
        self.btnPreviousStep.clicked.connect(self.stepBackSolution)
        self.btnFirstStep.clicked.connect(self.restartSteps)

        self.btnPlaySolution.clicked.connect(self.playSolutionBtnHandler)

        for y in range(Board.HEIGTH):
            for x in range(Board.WIDTH):
                self.board_buttons[y][x].clicked.connect(
                    lambda row=y, col=x: self.boardBtnHandler(row, col))

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

    def resolveBtnHandler(self):
        if not self.solved:
            current_board = tuple(tuple(i) for i in self.game._board)
            final_board = tuple(tuple(i) for i in self.game._final_board)
            self.solution = AStar().astar(current_board, final_board, False)
            if self.solution != None:
                self.solved = True
                self.last_step = len(self.solution)

                self.btnNextStep.setEnabled(True)
                self.btnPlaySolution.setEnabled(True)
            else:
                print("no solucionó nada")
        pass

    def stepAheadSolution(self):
        self.curr_step += 1
        current_step_board = self.solution[self.curr_step]
        self.game._board = [list(i) for i in current_step_board]

        self.redrawBoard()

        pass

    def stepBackSolution(self):
        self.curr_step -= 1
        current_step_board = self.solution[self.curr_step]
        self.game._board = [list(i) for i in current_step_board]

        self.redrawBoard()
        pass

    def restartSteps(self):
        if self.solved and self.curr_step != 0:
            self.curr_step = 0
            current_step_board = self.solution[self.curr_step]
            self.game._board = [list(i) for i in current_step_board]

            self.redrawBoard()
        pass

    def playSolutionBtnHandler(self):
        if not self.playing_solution:
            self.playing_solution = True
            # thread.start_new_thread(self.playSolution)
            t = threading.Thread(target=self.playSolution)
            t.start()
            self.btnPlaySolution.setText(QCoreApplication.translate(
                "MainWindow", u"Pause", None))
        else:
            self.playing_solution = False
            self.btnPlaySolution.setText(QCoreApplication.translate(
                "MainWindow", u"Play", None))

        pass

    def playSolution(self):
        while self.curr_step < self.last_step-1 and self.playing_solution:
            self.stepAheadSolution()
            time.sleep(1.5)
        self.playing_solution = False

    def redrawBoard(self):

        # manage buttons
        if self.solved:
            if self.curr_step == self.last_step - 1:
                self.btnNextStep.setEnabled(False)
            else:
                self.btnNextStep.setEnabled(True)

            if self.curr_step == 0:
                self.btnPreviousStep.setEnabled(False)
                self.btnFirstStep.setEnabled(False)
            else:
                self.btnPreviousStep.setEnabled(True)
                self.btnFirstStep.setEnabled(True)

        for y in range(Board.HEIGTH):
            for x in range(Board.WIDTH):
                self.board_buttons[y][x].setStyleSheet(
                    self.token_colors[self.game._board[y][x]])

        self.show()
        pass

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
