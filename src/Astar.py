# -*- coding: utf-8 -*-
""" generic A-Star path searching algorithm """

from abc import ABCMeta, abstractmethod
from copy import deepcopy
from heapq import heappush, heappop, heapify

Infinite = float('inf')


class AStar:
    __metaclass__ = ABCMeta
    __slots__ = ()

    class SearchNode:
        __slots__ = ('data', 'gscore', 'fscore',
                     'closed', 'came_from', 'out_openset')

        def __init__(self, data, gscore=Infinite, fscore=Infinite):
            self.data = data
            self.gscore = gscore
            self.fscore = fscore
            self.closed = False
            self.out_openset = True
            self.came_from = None

        def __lt__(self, b):
            return self.fscore < b.fscore

    class SearchNodeDict(dict):

        def __missing__(self, k):
            v = AStar.SearchNode(k)
            self.__setitem__(k, v)
            return v

    def calc_h(self, current, goal):
        averages = [0 for _ in range(4)]  # to keep the averages of each color
        curr_average = 0
        h = 0
        # colors = {red:False,blue:False,yellow:False,}
        for y, row in enumerate(goal):
            for x, col_v in enumerate(row):
                if col_v == -1 or col_v == 0:
                    continue
                # if averages[int(col_v) - 1]:
                #     continue

                curr_average = 999
                color_match_count = 0
                # check current matrix for distances
                for c_y, c_row in enumerate(current):
                    for c_x, c_col_v in enumerate(c_row):
                        if c_col_v == col_v:
                            # curr_average += abs(c_y-y)+abs(c_x-x)
                            color_match_count += 1
                            temp_average = abs(c_y-y)+abs(c_x-x)
                            if temp_average < curr_average:
                                curr_average = temp_average
                        if color_match_count == 4:
                            break
                    if color_match_count == 4:
                        break
                # curr_average = curr_average >> 2 # divide by 4
                # we do col_v-1 because color values start at 1
                averages[int(col_v)-1] += curr_average
                # h += (curr_average / 4)
        for val in averages:
            h += val/4
        return h

    def heuristic_cost_estimate(self, current, goal):
        """Computes the estimated (rough) distance between a node and the goal, this method must be implemented in a subclass. The second parameter is always the goal."""
        # return self.distance_between(current, goal)
        return self.calc_h(current, goal)

    def distance_between(self, n1, n2):
        """Gives the real distance between two adjacent nodes n1 and n2 (i.e n2 belongs to the list of n1's neighbors).
           n2 is guaranteed to belong to the list returned by the call to neighbors(n1).
           This method must be implemented in a subclass."""
        distance = 0
        for i in range(len(n1)):
            for j in range(len(n1[0])):
                if n1[i][j] == n2[i][j]:
                    distance += 1
        return distance

    def move_ws_up(self, node, ws_pos):
        if ws_pos[0]-1 < 0:
            print("no se puede mover para arriba")
            return node
        board = [list(item) for item in node]
        board[ws_pos[0]][ws_pos[1]], board[ws_pos[0]-1][ws_pos[1]
                                                        ] = board[ws_pos[0]-1][ws_pos[1]], board[ws_pos[0]][ws_pos[1]]
        return tuple(tuple(item) for item in board)

    def move_ws_down(self, node, ws_pos):
        if ws_pos[0]+1 > len(node[0]):
            print("no se puede mover para abajo")
            return node
        board = [list(item) for item in node]
        board[ws_pos[0]][ws_pos[1]], board[ws_pos[0]+1][ws_pos[1]
                                                        ] = board[ws_pos[0]+1][ws_pos[1]], board[ws_pos[0]][ws_pos[1]]
        return tuple(tuple(item) for item in board)

    def left_shift(self, tup, n):
        length = len(tup)
        if length != 0:
            n = n % length
        else:
            return tuple()
        return tup[n:] + tup[0:n]

    def right_shift(self, tup, n):
        length = len(tup)
        if length != 0:
            n = n % length
        else:
            return tuple()
        return tup[-n:] + tup[0:-n]

    def neighbors(self, node):
        """For a given node, returns (or yields) the list of its neighbors. this method must be implemented in a subclass"""
        res = []
        l0 = (self.left_shift(node[0], 1),)+node[1:]

        r0 = (self.right_shift(node[0], 1),)+node[1:]

        l1 = node[:1]+(self.left_shift(node[1], 1),)+node[2:]

        r1 = node[:1]+(self.right_shift(node[1], 1),)+node[2:]

        l2 = node[:2] + (self.left_shift(node[2], 1),)+node[3:]

        r2 = node[:2] + (self.right_shift(node[2], 1),)+node[3:]

        l3 = node[:3] + (self.left_shift(node[3], 1),)+node[4:]

        r3 = node[:3] + (self.right_shift(node[3], 1),)+node[4:]

        l4 = node[:4] + (self.left_shift(node[4], 1),)

        r4 = node[:4] + (self.right_shift(node[4], 1),)

        c1 = node[:][1:]

        # look for the empty space
        for y, row in enumerate(node):
            for x, data in enumerate(row):
                if data == 0:
                    ws_pos = (y, x)
                    break
            if data == 0:
                break

        if ws_pos[0] != 0:
            if node[ws_pos[0]][ws_pos[1]] != -1:
                mu = self.move_ws_up(node, ws_pos)
                res.append(mu)
        if ws_pos[0] != 4:
            md = self.move_ws_down(node, ws_pos)
            res.append(md)

        res.append(tuple(l1))
        res.append(tuple(r1))
        res.append(tuple(l2))
        res.append(tuple(r2))
        res.append(tuple(l3))
        res.append(tuple(r3))
        res.append(tuple(l4))
        res.append(tuple(r4))
        res.append(tuple(l0))
        res.append(tuple(r0))

        matrix_dim = len(node[0])

        #
        # if int(item_index / matrix_dim) < 4:
        #     up = deepcopy(node)
        #     removed = up[int(item_index / matrix_dim) + 1][item_index % matrix_dim]
        #     up[int(item_index / matrix_dim) + 1][item_index % matrix_dim] = 'w'
        #     up[int(item_index / matrix_dim)][item_index % matrix_dim] = removed
        #     res.append(tuple(up))
        #
        # if int(item_index / matrix_dim) > 0:
        #     do = deepcopy(node)
        #     removed = do[int(item_index / matrix_dim) - 1][item_index % matrix_dim]
        #     do[int(item_index / matrix_dim) - 1][item_index % matrix_dim] = 'w'
        #     do[int(item_index / matrix_dim)][item_index % matrix_dim] = removed
        #     res.append(tuple(do))

        return res

    def is_goal_reached(self, current, goal):
        """ returns true when we can consider that 'current' is the goal"""
        return current == goal

    def reconstruct_path(self, last, reversePath=False):
        # def _gen():
        #     current = last
        #     while current:
        #         yield current.data
        #         current = current.came_from

        # if reversePath:
        #     return _gen()
        # else:
        #     return reversed(list(_gen()))
        res = []
        res.append(last.data)
        current = last.came_from
        while current != None:
            res.append(current.data)
            current = current.came_from
        return list(reversed(res))

    def astar(self, start, goal, reversePath=False):
        if self.is_goal_reached(start, goal):
            return [start]
        searchNodes = AStar.SearchNodeDict()
        startNode = searchNodes[start] = AStar.SearchNode(
            start, gscore=.0, fscore=self.heuristic_cost_estimate(start, goal))
        openSet = []
        heappush(openSet, startNode)
        count = 0
        while openSet:
            current = heappop(openSet)
            if self.is_goal_reached(current.data, goal):
                return self.reconstruct_path(current, reversePath)
            current.out_openset = True
            current.closed = True
            neigh = self.neighbors(current.data)
            for neighbor in [searchNodes[n] for n in self.neighbors(current.data)]:
                if neighbor.closed:
                    continue
                tentative_gscore = current.gscore + 1
                # tentative_gscore = self.distance_between(
                #     current.data, neighbor.data)
                if tentative_gscore >= neighbor.gscore:
                    continue
                neighbor.came_from = current
                neighbor.gscore = current.gscore + 1
                neighbor.fscore = neighbor.gscore + \
                    self.heuristic_cost_estimate(neighbor.data, goal)
                if neighbor.out_openset:
                    neighbor.out_openset = False
                    heappush(openSet, neighbor)
                else:
                    # re-add the node in order to re-sort the heap
                    openSet.remove(neighbor)
                    heappush(openSet, neighbor)
            print("current node has g: ",
                  current.gscore, " f: ", current.fscore)
            count += 1
            print(count)
        return None


if __name__ == "__main__":
    goal = [[-1, -1, -1, 4], [3, 0, 1, 2],
            [3, 4, 2, 3], [1, 1, 1, 2], [4, 4, 2, 3]]
    t_goal = tuple(tuple(i) for i in goal)

    start = [[-1, -1, -1, 0], [1, 2, 3, 4],
             [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    s_tuple = tuple(tuple(i) for i in start)
    path = (AStar().astar(s_tuple, t_goal,
                          False))
    for step in path:
        for what in step:
            print(list(what))
        print("\n")
