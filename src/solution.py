import copy
from collections import deque


class Solution():
    def __init__(self, actual, goal, emptyPos, steps, g, h):
        self.actualBoard = actual
        self.goal = goal
        self.emptyPos = emptyPos
        self.steps = steps
        self.g = g
        self.h = h
        self.get_completion_percentage(self.actualBoard, self.goal)

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def expand(self, visited):
        if self.actualBoard[1:] == self.goal[1:]:
            return []

        result = []

        for row in range(0, len(self.actualBoard)):
            nextState = self.rotate(row, -1)
            result.append(nextState)

            nextState = self.rotate(row, 1)
            result.append(nextState)

        # if empty space is not at the bottom move down
        if self.emptyPos[0] < len(self.actualBoard) - 1:
            nextState = self.move_vertical(1)
            result.append(nextState)

        if self.emptyPos[0] > 0:  # if empty space is not at the top move up
            nextState = self.move_vertical(-1)
            result.append(nextState)

        return result

    def move_vertical(self, direction):  # -1 = up / 1 = down
        board = copy.deepcopy(self.actualBoard)
        row, column = self.emptyPos[0], self.emptyPos[1]

        board[row][column] = board[row+direction][column]
        board[row+direction][column] = 0

        newH = self.calculate_h(board)

        newEmptyPos = [row+direction, column]

        newSteps = copy.deepcopy(self.steps)
        if direction == -1:
            newSteps.append("u" + str(column))
        elif direction == 1:
            newSteps.append("d" + str(column))

        return Solution(board, self.goal, newEmptyPos, newSteps, self.g+1, newH)

    def rotate(self, row, direction):
        board = copy.deepcopy(self.actualBoard)

        temp_row = deque(board[row])
        temp_row.rotate(direction)
        board[row] = list(temp_row)

        if 0 in board[row]:
            newEmptyPos = [row, board[row].index(0)]
        else:
            newEmptyPos = self.emptyPos

        newH = self.calculate_h(board)

        newSteps = copy.deepcopy(self.steps)
        if direction == -1:
            newSteps.append("l" + str(row))
        elif direction == 1:
            newSteps.append("r" + str(row))

        return Solution(board, self.goal, newEmptyPos, newSteps, self.g+1, newH)

    def get_completion_percentage(self, board, goal):
        correct = 0
        for row in range(1, len(board)):
            for column in range(0, len(board[0])):
                if board[row][column] == goal[row][column]:
                    correct += 1

        self.percentage = abs(1-(correct/16))

    def calculate_h(self, board):
        tempGoal = copy.deepcopy(self.goal)
        tempGoal = self.disable_correct(board, tempGoal)
        h = 0

        for row in range(0, len(board)):
            for column in range(0, len(board[0])):
                if board[row][column] > 0:
                    color = board[row][column]

                    moves, tempGoal = self.find_manhattan_distance(
                        [row, column], board, tempGoal, color)

                    h += moves

        actualH = h * self.percentage
        return actualH

    def disable_correct(self, board, goal):
        for row in range(1, len(board)):
            for column in range(0, len(board[0])):
                if board[row][column] == goal[row][column]:
                    goal[row][column] = -1

        return goal

    def find_manhattan_distance(self, pos, board, goal, color):
        row = pos[0]
        column = pos[1]

        if board[row][column] != self.goal[row][column]:
            for row in range(0, len(goal)):
                for column in range(0, len(goal[0])):
                    if goal[row][column] == color:
                        if board[row][column] != color:
                            if (pos[1] == 0 and column == 3) or (pos[1] == 3 and column == 0):
                                moves = 1
                            else:
                                moves = abs(pos[1] - column)
                            if row == 0:
                                moves -= 1
                            else:
                                moves += abs(pos[0] - row)
                            goal[row][column] = -1

                            return moves, goal
        else:
            return 0, goal

    def get_cost(self):
        return self.g + self.h

    def get_board(self):
        return self.actualBoard

    def get_g(self):
        return self.g
