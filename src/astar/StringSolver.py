from queue import PriorityQueue as queue
from StateString import StateString

class StringSolver:
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.queue = queue()
        self.start = start
        self.goal = goal
    def solve(self):
        start_state = StateString(self.start, 0, self.start, self.goal)
        self.queue.put((0, start_state))
        while not self.path and self.queue.qsize():
            closest_children = self.queue.get()[2] # in call to put(), it's the third argument
            closest_children.create_children()
            self.visited_queue.append(closest_children.value)
            for child in closest_children.children:
                if child.value not in self.visited_queue:
                    if not child.distance:
                        self.path = child.path
                        break
                    self.queue.put((child.distance, child))
        if not self.path:
            print("Goal is not possible!" + self.goal )
