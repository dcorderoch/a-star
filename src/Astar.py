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

    def heuristic_cost_estimate(self, current, goal):
        """Computes the estimated (rough) distance between a node and the goal, this method must be implemented in a subclass. The second parameter is always the goal."""
        return self.distance_between(current, goal)

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

        l2 = node[:2]+ (self.left_shift(node[2], 1),)+node[3:]

        r2 = node[:2]+ (self.right_shift(node[2], 1),)+node[3:]

        l3 = node[:3]+ (self.left_shift(node[3], 1),)+node[4:]

        r3 = node[:3]+ (self.right_shift(node[3], 1),)+node[4:]

        l4 = node[:4]+ (self.left_shift(node[4], 1),)

        r4 = node[:4]+ (self.right_shift(node[4], 1),)

        res.append(tuple(l1))
        res.append(tuple(r1))
        res.append(tuple(l2))
        res.append(tuple(r2))
        res.append(tuple(l3))
        res.append(tuple(r3))
        res.append(tuple(l4))
        res.append(tuple(r4))

        matrix_dim = len(node[0])
        item_index = 0
        for row in node:
            for i in row:
                if i == 'w':
                    break
                item_index += 1
            if i == 'w':
                break
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
        def _gen():
            current = last
            while current:
                yield current.data
                current = current.came_from

        if reversePath:
            return _gen()
        else:
            return reversed(list(_gen()))

    def astar(self, start, goal, reversePath=False):
        if self.is_goal_reached(start, goal):
            return [start]
        searchNodes = AStar.SearchNodeDict()
        startNode = searchNodes[start] = AStar.SearchNode(
            start, gscore=.0, fscore=self.heuristic_cost_estimate(start, goal))
        openSet = []
        heappush(openSet, startNode)
        while openSet:
            current = heappop(openSet)
            if self.is_goal_reached(current.data, goal):
                return self.reconstruct_path(current, reversePath)
            current.out_openset = True
            current.closed = True
            for neighbor in map(lambda n: searchNodes[n], self.neighbors(current.data)):
                if neighbor.closed:
                    continue
                tentative_gscore = current.gscore + \
                                   self.distance_between(current.data, neighbor.data)
                if tentative_gscore >= neighbor.gscore:
                    continue
                neighbor.came_from = current
                neighbor.gscore = tentative_gscore
                neighbor.fscore = tentative_gscore + \
                                  self.heuristic_cost_estimate(neighbor.data, goal)
                if neighbor.out_openset:
                    neighbor.out_openset = False
                    heappush(openSet, neighbor)
                else:
                    # re-add the node in order to re-sort the heap
                    openSet.remove(neighbor)
                    heappush(openSet, neighbor)
        return None


if __name__ == "__main__":
    path =  (AStar().astar((('x', 'x', 'x', 'w'),
                   ('3','4','1', '2' ),
                   ('1', '2', '3', '4'),
                   ('1', '2', '3', '4'),
                   ('1', '2', '3', '4'))
                  , (('x', 'x', 'x', 'w'),
                     ('1', '2', '3', '4'),
                     ('1', '2', '3', '4'),
                     ('1', '2', '3', '4'),
                     ('1', '2', '3', '4')),
                  False))

    for step in path:
        for what in step:
            print(list(what))
        print("\n")

