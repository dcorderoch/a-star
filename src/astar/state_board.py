from state import State

class StateBoard(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(StateBoard, self).__init__(value, parent, start, goal)
        self.distance = self.get_distance()
    def get_distance(self):
        if self.value == self.goal:
            return 0
        distance = 0
        for i, letter in enumerate(self.goal):
            distance += abs(i - self.value.index(letter))
        return distance
    def create_children(self):
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.value[:i] + self.value[i+1] + self.value[i] + self.value[i+2:]
                child = StateBoard(val, self)
                self.children.append(child)
