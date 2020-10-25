from solver import *

if __name__ == '__main__':
    start = 'hema'
    goal = 'mahe'
    print('starting')
    a = solver(start, goal)
    a.solve()
    for i in range(len(a.path)):
        print(f'{i}) {a.path[i]}')
