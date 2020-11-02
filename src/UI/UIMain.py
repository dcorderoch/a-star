# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 5.15.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Colors():
    red = "background-color: rgb(255, 103, 103);"
    green = "background-color: rgb(0, 170, 127);"
    blue = "background-color: rgb(88, 155, 255);"
    yellow = "background-color: rgb(255, 255, 127);"
    free_space = "background-color: rgb(255, 255, 255);"
    unused_space = ""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1144, 930)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.btn00 = QPushButton(self.centralwidget)
        self.btn00.setObjectName(u"btn00")
        self.btn00.setGeometry(QRect(330, 210, 111, 111))
        self.btn00.setStyleSheet(u"background-color: rgb(255, 103, 103);")

        self.btn01 = QPushButton(self.centralwidget)
        self.btn01.setObjectName(u"btn01")
        self.btn01.setGeometry(QRect(460, 210, 111, 111))
        self.btn01.setStyleSheet(u"background-color: rgb(0, 170, 127);")

        self.btn02 = QPushButton(self.centralwidget)
        self.btn02.setObjectName(u"btn02")
        self.btn02.setGeometry(QRect(590, 210, 111, 111))
        self.btn02.setStyleSheet(u"background-color: rgb(88, 155, 255);")

        self.btn03 = QPushButton(self.centralwidget)
        self.btn03.setObjectName(u"btn03")
        self.btn03.setGeometry(QRect(720, 210, 111, 111))
        self.btn03.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.btn10 = QPushButton(self.centralwidget)
        self.btn10.setObjectName(u"btn10")
        self.btn10.setGeometry(QRect(330, 330, 111, 111))
        self.btn10.setStyleSheet(u"background-color: rgb(255, 103, 103);")

        self.btn11 = QPushButton(self.centralwidget)
        self.btn11.setObjectName(u"btn11")
        self.btn11.setGeometry(QRect(460, 330, 111, 111))
        self.btn11.setStyleSheet(u"background-color: rgb(0, 170, 127);")

        self.btn12 = QPushButton(self.centralwidget)
        self.btn12.setObjectName(u"btn12")
        self.btn12.setGeometry(QRect(590, 330, 111, 111))
        self.btn12.setStyleSheet(u"background-color: rgb(88, 155, 255);")

        self.btn13 = QPushButton(self.centralwidget)
        self.btn13.setObjectName(u"btn13")
        self.btn13.setGeometry(QRect(720, 330, 111, 111))
        self.btn13.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.btn20 = QPushButton(self.centralwidget)
        self.btn20.setObjectName(u"btn20")
        self.btn20.setGeometry(QRect(330, 450, 111, 111))
        self.btn20.setStyleSheet(u"background-color: rgb(255, 103, 103);")

        self.btn21 = QPushButton(self.centralwidget)
        self.btn21.setObjectName(u"btn21")
        self.btn21.setGeometry(QRect(460, 450, 111, 111))
        self.btn21.setStyleSheet(u"background-color: rgb(0, 170, 127);")

        self.btn22 = QPushButton(self.centralwidget)
        self.btn22.setObjectName(u"btn22")
        self.btn22.setGeometry(QRect(590, 450, 111, 111))
        self.btn22.setStyleSheet(u"background-color: rgb(88, 155, 255);")

        self.btn23 = QPushButton(self.centralwidget)
        self.btn23.setObjectName(u"btn23")
        self.btn23.setGeometry(QRect(720, 450, 111, 111))
        self.btn23.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.btn31 = QPushButton(self.centralwidget)
        self.btn31.setObjectName(u"btn31")
        self.btn31.setGeometry(QRect(460, 570, 111, 111))
        self.btn31.setStyleSheet(u"background-color: rgb(0, 170, 127);")

        self.btn30 = QPushButton(self.centralwidget)
        self.btn30.setObjectName(u"btn30")
        self.btn30.setGeometry(QRect(330, 570, 111, 111))
        self.btn30.setStyleSheet(u"background-color: rgb(255, 103, 103);")

        self.btn32 = QPushButton(self.centralwidget)
        self.btn32.setObjectName(u"btn32")
        self.btn32.setGeometry(QRect(590, 570, 111, 111))
        self.btn32.setStyleSheet(u"background-color: rgb(88, 155, 255);")

        self.btn33 = QPushButton(self.centralwidget)
        self.btn33.setObjectName(u"btn33")
        self.btn33.setGeometry(QRect(720, 570, 111, 111))
        self.btn33.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.btnRight4 = QPushButton(self.centralwidget)
        self.btnRight4.setObjectName(u"btnRight4")
        self.btnRight4.setGeometry(QRect(870, 610, 111, 31))
        self.btnRight2 = QPushButton(self.centralwidget)
        self.btnRight2.setObjectName(u"btnRight2")
        self.btnRight2.setGeometry(QRect(870, 370, 111, 31))
        self.btnRight1 = QPushButton(self.centralwidget)
        self.btnRight1.setObjectName(u"btnRight1")
        self.btnRight1.setGeometry(QRect(870, 250, 111, 31))
        self.btnRight3 = QPushButton(self.centralwidget)
        self.btnRight3.setObjectName(u"btnRight3")
        self.btnRight3.setGeometry(QRect(870, 490, 111, 31))
        self.btnLeft1 = QPushButton(self.centralwidget)
        self.btnLeft1.setObjectName(u"btnLeft1")
        self.btnLeft1.setGeometry(QRect(184, 250, 111, 31))
        self.btnLeft3 = QPushButton(self.centralwidget)
        self.btnLeft3.setObjectName(u"btnLeft3")
        self.btnLeft3.setGeometry(QRect(184, 490, 111, 31))
        self.btnLeft4 = QPushButton(self.centralwidget)
        self.btnLeft4.setObjectName(u"btnLeft4")
        self.btnLeft4.setGeometry(QRect(184, 610, 111, 31))
        self.btnLeft2 = QPushButton(self.centralwidget)
        self.btnLeft2.setObjectName(u"btnLeft2")
        self.btnLeft2.setGeometry(QRect(184, 370, 111, 31))
        self.btnComodin3 = QPushButton(self.centralwidget)
        self.btnComodin3.setObjectName(u"btnComodin3")
        self.btnComodin3.setGeometry(QRect(590, 90, 111, 111))
        self.btnComodin3.setStyleSheet(Colors.unused_space)
        self.btnLeft0 = QPushButton(self.centralwidget)
        self.btnLeft0.setObjectName(u"btnLeft0")
        self.btnLeft0.setGeometry(QRect(184, 130, 111, 31))
        self.btnComodin4 = QPushButton(self.centralwidget)
        self.btnComodin4.setObjectName(u"btnComodin4")
        self.btnComodin4.setGeometry(QRect(720, 90, 111, 111))
        self.btnComodin4.setStyleSheet(Colors.free_space)
        self.btnComodin2 = QPushButton(self.centralwidget)
        self.btnComodin2.setObjectName(u"btnComodin2")
        self.btnComodin2.setGeometry(QRect(460, 90, 111, 111))
        self.btnComodin2.setStyleSheet(Colors.unused_space)
        self.btnRight0 = QPushButton(self.centralwidget)
        self.btnRight0.setObjectName(u"btnRight0")
        self.btnRight0.setGeometry(QRect(870, 130, 111, 31))
        self.btnComodin1 = QPushButton(self.centralwidget)
        self.btnComodin1.setObjectName(u"btnComodin1")
        self.btnComodin1.setGeometry(QRect(330, 90, 111, 111))
        self.btnComodin1.setStyleSheet(Colors.unused_space)

        self.btnLoadInitialConfig = QPushButton(self.centralwidget)
        self.btnLoadInitialConfig.setObjectName(u"btnLoadInitialConfig")
        self.btnLoadInitialConfig.setGeometry(QRect(330, 720, 111, 31))

        self.btnLoadFinalConfig = QPushButton(self.centralwidget)
        self.btnLoadFinalConfig.setObjectName(u"btnLoadFinalConfig")
        self.btnLoadFinalConfig.setGeometry(QRect(460, 720, 111, 31))

        self.btnResolve = QPushButton(self.centralwidget)
        self.btnResolve.setObjectName(u"btnResolve")
        self.btnResolve.setGeometry(QRect(590, 720, 111, 31))

        self.btnShuffle = QPushButton(self.centralwidget)
        self.btnShuffle.setObjectName(u"btnShuffle")
        self.btnShuffle.setGeometry(QRect(720, 720, 111, 31))

        self.btnSaveFile = QPushButton(self.centralwidget)
        self.btnSaveFile.setObjectName(u"btnSaveFile")
        self.btnSaveFile.setGeometry(QRect(330, 790, 111, 31))

        self.btnIntruction = QPushButton(self.centralwidget)
        self.btnIntruction.setObjectName(u"btnIntruction")
        self.btnIntruction.setGeometry(QRect(460, 790, 111, 31))

        self.btnPlaySolution = QPushButton(self.centralwidget)
        self.btnPlaySolution.setObjectName(u"btnPlaySolution")
        self.btnPlaySolution.setGeometry(QRect(590, 790, 111, 31))

        self.btnSaveConfiguration = QPushButton(self.centralwidget)
        self.btnSaveConfiguration.setObjectName(u"btnSaveConfiguration")
        self.btnSaveConfiguration.setGeometry(QRect(720, 790, 111, 31))

        self.btnPreviousStep = QPushButton(self.centralwidget)
        self.btnPreviousStep.setObjectName(u"btnPreviousStep")
        self.btnPreviousStep.setGeometry(QRect(330, 860, 111, 31))
        self.btnPreviousStep.setEnabled(False)

        self.btnNextStep = QPushButton(self.centralwidget)
        self.btnNextStep.setObjectName(u"btnNextStep")
        self.btnNextStep.setGeometry(QRect(460, 860, 111, 31))
        self.btnNextStep.setEnabled(False)

        self.btnFirstStep = QPushButton(self.centralwidget)
        self.btnFirstStep.setObjectName(u"btnFirstStep")
        self.btnFirstStep.setGeometry(QRect(590, 860, 111, 31))
        self.btnFirstStep.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1144, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.layout = [[self.btn00, self.btn01, self.btn02, self.btn03],
                       [self.btn10, self.btn11, self.btn12, self.btn13],
                       [self.btn20, self.btn21, self.btn22, self.btn23],
                       [self.btn30, self.btn31, self.btn32, self.btn33]]

        self.retranslateUi(MainWindow)

        self.board_buttons = [[self.btnComodin1, self.btnComodin2, self.btnComodin3, self.btnComodin4],
                              [self.btn00, self.btn01, self.btn02, self.btn03],
                              [self.btn10, self.btn11, self.btn12, self.btn13],
                              [self.btn20, self.btn21, self.btn22, self.btn23],
                              [self.btn30, self.btn31, self.btn32, self.btn33]]

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def get_color_square(self, row, column):
        return self.layout[row][column]

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.btn00.setText("")
        self.btn01.setText("")
        self.btn02.setText("")
        self.btn03.setText("")
        self.btn10.setText("")
        self.btn11.setText("")
        self.btn12.setText("")
        self.btn13.setText("")
        self.btn20.setText("")
        self.btn21.setText("")
        self.btn22.setText("")
        self.btn23.setText("")
        self.btn30.setText("")
        self.btn31.setText("")
        self.btn32.setText("")
        self.btn33.setText("")

        self.btnComodin1.setText("")
        self.btnComodin2.setText("")
        self.btnComodin3.setText("")
        self.btnComodin4.setText("")

        self.btnRight4.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Derecha", None))
        self.btnRight2.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Derecha", None))
        self.btnRight1.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Derecha", None))
        self.btnRight3.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Derecha", None))
        self.btnLeft1.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Izquierda", None))
        self.btnLeft3.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Izquierda", None))
        self.btnLeft4.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Izquierda", None))
        self.btnLeft2.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Izquierda", None))
        self.btnLeft0.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Izquierda", None))
        self.btnRight0.setText(QCoreApplication.translate(
            "MainWindow", u"Rotar Derecha", None))

        self.btnLoadInitialConfig.setText(QCoreApplication.translate(
            "MainWindow", u"Cargar Conf. Inicial", None))

        self.btnLoadFinalConfig.setText(QCoreApplication.translate(
            "MainWindow", u"Cargar Conf. Final", None))

        self.btnResolve.setText(QCoreApplication.translate(
            "MainWindow", u"Resolver", None))

        self.btnShuffle.setText(QCoreApplication.translate(
            "MainWindow", u"Shuffle", None))

        self.btnSaveFile.setText(QCoreApplication.translate(
            "MainWindow", u"Guardar Configu.", None))

        self.btnIntruction.setText(QCoreApplication.translate(
            "MainWindow", u"Ver Instrucciones", None))
        self.btnIntruction.clicked.connect(self.btnIntructionHandler)

        self.btnPlaySolution.setText(QCoreApplication.translate(
            "MainWindow", u"Play Solution", None))

        self.btnSaveConfiguration.setText(QCoreApplication.translate(
            "MainWindow", u"Guardar Conf. Final", None))

        self.btnNextStep.setText(QCoreApplication.translate(
            "MainWindow", u"Paso Siguiente", None))

        self.btnPreviousStep.setText(QCoreApplication.translate(
            "MainWindow", u"Paso Anterior", None))

        self.btnFirstStep.setText(QCoreApplication.translate(
            "MainWindow", u"Paso Inicial", None))
    # retranslateUi

    # Mostrar las instrucciones
    def gameInfo():
        return

    def btnIntructionHandler(self):
        print("Instruction Button pressed")
        self.showIntructions()

    def showIntructions(self):
        msg = QMessageBox(self)
        msg.setText("Posibles Movimientos")
        msg.setInformativeText(
            "1) Rotar Derecha: Desplaza a la derecha un espacio cada pieza en una fila\n"
            "2) Rotar Izquierda: Desplazar a la Izquierda un espacio cada pieza en una fila\n"
            "3) Desplazamiento Vertical: Desplazar el espacio en blanco de manera vertical 1,2,3 o 4 espacios (Columnas)")
        msg.setWindowTitle("Instrucciones de Juego")
        ret = msg.exec_()
