"""
https://www.youtube.com/watch?v=pVfj6mxhdMw
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

    def dijkistra_search(self, source, destination):
        frontier = PriorityQueue()
        frontier.put(source, 0)
        came_from = {}
        cost_so_far = {}
        came_from[source] = None
        cost_so_far[source] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == destination:
                break

            for adjacent in self.neighbor_map[current]:
                """
                calculate new_cost to all adjacent nodes from current node
                to check if we can find a smaller weight path.
                """
                new_cost = cost_so_far[current] + self.cost(current, adjacent)
                if adjacent not in cost_so_far or (
                        new_cost < cost_so_far.get(adjacent, float('inf'))):
                    cost_so_far[adjacent] = new_cost
                    priority = new_cost
                    frontier.put(adjacent, priority)
                    came_from[adjacent] = current
        import ipdb
        ipdb.set_trace()
        return came_from, cost_so_far

if __name__ == '__main__':
    g_obj = GraphWithWeights()
    g_obj.edges = {
        ('a', 'b'): 7,
        ('a', 'c'): 9,
        ('a', 'f'): 14,
        ('b', 'c'): 10,
        ('b', 'd'): 15,
        ('c', 'd'): 11,
        ('c', 'f'): 2,
        ('d', 'e'): 6,
        ('e', 'f'): 9,
        ('b', 'a'): 7,
        ('c', 'a'): 9,
        ('f', 'a'): 14,
        ('c', 'b'): 10,
        ('d', 'b'): 15,
        ('d', 'c'): 11,
        ('f', 'c'): 2,
        ('e', 'd'): 6,
        ('f', 'e'): 9,
    }
    g_obj.neighbors()
    print g_obj.dijkistra_search('a', 'e')
