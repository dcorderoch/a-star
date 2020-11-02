from state import State

class Position:
    def __init__(self, *, x, y):
        self.col = x
        self.row = y

class StateBoard(State):
    def __init__(self, value, parent, start = 0, goal = 0, free_space = Position(x=3,y=0)):
        super(StateBoard, self).__init__(value, parent, start, goal)
        self.distance = self.get_distance()
        self.free_space = free_space
    def get_distance(self):
        if self.value == self.goal:
            return 0
        distance = 0
        for i, letter in enumerate(self.goal):
            distance += abs(i - self.value.index(letter))
        return distance
    def create_children(self):
        if self.children == []:
            return
        for row in range(0, 4):
            # insert child made by rotating a row to the right
            tmp = self.rotate_row_right(row)
            self.children.append(tmp)
            # insert child made by rotating a row to the left
            tmp = self.rotate_row_left(row)
            self.children.append(tmp)
            # insert child made by moving free space to different row
            if row != self.free_space.row:
                tmp = self.move_free_space_row(row)
            # insert child made by moving free space to different col
            if col != self.free_space.col:
                tmp = self.move_free_space_row(col)
