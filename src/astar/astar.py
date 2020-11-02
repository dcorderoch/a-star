from StringSolver import StringSolver
from BoardSolver import BoardSolver

def main():
    start = 'eham'
    goal = 'mahe'
    a = StringSolver(start, goal)
    a.solve()
    for i, s in enumerate(a.path):
        print(f'{i}) {s}')
    # very simple case
    print('now to print the board solution')
    start = [[-1, 1, 1, 1, 1], [-1, 2, 2, 2, 2], [-1, 3, 3, 3, 3], [4, 4, 4, 4, 0]]
    goal = [[-1, 1, 1, 1, 1], [-1, 2, 2, 2, 2], [-1, 3, 3, 3, 3], [0, 4, 4, 4, 4]]
    print(f'new start: {start}')
    print(f'new goal: {goal}')
    b = BoardSolver(start, goal)
    for i, s in enumerate(b.path):
        print(f'{i}) {s}')

if __name__ == '__main__':
    main()
