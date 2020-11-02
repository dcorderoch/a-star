from enum import Enum
import json
from PySide2.QtWidgets import QFileDialog


class Board():
    NOT_USED = -1
    FREE_SPACE = 0
    TOKEN1 = 1  # rojo
    TOKEN2 = 2  # verde
    TOKEN3 = 3  # azul
    TOKEN4 = 4  # amarillo
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
        self.reset_board()

        self._final_board = self._board
        self._free_space = Position(3, 0)

    RED = "0"
    GREEN = "1"
    BLUE = "2"
    YELLOW = "3"

    def loadFile(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        if path != '':
            print('file:', path)
            with open(path, "r") as config:
                json_file = json.load(config)
                self.loadConfig(json_file['init'])

    # se encarga de cargar la configuración de un archivo .txt, carga configuración final e inicial (crear otra si es necesario)
    def loadConfig(self, config):
        if self.validate_configuration(config) == False:
            return

        row = 0
        for line in config:
            column = 0

            for element in line:
                self.set_color(row, column, element)
                column += 1

            row += 1

    def reset_board(self):
        self._board = [[Board.NOT_USED, Board.NOT_USED, Board.NOT_USED, Board.FREE_SPACE],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4],
                       [Board.TOKEN1, Board.TOKEN2, Board.TOKEN3, Board.TOKEN4]]

    def validate_configuration(self, configuration):
        counter = {self.RED: 0, self.GREEN: 0, self.BLUE: 0, self.YELLOW: 0}
        if len(configuration) == 4:
            for row in configuration:
                if len(row) != 4:
                    print("Error: There are not 4 elements in a row")
                    return False
                else:
                    for column in row:
                        if isinstance(column, int):
                            if column == 0:
                                counter[self.RED] += 1
                            elif column == 1:
                                counter[self.GREEN] += 1
                            elif column == 2:
                                counter[self.BLUE] += 1
                            elif column == 3:
                                counter[self.YELLOW] += 1
                            else:
                                print("Error: Invalid value, found: " + str(column))
                                return False
                        else:
                            print("Error: Invalid value, found: " + str(column))
                            return False

            if counter["0"] != 4 or counter["1"] != 4 or counter["1"] != 4 or counter["1"] != 4:
                print("Error: There are not the required number of colors in the suplied configuration. There must be exactly 4 occurrences of each color")
                return False

            return True
        else:
            print("Error: There are not 4 rows")
            return False

    def set_color(self, row, column, colorCode):
        if str(colorCode) == self.RED:
            self._board[row+1][column] = Board.TOKEN1

        elif str(colorCode) == self.GREEN:
            self._board[row+1][column] = Board.TOKEN2

        elif str(colorCode) == self.BLUE:
            self._board[row+1][column] = Board.TOKEN3

        elif str(colorCode) == self.YELLOW:
            self._board[row+1][column] = Board.TOKEN4

    # se encarga de guardar la configuración en un archivo de .txt
    def saveConfig(self):
        return

    # se encarga de revolver el tablero de juego
    def shuffle(self):
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
            if(self._free_space.col + 1 == Board.WIDTH):
                self._free_space.col = 0
            else:
                self._free_space.col = self._free_space.col + 1

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
            if(self._free_space.col == 0):
                self._free_space.col = Board.WIDTH - 1
            else:
                self._free_space.col = self._free_space.col - 1

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
                if(self._free_space.col - 1 < 0):
                    self._free_space.col = Board.WIDTH
                else:
                    self._free_space.col = self._free_space.col - 1
        # si se mueve a la derecha
        elif direction == BoardMoves.RIGHT:

            for i in range(Board.WIDTH):
                next_index = i + 1
                if i == (Board.WIDTH - 1):
                    next_index = 0
                rotated_row[next_index] = self._board[row][i]

            # move free_space pointer
            if self._free_space.row == row:
                if(self._free_space.col + 1 == Board.WIDTH):
                    self._free_space.col = 0
                else:
                    self._free_space.col = self._free_space.col + 1
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
        self._board[self._free_space.row +
                    1][self._free_space.col] = Board.FREE_SPACE
        self._free_space.row = self._free_space.row + 1

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
        self._board[self._free_space.row -
                    1][self._free_space.col] = Board.FREE_SPACE
        self._free_space.row = self._free_space.row - 1

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
