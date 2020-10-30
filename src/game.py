

class BoardTokens(Enum):
    NOT_USED = -1
    FREE_SPACE = 0
    TOKEN1 = 1
    TOKEN2 = 2
    TOKEN3 = 3
    TOKEN4 = 4


class Game:
    # el primer row del tablero solo puede contener una pieza, por lo que efectivamente el tablero empieza en el 2ndo row
    self._board = [[BoardTokens.NOT_USED, BoardTokens.NOT_USED, BoardTokens.NOT_USED, BoardTokens.FREE_SPACE],
                   [BoardTokens.TOKEN1, BoardTokens.TOKEN2,
                       BoardTokens.TOKEN3, BoardTokens.TOKEN4],
                   [BoardTokens.TOKEN1, BoardTokens.TOKEN2,
                       BoardTokens.TOKEN3, BoardTokens.TOKEN4],
                   [BoardTokens.TOKEN1, BoardTokens.TOKEN2,
                       BoardTokens.TOKEN3, BoardTokens.TOKEN4],
                   [BoardTokens.TOKEN1, BoardTokens.TOKEN2, BoardTokens.TOKEN3, BoardTokens.TOKEN4]]
    self._final_board = self._board

    # se encarga de cargar la configuración de un archivo .txt, carga configuración final e inicial (crear otra si es necesario)
    def loadConfig():
        return

    # se encarga de guardar la configuración en un archivo de .txt
    def saveConfig():
        return

    # se encarga de revolver el tablero de juego
    def shuffle():
        return

    # se encarga de ejecutar A* para buscar la solución partiendo de _board y llegando a _final_board.
    # Debe guarda los pasos de solución de algún modo que pueda ser luego ejecutado
    def solvePuzzle():
        return

    # se encarga de rotar los valores del _board en la fila(row) seleccionada por la cantidad en rotation, en la direccion (0=izq, 1=derecha)
    def rotateRow(row, direction, rotation=1):
        return

    # mueve la posición vacía al lugar indicado si esta se encuentra en ese row o esa col
    def moveEmptySpace(row, col):
        return

    # Se ejecutan los movimientos de la solución uno a uno (PROBABLEMENTE VA EN LA CLASE DE UI!!!)
    def playSolution():
        return
