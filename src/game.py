#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random as ran
class Board():
    NOT_USED = -1
    FREE_SPACE = 0
    TOKEN1 = 1
    TOKEN2 = 2
    TOKEN3 = 3
    TOKEN4 = 4
    WIDTH = 4
    HEIGTH = 5

class BoardMoves():
    RIGHT = 1
    LEFT = 0
    MV_WHTSPC = 2

class Position():
    def __init__(self, x, y):
        self.col = x
        self.row = y

class Game():
    def __init__(self):
        # el primer row del tablero solo puede contener una pieza, por lo que efectivamente el tablero empieza en el 2ndo row
        self._board = [[Board.NOT_USED, Board.NOT_USED, Board.NOT_USED, Board.FREE_SPACE],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4]]

        self._final_board = self._board
        self._free_space = Position(3, 0)

    # se encarga de cargar la configuracion de un archivo .txt, carga configuracion final e inicial (crear otra si es necesario)
    def loadConfig(self):
        return

    # se encarga de guardar la configuracion en un archivo de .txt
    def saveConfig(self):
        return

    # se encarga de revolver el tablero de juego
    def shuffle(self):
        initialRow=self._board[0]
        boardtemp= self._board
        boardtemp.pop(0)
        ran.shuffle(boardtemp)
        for sublist in boardtemp:
            ran.shuffle(sublist)

        boardtemp.insert(0,initialRow)
        self._board=boardtemp

        for i in range(Board.HEIGTH):
            for j in range(Board.WIDTH):
                if self._board[i][j]==0:
                    self._free_space=Position(j,i)
        print(self._free_space.row)
        print(self._free_space.col)
        return

    # se encarga de ejecutar A* para buscar la solución partiendo de _board y llegando a _final_board.
    # Debe guarda los pasos de solución de algún modo que pueda ser luego ejecutado
    def solvePuzzle(self):
        return

    def rotateRowRight(self, row):
        rotated_row = list(range(Board.WIDTH))
        for i in range(Board.WIDTH):
            next_index = i + 1
            if i == (Board.WIDTH - 1):
                next_index = 0
            rotated_row[next_index] = self._board[row][i]

        # mover puntero a espacio vacio
        if self._free_space.row == row:
            self._free_space.col += 1
            if self._free_space.col == Board.WIDTH:
                self._free_space.col = 0

        # hacer el cambio
        self._board[row] = rotated_row

    def rotateRowLeft(self, row):
        rotated_row = list(range(Board.WIDTH))
        for i in range(Board.WIDTH-1, -1, -1):
            next_index = i-1
            if i == 0:
                next_index = Board.WIDTH - 1
            rotated_row[next_index] = self._board[row][i]

        # mover puntero a espacio vacio
        if self._free_space.row == row:
            self._free_space.col -= 1
            if self._free_space.col < 0:
                self._free_space.col = Board.WIDTH - 1

        # hacer el cambio
        self._board[row] = rotated_row

    # se encarga de rotar los valores del _board en la fila(row) seleccionada por la cantidad en rotation, en la direccion (0=izq, 1=derecha)

    def rotateRow(self, row, direction, rotation=1):
        rotated_row = list(range(Board.WIDTH))
        # si se mueve a la izquierda
        if direction == BoardMoves.LEFT:

            for i in range(Board.WIDTH-1, -1, -1):
                next_index = i-1
                if i == 0:
                    next_index = Board.WIDTH - 1
                rotated_row[next_index] = self._board[row][i]

            # move free_space pointer
            if self._free_space.row == row:
                self._free_space.col -= 1
                if self._free_space.col < 0:
                    self._free_space.col = Board.WIDTH
        # si se mueve a la derecha
        elif direction == BoardMoves.RIGHT:

            for i in range(Board.WIDTH):
                next_index = i + 1
                if i == (Board.WIDTH - 1):
                    next_index = 0
                rotated_row[next_index] = self._board[row][i]

            # move free_space pointer
            if self._free_space.row == row:
                self._free_space.col += 1
                if self._free_space.col == Board.WIDTH:
                    self._free_space.col = 0
        else:
            print("Error, no indicó dirección derecha o izquierda")
            return

        # hacer el cambio
        self._board[row] = rotated_row
        return

    # mueve la posición vacía al lugar indicado si esta se encuentra en ese row o esa col
    def moveFreeSpace(self, row, col):
        if self._free_space.col == col and self._free_space.row == row:
            print("Se esta intentando mover el espacio vacio al mismo lugar que ya está")
            return
        if self._board[row][col] == Board.NOT_USED:
            print("No se puede mover el espacio vacio a un lugar no utilizado")
            return

        # si el lugar donde queremos movernos esta en la misma columna
        if self._free_space.col == col:
            diff = row - self._free_space.row
            # nos tenemos q mover hacia arriba
            if diff < 0:
                for i in range(-1*diff):
                    self.moveFreeSpaceUP()
            # nos movemos hacia abajo
            else:
                for i in range(diff):
                    self.moveFreeSpaceDown()

        # si el lugar donde queremos movernos esta en la misma fila
        elif self._free_space.row == row:
            diff = col - self._free_space.col
            # nos tenemos q mover hacia la izquierda
            if diff < 0:
                for i in range(-1*diff):
                    self.rotateRowLeft(row)
            # nos movemos hacia la derecha
            else:
                for i in range(diff):
                    self.rotateRowRight(row)
        else:
            print("el lugar indicado no comparte columna ni fila con el espacio vacio y por eso no se puede mover el espacio vacio ahi")

        return

    def moveFreeSpaceDown(self):
        if self._free_space.row + 1 > Board.HEIGTH:
            print("No se puede mover el espacio hacia abajo ya se llegó al limite")
            return
        self._board[self._free_space.row][self._free_space.col] = self._board[self._free_space.row +
                                                                              1][self._free_space.col]
        self._board[self._free_space.row + 1][self._free_space.col] = Board.FREE_SPACE
        self._free_space.row += 1

    def moveFreeSpaceUP(self):
        if self._free_space.row - 1 < 0:
            print("No se puede mover el espacio hacia arriba se llegó al limite")
            return
        if self._board[self._free_space.row - 1][self._free_space.col] == Board.NOT_USED:
            print(
                "No se puede mover el espacio hacia arriba con un espacio no usado en la casilla de arriba")
            return
        self._board[self._free_space.row][self._free_space.col] = self._board[self._free_space.row -
                                                                              1][self._free_space.col]
        self._board[self._free_space.row - 1][self._free_space.col] = Board.FREE_SPACE
        self._free_space.row -= 1

        # Se ejecutan los movimientos de la solución uno a uno (PROBABLEMENTE VA EN LA CLASE DE UI!!!)
    def playSolution(self):
        return

if __name__ == '__main__':
    game = Game()

    game.moveFreeSpaceDown()
    game.moveFreeSpaceDown()
    game.moveFreeSpaceDown()
    game.rotateRowLeft(0)
    game.rotateRowRight(1)
    # game.moveFreeSpace(4, 2)
    print(game._board)
    # game.rotateRow(0, 0)
    # print(game._board)
    # game.rotateRow(1, 0)
    # print(game._board)
    # game.rotateRow(2, 1)
    # print(game._board)
    # game.rotateRow(3, 0)
    # print(game._board)
    # game.rotateRow(4, 1)
    # a = list(range(0, 3))
    # print(a)
    # print(game._board)

    print("el espacio vacio esta en la columna ",
          game._free_space.col,  " y en la fila ", game._free_space.row)
