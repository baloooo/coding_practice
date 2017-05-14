"""
Given a graph and a source vertex in graph, find shortest paths from source to
all vertices in the given graph.
http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
One source, one destination:
Greedy Best First Search
A* - commonly used in games
One source, all destinations, or all sources, one destination:
Breadth First Search - unweighted edges
Dijkstra’s Algorithm - adds weights to edges
Bellman-Ford - supports negative weights
All sources, all destinations:
Floyd-Warshall
Johnson’s Algorithm
"""

import sys


class Vertex:
    def __init__(self, node):
        # Node value ('A'/'B' or 0/1/2 or 'Tokyo'/'Osaka' etc.
        self.id = node
        # {adjacent_node: edge weight b/w cur_node and adjacent_node}
        self.adjacent = {}
        # distance from cur_node to source
        # Initially Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Initially Mark all nodes unvisited
        self.visited = False
        # Predecessor(Prev node in shortest path to source)
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str(
            [x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


class Solution:

    def shortest(self, v, path):
        ''' make shortest path from v.previous'''
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
        return

    def dijkstra(self, graph, source, destination):
        pass


if __name__ == '__main__':
    pass
