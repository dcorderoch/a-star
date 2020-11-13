"""
this is an implementation of the A-star algorithm's state for a board of the whip-it game
"""

import itertools

from queue import PriorityQueue
from enum import IntEnum

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from state import State

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
        self.distance = (parent.g() + 1 if parent else 0, self.h())
        self.free_space = (free_space[0], free_space[1])
        self.make_vertical = True

    def __repr__(self):
        return f'BoardState({self.value})'

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.f() < other.f()

    def __le__(self, other):
        return self.f() <= other.f()

    def __gt__(self, other):
        return self.f() > other.f()

    def __ge__(self, other):
        return self.f() >= other.f()

    def __str__(self):
        return f'BoardState({self.value})'

    def calculate_board_sums(self):
        """
        calculate board sums for a specific board
        """
        board = self.value
        goal = self.goal
        rows = [0 for _ in board]
        cols = [0 for _ in board[0]]
        grows = [0 for _ in goal]
        gcols = [0 for _ in goal[0]]
        for i, j in itertools.product(range(Board.H), range(Board.W)):
            rows[i] += board[i][j]
            cols[j] += board[i][j]
            grows[i] += goal[i][j]
            gcols[j] += goal[i][j]
        return rows, cols, grows, gcols

    def g(self):
        """
        return this instance's g distance
        """
        return self.distance[0]

    def manhattan_distance(self):
        """
        calculate sum of manhattan distance of all positions of this board and the goal
        """
        values = {-1: (), 0: (), 1: (), 2: (), 3: (), 4: ()}
        goalvs = {-1: (), 0: (), 1: (), 2: (), 3: (), 4: ()}

        for i, j in itertools.product(range(Board.H), range(Board.W)):
            value = self.value[i][j]
            goal = self.goal[i][j]
            point = (i, j)
            values[value] = (*values[value], point)
            goalvs[goal] = (*goalvs[goal], point)

        manhattan = 0
        for key in values:
            vlist = values[key]
            glist = goalvs[key]
            tmp = 0
            for i, j in itertools.product(range(len(vlist)), repeat=2):
                tmp += abs(vlist[j][0] - glist[i][0])
                tmp += abs(vlist[j][1] - glist[i][1])
            manhattan += tmp
        return manhattan >> 2

    def get_number_of_different_rows(self, vrows, grows):
        """
        calculate the number of rows that don't have the same sum
        """
        rows_diff = Board.H
        for i, row_sum in enumerate(vrows):
            diff = abs(row_sum - grows[i])
            if diff == 0:
                rows_diff -= 1
        return rows_diff

    def get_number_of_different_cols(self, vcols, gcols):
        """
        calculate the number of columns that don't have the same sum
        """
        cols_diff = Board.W
        for i, col_sum in enumerate(vcols):
            diff = abs(col_sum - gcols[i])
            if diff == 0:
                cols_diff -= 1
        return cols_diff

    def h(self):
        """
        return this instance's h heuristic distance
        """
        manhattan = self.manhattan_distance()

        vrows, vcols, grows, gcols = self.calculate_board_sums()

        rows_diff = self.get_number_of_different_rows(vrows, grows)

        cols_diff = self.get_number_of_different_cols(vcols, gcols)

        pos_diff = Board.H * Board.W
        for i, row in enumerate(self.value):
            for j, cell in enumerate(row):
                pos_diff -= 1 * (cell == self.goal[i][j])

        return manhattan + rows_diff + cols_diff + pos_diff

    def f(self):
        """
        return g + h
        """
        return self.distance[0] + self.distance[1] # self.g() + self.h()

    def create_children(self, closed_set):
        """
        create this board's children by one (valid) move
        """
        for row in range(Board.H):
            # insert child made by rotating a row to the right
            tmp = self.rotate_row_right(row)
            if tmp not in closed_set:
                self.children = (*self.children, tmp)
            # insert child made by rotating a row to the left
            tmp = self.rotate_row_left(row)
            if tmp not in closed_set:
                self.children = (*self.children, tmp)

        for steps in range(Board.H):
            if self.free_space[0] == 0:
                break
            row = self.free_space[0]
            col = self.free_space[1]
            if row == 0 or row - steps < 0 or self.value[row - steps][col] == -1:
                continue
            # insert child made by moving the free space up
            tmp = self.move_free_space_up(steps)
            if tmp not in closed_set:
                self.children = (*self.children, tmp)
        for steps in range(Board.H):
            if self.free_space[0] == Board.H - 1:
                break
            row = self.free_space[0]
            col = self.free_space[1]
            if row == Board.H - 1 or row + steps >= Board.H:
                continue
            # insert child made by moving the free space down
            tmp = self.move_free_space_down(steps)
            if tmp not in closed_set:
                self.children = (*self.children, tmp)

    def rotate_row_right(self, row):
        """
        generate child with row rotated to the right
        """
        nboard = self.value
        vrow = nboard[row]
        rotated_row = vrow[-1:] + vrow[0:-1]
        nboard = (*nboard[:row], rotated_row, *nboard[row+1:])
        col = self.free_space[1] + 1 * (self.free_space[0] == row)
        if col >= Board.W:
            col = 0
        row = self.free_space[0]
        return StateBoard(value=nboard,
                          parent=self,
                          start=self.start,
                          goal=self.goal,
                          free_space=(row, col))

    def rotate_row_left(self, row):
        """
        generate child with row rotated to the left
        """
        nboard = self.value
        vrow = nboard[row]
        rotated_row = vrow[1:] + vrow[0:1]
        nboard = (*nboard[:row], rotated_row, *nboard[row+1:])
        col = self.free_space[1] - 1 * (self.free_space[0] == row)
        if col < 0:
            col = Board.W - 1
        row = self.free_space[0]
        return StateBoard(value=nboard,
                          parent=self,
                          start=self.start,
                          goal=self.goal,
                          free_space=(row, col))

    def move_free_space_down(self, steps):
        """
        generate child with column rotated down
        """
        row = self.free_space[0]
        col = self.free_space[1]
        nboard = [list(x) for x in self.value]
        for i in range(steps):
            tmp = nboard[row+i+1][col]
            nboard[row+i+1][col] = nboard[row+i][col]
            nboard[row+i][col] = tmp
        nboard = tuple(tuple(x) for x in nboard)
        row += steps
        return StateBoard(value=nboard,
                          parent=self,
                          start=self.start,
                          goal=self.goal,
                          free_space=(row, col))

    def move_free_space_up(self, steps):
        """
        generate child with column rotated up
        """
        row = self.free_space[0]
        col = self.free_space[1]
        nboard = [list(x) for x in self.value]
        for i in range(steps):
            tmp = nboard[row - i][col]
            nboard[row - i][col] = nboard[row - i - 1][col]
            nboard[row - i - 1][col] = tmp
        nboard = tuple(tuple(x) for x in nboard)
        row -= steps
        return StateBoard(value=nboard,
                          parent=self,
                          start=self.start,
                          goal=self.goal,
                          free_space=(row, col))

class BoardSolver:
    """
    class to solve the A-star algorithm in board states
    """
    def __init__(self, *, start, goal):
        self.path = []
        self.start = start
        self.goal = goal
        self.free_space = (self.get_initial_position())
        self.open_set = PriorityQueue()
        self.closed_set = ()

    def get_initial_position(self):
        """
        get the initial y, x position of the free space
        """
        initial_y, initial_x = 0, 0
        for i, j in itertools.product(range(Board.H), range(Board.W)):
            if self.start[i][j] == 0:
                initial_y, initial_x = i, j
                break
        return initial_y, initial_x

    def solve(self):
        """
        run the A-star algorithm over the board states
        """
        start_state = StateBoard(value=self.start,
                                 parent=None,
                                 free_space=self.free_space,
                                 start=self.start,
                                 goal=self.goal)

        self.open_set.put((start_state.f(), start_state.g(), start_state))

        #i = 0
        while not self.open_set.empty():
            curr = self.open_set.get()[2]
            #if i % 0x80 == 0:
                #print(f'curr: {curr}, f:{curr.f():04d}, g:{curr.g():03d}, h:{curr.h():03d}')
            self.closed_set = (*self.closed_set, curr)

            curr.create_children(self.closed_set)
            children = curr.children

            for child in children:
                if child.value == self.goal:
                    self.path = child.path
                    return  # this here, it's extremely important
                self.open_set.put((child.f(), child.g(), child))
                #i += 1

        if not self.path:
            print('is not possible?')
