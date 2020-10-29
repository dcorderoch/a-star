from solver import *

def main():
    start = [[3, 2], [1, 0]]
    goal = [[0, 2], [1, 3]]
    for m in goal:
        for e in m:
            print(e)
    for m in start:
        for e in m:
            print(e)
    #return

    start = 'hema'
    goal = 'mahe'
    print('starting')
    a = solver(start, goal)
    a.solve()
    for i in range(len(a.path)):
        print(f'{i}) {a.path[i]}')

if __name__ == '__main__':
    main()
