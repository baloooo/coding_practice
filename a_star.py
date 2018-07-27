"""
https://www.youtube.com/watch?v=eSOJ3ARN5FM
http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
Time: O(E), Space: O(V), its worst case is similar to BFS/DFS but ideally should be far better than this due to the heuristic we include in our strategy for finding the next best node that would lead us to our goal.

A* is a best first search algorithm(with BFS type queue, though in practice it uses a PriorityQueue).
Notice that the 
A* selects the path that minimizes f(n)=g(n)+h(n)
where n is the last node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal.
The heuristic is problem-specific. For the algorithm to find the actual shortest path, the heuristic function must be admissible, meaning that it never overestimates the actual cost(minimum cost in path finding) to get to the goal node.
It's guaranteed to find the path, if a path exists but how quickly it does so depends on some extent to chance(b'coz we can pick any node from a set of nodes that have the same f(n)) but very much on the quality of our heuristics.Ideally the heuristic distances should be as close to the actual remaining distances to the goal, but not    greater.
If the heuristic estimates are too small, frontier will expand unneccessarily and A* will waste time in exploring unfavorale nodes. In fact if heuristic for all nodes are zero, A* will traverse all nodes which is what dijkistra's algo does.
On the other hand if heuristics are overestimated, A* will find a path to goal but that may not be the shortest
path to goal node.
Finding the heuristics is very critical to A*, and very much depends on the nature of the problem
"""

import heapq
from collections import defaultdict


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (item, priority))

    def get(self):
        return heapq.heappop(self.elements)[0]


class GraphWithWeights:
    def __init__(self):
        self.edges = {}
        self.neighbor_map = defaultdict(list)

    def neighbors(self):
        """
        populates self.neighbor as {'a': ['b', 'c', 'f'], ....}
        """
        for source, dest in self.edges:
            self.neighbor_map[source].append(dest)

    def cost(self, from_node, to_node):
        return self.edges.get((from_node, to_node))

    def heuristic(self, current, destination):
        """
        These heuristics can be euclidean distance/manhattan distance etc
        depending on the type of search space(grid/graph) or type of problem
        in general terrain, forest, down hill in path ways.
        """
        pass

    def a_star_search(self, source, destination):
        frontier = PriorityQueue()
        frontier.put(source, 0)
        came_from = {}
        cost_so_far = defaultdict(lambda: float('inf'))
        came_from[source] = None
        cost_so_far[source] = 0

        while not frontier.empty():
            current = frontier.get()

            for adjacent in self.neighbor_map[current]:
                """
                calculate new_cost to all adjacent nodes from current node
                to check if we can find a smaller weight path.
                TIP: Compare and contrast with the dijkistra implementation in network_delay_time
                """
                new_cost = cost_so_far[current] + self.cost(current, adjacent)
                if new_cost < cost_so_far[adjacent]:
                    cost_so_far[adjacent] = new_cost
                    priority = new_cost + self.heuristic(destination, adjacent) # This step sets apart astar from dijkistra
                    frontier.put(adjacent, priority)
                    came_from[adjacent] = current
        return came_from, cost_so_far

if __name__ == '__main__':
    # These examples don't run, these were copied from dijkstra example.
    # use a grid and add heuristic logic to run
    g_obj = GraphWithWeights()
    g_obj.edges = {
        (0, 1): 4,
        (0, 7): 8,
        (1, 2): 8,
        (1, 7): 11,
        (2, 3): 7,
        (2, 8): 2,
        (2, 5): 4,
        (3, 4): 9,
        (3, 5): 14,
        (4, 5): 10,
        (5, 6): 2,
        (6, 7): 1,
        (6, 8): 6,
        (7, 8): 7,
        (1, 0): 4,
        (7, 0): 8,
        (2, 1): 8,
        (7, 1): 11,
        (3, 2): 7,
        (8, 2): 2,
        (5, 2): 4,
        (4, 3): 9,
        (5, 3): 14,
        (5, 4): 10,
        (6, 5): 2,
        (7, 6): 1,
        (8, 6): 6,
        (8, 7): 7,
    }
    # g_obj.edges = {
    #     ('a', 'b'): 7,
    #     ('a', 'c'): 9,
    #     ('a', 'f'): 14,
    #     ('f', 'e'): 9,
    #     ('b', 'c'): 10,
    #     ('b', 'd'): 15,
    #     ('c', 'd'): 11,
    #     ('c', 'f'): 2,
    #     ('d', 'e'): 6,
    #     ('e', 'f'): 9,
    #     ('b', 'a'): 7,
    #     ('c', 'a'): 9,
    #     ('f', 'a'): 14,
    #     ('c', 'b'): 10,
    #     ('d', 'b'): 15,
    #     ('d', 'c'): 11,
    #     ('f', 'c'): 2,
    #     ('e', 'd'): 6,
    # }
    g_obj.neighbors()
    # print g_obj.dijkistra_search('a', 'e')
    print g_obj.a_star_search(0, 5)
