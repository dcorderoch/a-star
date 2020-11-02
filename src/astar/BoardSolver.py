from queue import SimpleQueue as queue
from state_board import StateBoard, Position

class BoardSolver:
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.queue = queue()
        self.start = start
        self.goal = goal
        self.free_space = Position(x = 3, y = 0)
    def solve(self):
        start_state = StateBoard(self.start, 0, self.start, self.goal)
        count = 0
        self.queue.put((0, count, start_state))
        while not self.path and self.queue.qsize():
            closest_children = self.queue.get()[2]
            closest_children.create_children()
            self.visited_queue.append(closest_children.value)
            for child in closest_children.children:
                if child.value not in self.visited_queue:
                    cound += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.queue.put((child.dist, cound, child))
        if not self.path:
            print('goal is not possible', self.goal )
