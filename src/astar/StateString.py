from state import State

class StateString(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.distance = self.get_f()
    def __repr__(self):
        return f'StringState({self.value})'
    def __str__(self):
        return f'StringState({self.value})'
    def get_f(self):
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
                child = StateString(val, self)
                self.children.append(child)
