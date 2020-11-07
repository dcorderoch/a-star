from enum import IntEnum
from state import State
import copy

from queue import PriorityQueue as queue

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
    def __init__(self, *, value, parent, start = 0, goal = 0, free_space = Position(x=3,y=0)):
        super(StateBoard, self).__init__(value, parent, start, goal)
        self.free_space = free_space
        self.goal_row_sums, self.goal_col_sums = self.calculate_board_sums(board=self.goal)
        self.row_sums, self.col_sums = self.calculate_board_sums(board=self.value)
        self.get_distance()

    def __repr__(self):
        return f'BoardState({self.value})'

    def __eq__(self, other):
        if other == None:
            return False
        #print(f'StateBoard.__eq__(self, other), self.value:{self.value}, other.value:{other.value}')
        return self.value == other.value

    def __str__(self):
        return f'BoardState({self.value})'

    def calculate_board_sums(self, *, board):
        rows = [0 for _ in board]
        cols = [0 for _ in board[0]]
        for x in range(len(board)):
            for y in range(len(board[0])):
                rows[x] += board[x][y]
                cols[y] += board[x][y]
        return rows, cols

    def get_distance(self):
        if self.distance != 0:
            return self.distance # it has already been calculated
        distance = 0
        zeros = 0
        for i in range(len(self.row_sums)):
            partial = abs(self.row_sums[i] - self.goal_row_sums[i])
            if partial == 0:
                zeros += 1
            distance += (1 + 5 * zeros) * partial

        if self.parent:
            distance += self.parent.get_distance()

        self.distance = distance
        return distance

    def create_children(self):
        if self.children != []:
            return
        for row in range(Board.H):
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
            tmp = self.move_free_space_up(steps)
            if tmp != None:
                self.children.append(tmp)
        for steps in range(Board.H):
            tmp = self.move_free_space_down(steps)
            if tmp != None:
                self.children.append(tmp)
        return self.children

    def rotate_row_right(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W):
            j = 0 if i == Board.W - 1 else i + 1
            rotated_row[j] = self.value[row][i]
        newvalue = copy.deepcopy(self.value) # deep copy of the current value
        newvalue[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col + 1 * (row == self.free_space.col)
        if x == Board.W:
            x = 0
        new_p = Position(x=x, y=y)
        return StateBoard(value=newvalue, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def rotate_row_left(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W - 1, -1, -1):
            j = Board.W - 1 if i == 0 else i - 1
            rotated_row[j] = self.value[row][i]
        newvalue = copy.deepcopy(self.value) # deep copy of the current value
        newvalue[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col - 1 * (row == self.free_space.col)
        if x < 0:
            x = Board.W - 1
        new_p = Position(x=x, y=y)
        return StateBoard(value=newvalue, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def move_free_space_up(self, steps):
        row = self.free_space.row
        col = self.free_space.col
        if row == 0 or row - steps <= 0:
            return None
        if self.value[row - 1][col] == -1:
            return None
        if self.value[row - steps][col] == -1:
            return None
        row = self.free_space.row
        col = self.free_space.col
        nboard = copy.deepcopy(self.value)
        for i in range(steps):
            tmp = nboard[row - i][col]
            if nboard[row - i - 1][col] == -1:
                return None
            nboard[row - i][col] = nboard[row - i - 1][col]
            nboard[row - i - 1][col] = tmp
        y = row
        x = col
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def move_free_space_down(self, steps):
        row = self.free_space.row
        col = self.free_space.col
        if row + 1 == Board.H:
            return None
        if row + steps >= Board.H:
            return None
        if self.value[row][col] == -1:
            return None
        nboard = copy.deepcopy(self.value)
        for i in range(steps):
            tmp = nboard[row+i][col]
            nboard[row+i][col] = nboard[row+i+1][col]
            nboard[row+i+1][col] = tmp
        y = row
        x = col
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

def get_state_distance(state):
    return state.distance

class BoardSolver:
    def __init__(self, start, goal):
        self.path = []
        self.open_set = []
        self.visited_queue = []
        self.queue = queue()
        self.start = start
        self.goal = goal
        self.free_space = Position(x = 3, y = 0)

    def solve(self):
        self.open_set = []
        self.closed_set = []

        start_state = StateBoard(value=self.start, parent=None, start=self.start, goal=self.goal)

        self.open_set.append(start_state)

        while len(self.open_set) > 0:
            current = self.open_set[0]
            print(f'current: {current}, {current.distance}')
            self.open_set.remove(current)
            self.closed_set.append(current)

            if current.value == self.goal:
                self.path = current.path
                break

            current.create_children()
            children = current.children

            for child in children:
                if child in self.closed_set:
                    continue
                if child in self.open_set:
                    continue
                self.open_set.append(child)
            self.open_set.sort(key=get_state_distance)
        if not self.path:
            print('is not possible?')
