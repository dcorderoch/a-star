from StringSolver import StringSolver
from board import BoardSolver

def main():
    # very simple case
    print('print Board A*')

    #start = [[-1, -1, -1, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 0]]
    #goal  = [[-1, -1, -1, 4], [1, 2, 0, 4], [3, 2, 3, 4], [1, 1, 2, 3], [4, 1, 2, 3]]
    #goal =  [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

    # this works
    start = [[-1, -1, 3], [1, 2, 0], [1, 2, 3], [1, 2, 3]]
    goal =  [[-1, -1, 0], [3, 1, 2], [3, 1, 2], [3, 1, 2]]

    print(f'new start: {start}')
    print(f'new goal: {goal}')
    b = BoardSolver(start=start, goal=goal, x=2, y=1) # x = start's free space's col, same for y
    b.solve()
    print(f'the path is:{b.path}')
    for i, s in enumerate(b.path):
        for row in s:
            print(f'step:{i}) {row}')

if __name__ == "__main__":
    main()
