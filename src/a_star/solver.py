from queue import PriorityQueue as priority_queue
from state_string import *

class solver:
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.priority_queue = priority_queue()
        self.start = start
        self.goal = goal
    def solve(self):
        start_state = state_string(self.start, 0, self.start, self.goal)
        count = 0
        self.priority_queue.put((0, count, start_state))
        while not self.path and self.priority_queue.qsize():
            closest_children = self.priority_queue.get()[2] # check why 2
            closest_children.create_children()
            self.visited_queue.append(closest_children.value)
            for child in closest_children.children:
                if child.value not in self.visited_queue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priority_queue.put((child.dist, count, child))
        if not self.path:
            print("Goal is not possible!" + self.goal )
