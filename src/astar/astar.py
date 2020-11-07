from StringSolver import StringSolver
from board import BoardSolver

def main():
    print('print string A*')
    start = 'eham'
    goal = 'mahe'
    a = StringSolver(start, goal)
    a.solve()
    for i, s in enumerate(a.path):
        print(f'{i}) {s}')
    # very simple case
    print('print Board A*')
    start = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    goal =  [[-1, -1, -1, 4], [1, 2, 3, 4], [3, 0, 1, 2], [4, 1, 2, 3], [3, 4, 1, 2]]
    print(f'new start: {start}')
    print(f'new goal: {goal}')
    b = BoardSolver(start, goal)
    b.solve()
    print(f'the path is:{b.path}')
    for i, s in enumerate(b.path):
        for row in s:
            print(f'step:{i}) {row}')

if __name__ == "__main__":
    main()
