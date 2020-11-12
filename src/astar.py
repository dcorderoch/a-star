from game import *
from solution import *
import heapq
import numpy as np


class AStar():

    def __init__(self, start, end):
        self.visited = []
        self.possible = []
        self.actualCost = 0
        self.goal = end

        self.find_empty_pos(start)

        heapq.heappush(self.possible, Solution(
            start, end, self.emptyPos, [], 0, 0))

    def find_empty_pos(self, board):
        for row in range(0, len(board)):
            for column in range(0, len(board[0])):
                if board[row][column] == 0:
                    self.emptyPos = [row, column]
                    return

    def solve(self):
        iteration = 0
        while self.possible:
            current = heapq.heappop(self.possible)
            self.visited.append(np.array(current.get_board()))

            expanded = current.expand(self.visited)

            if expanded == []:
                # if self.actualCost == 0 or current.get_cost() < self.actualCost:
                # self.actualCost = current.get_cost()
                self.solution = current
                return self.solution
            else:
                for board in expanded:
                    if any(np.array_equal(np.array(board.get_board()), i) for i in self.visited):
                        continue

                    for possibleBoard in self.possible:
                        if possibleBoard.get_board() == board.get_board() and possibleBoard.get_g() < board.get_g():
                            continue

                    heapq.heappush(
                        self.possible, board)

            iteration += 1

        return self.solution
