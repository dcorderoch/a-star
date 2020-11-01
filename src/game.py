from enum import Enum


class BoardTokens(Enum):
    NOT_USED = -1
    FREE_SPACE = 0
    TOKEN1 = 1
    TOKEN2 = 2
    TOKEN3 = 3
    TOKEN4 = 4


class Game:
    # el primer row del tablero solo puede contener una pieza, por lo que efectivamente el tablero empieza en el 2ndo row
    _board = [[BoardTokens.NOT_USED, BoardTokens.NOT_USED, BoardTokens.NOT_USED, BoardTokens.FREE_SPACE],
              [BoardTokens.TOKEN1, BoardTokens.TOKEN2,
               BoardTokens.TOKEN3, BoardTokens.TOKEN4],
              [BoardTokens.TOKEN1, BoardTokens.TOKEN2,
               BoardTokens.TOKEN3, BoardTokens.TOKEN4],
              [BoardTokens.TOKEN1, BoardTokens.TOKEN2,
               BoardTokens.TOKEN3, BoardTokens.TOKEN4],
              [BoardTokens.TOKEN1, BoardTokens.TOKEN2, BoardTokens.TOKEN3, BoardTokens.TOKEN4]]
    _final_board = _board

    redBackground = "rgb(255, 103, 103)"
    greenBackground = "rgb(0, 170, 127)"
    blueBackground = "rgb(88, 155, 255)"
    yellowBackground = "rgb(255, 255, 127)"

    # se encarga de cargar la configuración de un archivo .txt, carga configuración final e inicial (crear otra si es necesario)
    def loadConfig(self, config, ui):
        row = 0
        if self.validate_configuration(config) == False:
            print("Error: There are not the required number of colors in the suplied configuration. There must be exactly 4 occurrences of each color")
            return

        for line in config:
            if row >= 4:
                print("Warning: There are more rows than needed, skipping...")
                break

            trimedLine = line.replace('\n', '')
            trimedLine = trimedLine.replace(' ', '')

            elements = trimedLine.split(',')
            column = 0
            for element in elements:
                if column >= 4:
                    print("Warning: There are more columns than needed, skipping...")
                    break
                if not element.isdigit() or 0 <= int(element) >= 4:
                    print("Error: Invalid value: \"" + element +
                          "\". Cannot load configuration.")
                    self.reset_colors(ui)
                    return
                button = ui.layout[row][column]
                button.setStyleSheet(self.getColor(element))
                column += 1
            row += 1

    def reset_colors(self, ui):
        for column in range(0, 4):
            for row in range(0, 4):
                button = ui.layout[row][column]
                button.setStyleSheet(self.getColor(str(column)))

    def validate_configuration(self, configuration):
        singleConfig = ','.join(configuration)
        if singleConfig.count("0") != 4:
            return False
        if singleConfig.count("1") != 4:
            return False
        if singleConfig.count("2") != 4:
            return False
        if singleConfig.count("3") != 4:
            return False
        return True

    def getColor(self, colorCode):
        if colorCode == "0":
            return u"background-color: " + self.redBackground + ";"
        elif colorCode == "1":
            return u"background-color: " + self.greenBackground + ";"
        elif colorCode == "2":
            return u"background-color: " + self.blueBackground + ";"
        elif colorCode == "3":
            return u"background-color: " + self.yellowBackground + ";"
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

    # se encarga de rotar los valores del _board en la fila(row) seleccionada por la cantidad en rotation, en la direccion (0=izq, 1=derecha)
    def rotateRow(self, row, direction, rotation=1):
        return

    # mueve la posición vacía al lugar indicado si esta se encuentra en ese row o esa col
    def moveEmptySpace(self, row, col):
        return

    # Se ejecutan los movimientos de la solución uno a uno (PROBABLEMENTE VA EN LA CLASE DE UI!!!)
    def playSolution(self):
        return
