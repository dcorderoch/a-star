from enum import IntEnum
from state import State
import copy

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
        self.distance = self.get_distance()
        self.free_space = free_space
    def __repr__(self):
        return f'BoardState({self.value})'
    def __eq__(self, other):
        if other == None:
            return False
        print(f'StateBoard.__eq__(self, other), self.value:{self.value}, other.value:{other.value}')
        return self.value == other.value
    def __str__(self):
        return f'BoardState({self.value})'
    def get_distance(self): # still gotta fix this
        distance = 0
        print(f'StateBoard.get_distance()')
        print(f'self.value:{self.value}, self.goal:{self.goal}')
        print(f'self.value == self.goal is {self.value == self.goal}')
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
        print(f'self.distance:{self.distance}')
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
        print('rotate row:{row} to the right')
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
        child = StateBoard(value=newvalue, parent=self, start=self.start, goal=self.goal, free_space=new_p)
        return child
    def rotate_row_left(self, row):
        print('rotate row:{row} to the left')
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
        child = StateBoard(value=newvalue, parent=self, start=self.start, goal=self.goal, free_space=new_p)
        return child
    def create_board_w_space_up(self, board, row, col):
        newvalue = copy.deepcopy(board) # deep copy of the current value
        newvalue[row][col] = newvalue[row - 1][col]
        newvalue[row - 1][col] = 0
        return newvalue
    def create_board_w_space_down(self, board, row, col):
        print(f'the row is:{row}')
        print(f'the col is:{col}')
        newvalue = copy.deepcopy(board) # deep copy of the current value
        print(f'the board is:{newvalue}')
        newvalue[row][col] = newvalue[row + 1][col]
        newvalue[row + 1][col] = 0
        return newvalue
    def move_free_space_up(self, steps):
        print(f'up steps:{steps}, current position, x:{self.free_space.col}, y:{self.free_space.row}')
        if steps == 0:
            return None
        if self.free_space.row == 0:
            return None
        if self.free_space.row - steps < 1:
            return None
        if self.value[self.free_space.row - 1][self.free_space.col] == -1:
            return None
        if self.value[self.free_space.row - steps][self.free_space.col] == -1:
            return None
        row = self.free_space.row
        col = self.free_space.col
        newvalue = self.create_board_w_space_up(self.value, row, col)
        steps_left = steps - 1
        while steps_left > 0:
            newvalue = self.create_board_w_space_up(newvalue, row - 1, col)
            row -= 1
            steps_left -= 1
        y = row
        x = col
        new_p = Position(x=x, y=y)
        potential = StateBoard(value=newvalue, parent=self, start=self.start, goal=self.goal, free_space=new_p)
        total = 0
        for row in potential.value:
            for col in row:
                total += col
        if total != 4 * (1 + 2 + 3 + 4) - 3 * 1:
            return None
        return potential
    def move_free_space_down(self, steps):
        print(f'down steps:{steps}, current position, x:{self.free_space.col}, y:{self.free_space.row}')
        if steps == 0:
            return None
        if self.free_space.row == Board.H - 1:
            return None
        if self.free_space.row + steps >= Board.H - 1:
            return None
        row = self.free_space.row
        col = self.free_space.col
        newvalue = self.create_board_w_space_down(self.value, row, col)
        steps_left = steps - 1
        while steps_left > 0:
            newvalue = self.create_board_w_space_down(newvalue, row + 1, col)
            row += 1
            steps_left -= 1
        y = row
        x = col
        new_p = Position(x=x, y=y)
        potential = StateBoard(value=newvalue, parent=self, start=self.start, goal=self.goal, free_space=new_p)
        total = 0
        for row in potential.value:
            for col in row:
                total += col
        if total != 4 * (1 + 2 + 3 + 4) - 3 * 1:
            return None
        return potential

from queue import SimpleQueue as queue

def get_state_distance(state):
    return state.distance

class BoardSolver:
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.queue = queue()
        self.start = start
        self.goal = goal
        self.free_space = Position(x = 3, y = 0)
    def solve(self):
        print(f'BoardSolver.solve()')
        start_state = StateBoard(value=self.start, parent=None, start=self.start, goal=self.goal)
        print(f'start_state:{start_state}')
        count = 0
        self.queue.put((0, count, start_state))
        while not self.path and self.queue.qsize():
            closest_children = self.queue.get()[2]
            print(f'closest_children:{closest_children}')
            closest_children.create_children()
            for i, child in enumerate(closest_children.children):
                print(f'child No. {i+1}:{child}')
            #return
            closest_children.children.sort(key=get_state_distance)
            for i, child in enumerate(closest_children.children):
               print(f'child No. {i+1}:{child}')
            #return
            print(f'child is {closest_children.value}')
            self.visited_queue.append(closest_children.value)
            for child in closest_children.children:
                if child.value not in self.visited_queue:
                    self.visited_queue.append(child.value)
                    count += 1
                    if child.value == self.goal:
                        print('child == goal')
                        self.path = child.path
                        print('------------------------------------')
                        break
                    if child.distance == 0:
                        print('distance == 0')
                        print(f'current path:{self.path}, new path:{child.path}')
                        self.path = child.path
                        print('------------------------------------')
                        break
                    self.queue.put((child.distance, count, child))
            print('exited the for')
        if not self.path:
            print('goal is not possible', self.goal )
