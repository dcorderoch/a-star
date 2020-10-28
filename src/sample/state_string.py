from state import *

class state_string(state):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(state_string, self).__init__(value, parent, start, goal)
        self.dist = self.get_distance()
    def get_distance(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist
    def create_children(self):
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.value[:i] + self.value[i+1] + self.value[i] + self.value[i+2:]
                child = state_string(val, self)
                self.children.append(child)
