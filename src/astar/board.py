"""
this is an implementation of the A-star algorithm's state for a board of the whip-it game
"""

import copy
from queue import PriorityQueue
from enum import IntEnum
from collections import namedtuple

from state import State

class Position:
    def __init__(self, *, x, y):
        self.col = x
        self.row = y

Positiont = namedtuple('Position', ['y', 'x'])

Distancet = namedtuple('Distance', ['g', 'h'])

class Board(IntEnum):
    """
    this class is used for Enums, which are constants used in this program
    """
    WIDTH = 4
    HEIGHT = 5
    W = WIDTH
    H = HEIGHT

class StateBoard(State):
    """
    this class represents a board/state in the whip it game for the A-star algorithm
    """
    def __init__(self, *, value, parent, free_space, start=0, goal=0):
        super(StateBoard, self).__init__(value, parent, start, goal)
        self.free_space = free_space
        self.g = 0
        self.h = 0
        self.goal_row_sums, self.goal_col_sums = self.calculate_board_sums(
            board=self.goal)
        self.row_sums, self.col_sums = self.calculate_board_sums(
            board=self.value)
        self.make_vertical = True
        self.get_f()

    def __repr__(self):
        return f'BoardState({self.value})'

    def __eq__(self, other):
        return other is not None and (self.value == other.value)

    def __lt__(self, other):
        return self.get_f() < other.get_f()

    def __le__(self, other):
        return self.get_f() <= other.get_f()

    def __gt__(self, other):
        return self.get_f() > other.get_f()

    def __ge__(self, other):
        return self.get_f() >= other.get_f()

    def __str__(self):
        return f'BoardState({self.value})'

    def calculate_board_sums(self, *, board):
        """
        calculate board sums for a single board
        """
        rows = [0 for _ in board]
        cols = [0 for _ in board[0]]
        for x in range(len(board)):
            for y in range(len(board[0])):
                rows[x] += board[x][y]
                cols[y] += board[x][y]
        return rows, cols

    def calculate_all_board_sums(self):
        """
        calculate board sums for a all boards
        """
        vrows = (*(0 for _ in range(Board.H)),)
        vcols = (*(0 for _ in range(Board.W)),)
        grows = (*(0 for _ in range(Board.H)),)
        gcols = (*(0 for _ in range(Board.W)),)

        for y in range(Board.H):
            for x in range(Board.W):
                vrows = tuple(vrows[y] + self.value[y][x] if i == y else r for i, r in enumerate(vrows))
                vcols = tuple(vcols[x] + self.value[y][x] if j == x else c for j, c in enumerate(vcols))
                grows = tuple(grows[y] + self.value[y][x] if i == y else r for i, r in enumerate(grows))
                gcols = tuple(gcols[x] + self.value[y][x] if j == x else c for j, c in enumerate(gcols))
        return tuple(vrows, vcols, grows, gcols)

    def find_nearest(self, yi, xi):
        points = {}
        dist = 0
        look_for = self.value[yi][xi]
        for y, row in enumerate(self.goal):
            for x, cell in enumerate(row):
                if cell == look_for:
                    dist = (abs(y - yi) << 2) + abs(x - xi)
                    points[(y, x)] = dist
        for p in points:
            if p[1] < dist:
                dist = p[1]
        return dist

    def calc_h(self):
        averages = [0 for _ in range(4)]  # to keep the averages of each color
        curr_average = 0
        h = 0
        for y, row in enumerate(self.goal):
            for x, col_v in enumerate(row):
                curr_average = 0
                # check current matrix for distances
                for c_y, c_row in enumerate(self.value):
                    for c_x, c_col_v in enumerate(c_row):
                        if c_col_v == col_v:
                            # curr_average += abs(c_y-y)+abs(c_x-x)
                            temp_average = abs(c_y-y)+abs(c_x-x)
                            if temp_average < curr_average:
                                curr_average = temp_average
                # curr_average = curr_average >> 2 # divide by 4
                # we do col_v-1 because color values start at 1
                averages[col_v-1] += curr_average >> 2
                h += (curr_average // 4)

        # for i in range(4):
        #     h += averages[i]

        return h
    def get_h(self):
        if self.h != 0:
            return self.h # already calculated

        values = {-1: (), 0: (), 1: (), 2: (), 3: (), 4: ()}
        goalvs = {-1: (), 0: (), 1: (), 2: (), 3: (), 4: ()}

        for y in range(Board.H):
            for x in range(Board.W):
                value = self.value[y][x]
                goal = self.goal[y][x]
                point = (y,x)
                values[value] = (*values[value], point)
                goalvs[goal] = (*goalvs[goal], point)
        manhattan = 0
        for key in values:
            vlist = values[key]
            glist = goalvs[key]
            tmp = 0
            for i in range(len(vlist)):
                for j in range(len(vlist)):
                    tmp += abs(vlist[j][0] - glist[i][0])
                    tmp += abs(vlist[j][1] - glist[i][1])
            manhattan += tmp >> 2

        rows_diff = Board.H
        for i, rs in enumerate(self.row_sums):
            diff = abs(rs - self.goal_row_sums[i])
            if diff == 0:
                rows_diff -= 1

        cols_diff = Board.W
        for i, cs in enumerate(self.col_sums):
            diff = abs(cs - self.goal_col_sums[i])
            if diff == 0:
                cols_diff -= 1

        pos_diff = Board.H * Board.W
        for i, row in enumerate(self.value):
            for j, cell in enumerate(row):
                pos_diff -= 1 * (cell == self.goal[i][j])

        self.h = manhattan + rows_diff + cols_diff + pos_diff

        return self.h

    def get_g(self):
        if self.g != 0:
            return self.g
        if self.parent:
            self.g = 1 + self.parent.g
        return self.g

    def get_f(self):
        if self.distance != 0:
            return self.distance  # it has already been calculated

        self.distance = self.get_g() + self.get_h()

        return self.distance

    def create_children(self, closed_set):
        for row in range(Board.H):
            # insert child made by rotating a row to the right
            tmp = self.rotate_row_right(row)
            if tmp not in closed_set and tmp not in self.children:
                self.children = (*self.children, tmp)
                #self.children.append(tmp)
            # insert child made by rotating a row to the left
            tmp = self.rotate_row_left(row)
            if tmp not in closed_set and tmp not in self.children:
                #self.children.append(tmp)
                self.children = (*self.children, tmp)
        #for steps in range(Board.W):
        #    # insert child made by moving the free space to the left # this is NOT valid in the toy
        #    tmp = self.move_free_space_left(steps)
        #    if tmp != None:
        #        if tmp not in closed_set and tmp not in self.children:
        #            self.children.append(tmp)
        #    # insert child made by moving the free space to the right # this is NOT valid in the toy
        #    tmp = self.move_free_space_right(steps)
        #    if tmp != None:
        #        if tmp not in closed_set and tmp not in self.children:
        #            self.children.append(tmp)

        for steps in range(Board.H):
            if self.free_space.row == 0:
                break
            # insert child made by moving the free space up
            tmp = self.move_free_space_up(steps)
            if tmp != None:
                if tmp not in closed_set:
                    #self.children.append(tmp)
                    self.children = (*self.children, tmp)
        for steps in range(Board.H):
            if self.free_space.row == Board.H - 1:
                break
            # insert child made by moving the free space down
            tmp = self.move_free_space_down(steps)
            if tmp:
                if tmp not in closed_set:
                    #self.children.append(tmp)
                    self.children = (*self.children, tmp)

    def rotate_row_right(self, row):
        rotated_row = [0 for _ in range(Board.W)]
        for i in range(Board.W):
            j = 0 if i == Board.W - 1 else i + 1
            rotated_row[j] = self.value[row][i]
        nboard = copy.deepcopy(self.value)  # deep copy of the current value
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
        nboard = copy.deepcopy(self.value)  # deep copy of the current value
        nboard[row] = rotated_row
        y = self.free_space.row
        x = self.free_space.col - 1 * (self.free_space.row == row)
        if x < 0:
            x = Board.W - 1
        new_p = Position(x=x, y=y)
        return StateBoard(value=nboard, parent=self, start=self.start, goal=self.goal, free_space=new_p)

    def move_free_space_down(self, steps):
        row = self.free_space.row
        col = self.free_space.col
        if row == Board.H - 1 or row + steps >= Board.H:
            return None
        if row + steps >= Board.H:
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

def get_state_distance(state):
    return state.get_f()

def get_state_g(state):
    return state.g

def get_state_h(state):
    return state.h

class BoardSolver:
    def __init__(self, *, start, goal, x, y):
        self.path = []
        self.start = start
        self.goal = goal
        self.free_space = Position(x=x, y=y)

    def solve(self):
        self.open_set = PriorityQueue()
        self.closed_set = ()

        start_state = StateBoard(value=self.start, parent=None,
                                 free_space=self.free_space, start=self.start, goal=self.goal)

        self.open_set.put((start_state.get_f(), start_state.g, start_state))

        i = 0
        while not self.open_set.empty():
            curr = self.open_set.get()[2]
            if i % 0x80 == 0:
                print(f'curr: {curr}, f:{curr.get_f():04d}, g:{curr.g:03d}, h:{curr.h:03d}')
            self.closed_set = (*self.closed_set, curr)

            if curr.value == self.goal:
                self.path = curr.path
                break

            curr.create_children(self.closed_set)
            children = curr.children

            for child in children:
                if child.value == self.goal:
                    self.path = child.path
                    return  # this here, it's extremely important
                self.open_set.put((child.get_f(), child.g, child))
                i += 1

        if not self.path:
            print('is not possible?')
