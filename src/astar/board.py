from enum import IntEnum
from state import State
import copy

from queue import PriorityQueue as queue

class Position:
    def __init__(self, *, x, y):
        self.col = x
        self.row = y

class Board(IntEnum):
    WIDTH = 3
    HEIGHT = 4
    W = WIDTH
    H = HEIGHT

class StateBoard(State):
    def __init__(self, *, value, parent, free_space, start = 0, goal = 0):
        super(StateBoard, self).__init__(value, parent, start, goal)
        self.free_space = free_space
        self.g = 0
        self.h = 0
        self.goal_row_sums, self.goal_col_sums = self.calculate_board_sums(board=self.goal)
        self.row_sums, self.col_sums = self.calculate_board_sums(board=self.value)
        self.make_vertical = True
        self.get_distance()

    def __repr__(self):
        return f'BoardState({self.value})'

    def __eq__(self, other):
        if other == None:
            return False
        #print(f'StateBoard.__eq__(self, other), self.value:{self.value}, other.value:{other.value}')
        return self.value == other.value
    def __lt__(self, other):
        return self.get_distance() < other.get_distance()
    def __le__(self, other):
        return self.get_distance() <= other.get_distance()
    def __gt__(self, other):
        return self.get_distance() > other.get_distance()
    def __ge__(self, other):
        return self.get_distance() >= other.get_distance()

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

        if self.parent:
            self.g = 1 + self.parent.g
        distance += self.g

        partials = [0 for _ in self.row_sums]
        rzeros = 0
        for i, _ in enumerate(self.row_sums):
            p = abs(self.row_sums[i] - self.goal_row_sums[i])
            if p == 0:
                rzeros += 1

        #if rzeros == Board.H:
        #    self.make_vertical = False

        partials = [0 for _ in self.col_sums]
        czeros = 0
        for i, _ in enumerate(self.col_sums):
            p = abs(self.col_sums[i] - self.goal_row_sums[i])
            if p == 0:
                czeros += 1

        if czeros == Board.W:
            self.h = 1
        else:
            self.h = (Board.H - rzeros) + ((Board.W - czeros ) << 2)

        self.distance = distance + self.h
        return self.distance

    def create_children(self, closed_set):
        if self.children != []:
            return
        for row in range(Board.H):
            # insert child made by rotating a row to the right
            tmp = self.rotate_row_right(row)
            if tmp not in closed_set and tmp not in self.children:
                self.children.append(tmp)
            # insert child made by rotating a row to the left
            tmp = self.rotate_row_left(row)
            if tmp not in closed_set and tmp not in self.children:
                self.children.append(tmp)
        for steps in range(Board.W):
            tmp = self.move_free_space_left(steps)
            if tmp != None:
                if tmp not in closed_set and tmp not in self.children:
                    self.children.append(tmp)
            tmp = self.move_free_space_right(steps)
            if tmp != None:
                if tmp not in closed_set and tmp not in self.children:
                    self.children.append(tmp)

        if self.make_vertical:
            for steps in range(Board.H):
                tmp = self.move_free_space_up(steps)
                if tmp != None:
                    if tmp not in closed_set:
                        print('moved up')
                        print(tmp)
                        self.children.append(tmp)
                tmp = self.move_free_space_down(steps)
                if tmp != None:
                    if tmp not in closed_set:
                        self.children.append(tmp)
        for row in range(Board.H):
            child = self.rotate_row_left(row)
            if child != None:
                if child not in closed_set:
                    self.children.append(child)
            for step in range(Board.W):
                child = child.rotate_row_left(row)
                if child != None:
                    if child not in closed_set:
                        self.children.append(child)
        return self.children

    def rotate_row_right(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W):
            j = 0 if i == Board.W - 1 else i + 1
            rotated_row[j] = self.value[row][i]
        nboard = copy.deepcopy(self.value) # deep copy of the current value
        nboard[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col + 1 * (self.free_space.row == row)
        if x >= Board.W:
            x = 0
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def rotate_row_left(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W - 1, -1, -1):
            j = Board.W - 1 if i == 0 else i - 1
            rotated_row[j] = self.value[row][i]
        nboard = copy.deepcopy(self.value) # deep copy of the current value
        nboard[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col - 1 * (self.free_space.row == row)
        if x < 0:
            x = Board.W - 1
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def move_free_space_up(self, steps):
        row = self.free_space.row
        col = self.free_space.col
        if row == 0 or row - steps < 0:
            return None
        if self.value[row - 1][col] == -1:
            return None
        if self.value[row - steps][col] == -1:
            return None
        nboard = copy.deepcopy(self.value)
        for i in range(steps):
            tmp = nboard[row - i][col]
            if nboard[row - i - 1][col] == -1:
                return None
            nboard[row - i][col] = nboard[row - i - 1][col]
            nboard[row - i - 1][col] = tmp
        y = row - steps
        x = col
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def move_free_space_left(self, steps):
        row = self.free_space.row
        col = self.free_space.col
        if col - steps < 0:
            return None
        nboard = copy.deepcopy(self.value)
        for i in range(steps):
            tmp = nboard[row][col-i]
            nboard[row][col-i] = nboard[row][col-i-1]
            nboard[row][col-i-1] = tmp
        y = row
        x = col - steps
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def move_free_space_right(self, steps):
        row = self.free_space.row
        col = self.free_space.col
        if col + steps >= Board.W:
            return None
        nboard = copy.deepcopy(self.value)
        for i in range(steps):
            tmp = nboard[row][col+i]
            nboard[row][col+i] = nboard[row][col+i+1]
            nboard[row][col+i+1] = tmp
        y = row
        x = col + steps
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
            tmp = nboard[row+i+1][col]
            nboard[row+i+1][col] = nboard[row+i][col]
            nboard[row+i][col] = tmp
        y = row + steps
        x = col
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

def get_state_distance(state):
    return state.get_distance()

def get_state_g(state):
    return state.g

def get_state_h(state):
    return state.h

class BoardSolver:
    def __init__(self, *, start, goal, x, y):
        self.path = []
        self.open_set = []
        self.visited_queue = []
        self.queue = queue()
        self.start = start
        self.goal = goal
        self.free_space = Position(x = x, y = y)

    def solve(self):
        self.open_set = []
        self.closed_set = []

        start_state = StateBoard(value=self.start, parent=None, free_space=self.free_space, start=self.start, goal=self.goal)

        self.open_set.append(start_state)

        while len(self.open_set) > 0:
            current = self.open_set[0]
            print(f'current: {current}, f:{current.get_distance():05d}, g:{current.g:03d}, h:{current.h:03d}')
            self.open_set.remove(current)
            self.closed_set.append(current)

            if current.value == self.goal:
                self.path = current.path
                break

            current.create_children(self.closed_set)
            children = current.children

            for child in children:
                if child.value == self.goal:
                    self.path = child.path
                    return
                if child in self.closed_set:
                    continue
                if child in self.open_set:
                    continue
                self.open_set.append(child)
            self.open_set.sort()
            if(len(self.open_set)) < 10:
                print(f'openset:{self.open_set}')
        if not self.path:
            print('is not possible?')
