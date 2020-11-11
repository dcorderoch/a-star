from StringSolver import StringSolver
from board import BoardSolver

def main():
    # very simple case
    print('print Board A*')

    start = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

    # works
    goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    start = [[-1, -1, -1, 4], [3, 0, 1, 2], [3, 4, 2, 3], [1, 1, 1, 2], [4, 4, 2, 3]]

    # works (no change)
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

    # works (all single rotation)
    #goal = [[-1, -1, -1, 0], [4, 1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [4, 1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [4, 1, 2, 3], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [4, 1, 2, 3]]

    # works (double rotations)
    #goal = [[-1, -1, -1, 0], [3, 4, 1, 2], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [3, 4, 1, 2]]

    # works (space move)
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 0], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 0], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 0]]

    # works (space move, and rotation)
    #goal = [[-1, -1, -1, 4], [0, 1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [0, 1, 2, 3]]

    # works (space move, and rotation)
    #goal = [[-1, -1, -1, 4], [2, 3, 0, 1], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [2, 3, 0, 1], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [2, 3, 0, 1], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [2, 3, 0, 1]]

    # works (space move, double rotation)
    #goal = [[-1, -1, -1, 3], [4, 1, 2, 4], [1, 2, 3, 0], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 3], [1, 2, 3, 0], [4, 1, 2, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 3], [1, 2, 3, 0], [1, 2, 3, 4], [4, 1, 2, 4], [1, 2, 3, 4]]
    #goal = [[-1, -1, -1, 3], [1, 2, 3, 0], [1, 2, 3, 4], [1, 2, 3, 4], [4, 1, 2, 4]]

    # works (takes ~90s) (6 steps)
    #goal = [[-1, -1, -1, 2], [3, 4, 1, 4], [3, 2, 1, 2], [1, 2, 3, 4], [1, 0, 3, 4]]
    # works (7 steps)
    #goal = [[-1, -1, -1, 2], [3, 0, 1, 4], [3, 4, 1, 2], [1, 2, 3, 4], [4, 1, 2, 3]]

    # works (11 steps)
    #goal = [[-1, -1, -1, 4], [1, 2, 3, 4], [3, 0, 2, 3], [1, 1, 1, 2], [4, 4, 2, 3]]

    # works (14 steps)
    #goal = [[-1, -1, -1, 4], [3, 0, 1, 2], [3, 4, 2, 3], [1, 1, 1, 2], [4, 4, 2, 3]]

    # goal = [[-1, -1, -1, 0], [4, 4, 4, 4], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]

    print(f'new start: {start}')
    print(f'new goal: {goal}')
    for i, row in enumerate(start):
        for j, cell in enumerate(row):
            if cell == 0:
                y, x = i, j
                break
        else:
            continue
        break
    # x = start's free space's col, same for y
    b = BoardSolver(start=start, goal=goal, x=x, y=y)
    b.solve()
    print('the path is')
    for i, s in enumerate(b.path):
        for row in s:
            print(f'step:{i}) {row}')

if __name__ == "__main__":
    main()
