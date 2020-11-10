import copy


class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.distance = 0
        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = copy.deepcopy(parent.path)
            self.path.append(value)
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def __repr__(self):
        pass

    def __eq__(self, other):
        for y, row in enumerate(value):
            if row != other[y]:
                return False
        return True

    def __str__(self):
        pass

    def get_distance(self):
        pass

    def create_children(self):
        pass
