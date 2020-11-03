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
    goal = [[-1, -1, -1, 0], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [2, 3, 4, 1]]
    print(f'new start: {start}')
    print(f'new goal: {goal}')
    b = BoardSolver(start, goal)
    b.solve()
    for i, s in enumerate(b.path):
        print(f'{i}) {s}')

if __name__ == "__main__":
    main()
