from enum import IntEnum
from state import State

class Position:
    def __init__(self, *, x, y):
        self.col = x
        self.row = y

class Board(IntEnum):
    WIDTH = 4
    HEIGHT = 5
    W = WIDTH
    H = HEIGHT

class StateBoard(State):
    def __init__(self, value, parent, start = 0, goal = 0, free_space = Position(x=3,y=0)):
        super(StateBoard, self).__init__(value, parent, start, goal)
        self.distance = self.get_distance()
        self.free_space = free_space
    def get_distance(self): # still gotta fix this
        distance = 0
        if self.value == self.goal:
            return distance
        if self.distance != 0:
            return distance
        for i, row in enumerate(self.value):
            for j, cell in enumerate(row):
                if cell == -1:
                    continue
                if cell == 0:
                    distance += 2 + i + j
                    continue
                distance += (abs(cell - j) - 1)
        if self.parent:
            distance += self.parent.get_distance()
        self.distance = distance
        return distance
    def create_children(self):
        if self.children == []:
            return
        for row in range(Board.W):
            if row == self.free_space.row:
                continue # only do for values other than the current state's row
            # insert child made by rotating a row to the right
            tmp = self.rotate_row_right(row)
            self.children.append(tmp)
            # insert child made by rotating a row to the left
            tmp = self.rotate_row_left(row)
            self.children.append(tmp)
            # insert child made by moving up once
        for steps in range(Board.H):
            if self.free_space.col - steps < 1:
                continue
            tmp = self.move_free_space_up(steps)
            if tmp != None:
                self.children.append(tmp)
        for steps in range(Board.H):
            if self.free_space.col + steps > Board.H:
                continue
            tmp = self.move_free_space_down(steps)
            if tmp != None:
                self.children.append(tmp)
    def rotate_row_right(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W):
            j = 0 if i == Board.W - 1 else i + 1
            rotated_row[j] = self.value[row][i]
        newvalue = self.value[:] # deep copy of the current value
        newvalue[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col + 1 * (col == self.free_space.col)
        new_p = Position(x, y)
        child = StateBoard(newvalue, self, start = self.start, goal = self.goal, free_space = new_p)
        return child
    def rotate_row_left(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W - 1, -1, -1):
            j = Board.W - 1 if i == 0 else i - 1
            rotated_row[j] = self.value[row][i]
        newvalue = self.value[:] # deep copy of the current value
        newvalue[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col - 1 * (col == self.free_space.col)
        new_p = Position(x, y)
        child = StateBoard(newvalue, self, start = self.start, goal = self.goal, free_space = new_p)
        return child
    def create_board_w_space_up(self, board, row, col):
        newvalue = board[:] # deep copy of the current value
        newvalue[row][col] = newvalue[row - 1][col]
        newvalue[row - 1][col] = 0
        return newvalue
    def move_free_space_up(self, steps):
        if self.free_space.col - steps < 1:
            return None
        if self.free_space.col == 0:
            return None
        if self.value[self.free_space.row - 1][self.free_space.col] == -1:
            return None
        newvalue = create_board_w_space_up(self.value, self.free_space.row, self.free_space.col)
        steps_left = steps - 1
        while steps_left > 0:
            newvalue = create_board_w_space_up(newvalue, self.free_space.row - 1, self.free_space.col)
            steps_left -= 1
        y = self.free_space.row - steps
        x = self.free_space.col
        new_p = Position(x, y)
        return StateBoard(newvalue, self, start = self.start, goal = self.goal, free_space = new_p)
    def move_free_space_down(self, steps):
        if self.free_space.col + steps > Board.H:
            return None
        if self.free_space.col == Board.H - 1:
            return None
        newvalue = create_board_w_space_down(self.value, self.free_space.row, self.free_space.col)
        steps_left = steps - 1
        while steps_left > 0:
            newvalue = create_board_w_space_down(newvalue, self.free_space.row + 1, self.free_space.col)
            steps_left -= 1
        y = self.free_space.row + steps
        x = self.free_space.col
        new_p = Position(x, y)
        return StateBoard(newvalue, self, start = self.start, goal = self.goal, free_space = new_p)
