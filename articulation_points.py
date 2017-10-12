# coding: utf-8
"""
Find all articulation points in a graph.

Implementation of Tarjan’s algorithm for finding articulation points

Time Complexity: The above function is simple DFS with additional arrays.
So time complexity is same as DFS which is O(V+E) for adjacency list
representation of graph.

Idea: https://www.youtube.com/watch?v=2kREIkF9UAs
"""


class Node:
    def __init__(self, data):
        self.visited = False
        self.data = data
        # Time stamp when this node was visited
        self.visited_time = None
        # Lowest timestamp node reachable from this node
        self.low_time = None
        self.child_count = 0
        self.parent = None
        # nodes directly connected to this node.
        self.adjacent = set()


class Graph:
    def __init__(self):
        self.cur_time = 0
        self.cut_vertices = set()

    def find_articulation_points(self, node_map):
        self.dfs(node_map[0])
        return [node.data for node in self.cut_vertices]

    def dfs(self, cur_node):
        # It's just a regular DFS with a bit of book keeping,
        # which helps us to find articulation points.
        cur_node.visited = True
        cur_node.visited_time = self.cur_time
        cur_node.low_time = self.cur_time
        self.cur_time += 1
        articulation_point = False
        for adjacent_node in cur_node.adjacent:
            if adjacent_node == cur_node.parent:
                continue
            if not adjacent_node.visited:
                adjacent_node.parent = cur_node
                cur_node.child_count += 1
                self.dfs(adjacent_node)
                if cur_node.visited_time <= adjacent_node.low_time:
                    """
                    The time cur_node was first visited is the lowest among all
                    the adjacent nodes low times (lowest time node visited from
                    any of the adjacent node)
                    or
                    This means that cur_node doesn't have any backedge to any
                    of it's ancestors and therefore removing this node will
                    disconnect subtree rooted at cur_node from rest of the
                    graph.
                    """
                    articulation_point = True
                else:
                    # Check if the subtree rooted with v has a connection to
                    # one of the ancestors of u,to be precise earliest ancestor
                    cur_node.low_time = min(cur_node.low_time,
                                            adjacent_node.low_time)
            else:
                """
                if adjacent is already visited see if this was visited earlier
                than current node meaning it's visited time is less, if yes
                then this would be a back edge and therefore update current
                node's low time which is basically the visited time stamp of
                the earliest node that can be visited from cur_node.
                Notice: min here is with adjacent's visited time whereas
                if we were visiting this for the first time we'd take min
                b/w adjacent's low time (as above)
                """
                cur_node.low_time = min(cur_node.low_time,
                                        adjacent_node.visited_time)
        # cur_node.parent is None only for the root of DFS
        if ((cur_node.parent is None and cur_node.child_count >= 2) or
                cur_node.parent is not None and articulation_point):
            self.cut_vertices.add(cur_node)

if __name__ == '__main__':
    test_cases = [
        (5, [[1, 2], [0, 1], [0, 2], [0, 3], [3, 4]]),
        (4, [[0, 1], [1, 2], [2, 3]]),
        (7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]]),
        (3, [[0, 1], [1, 0], [1, 2], [2, 1], [0, 2], [2, 0]]),
    ]
    for test_case in test_cases:
        n = test_case[0]
        edges = test_case[1]
        # Graph construction
        node_map = {}
        for i in xrange(n):
            node = Node(i)
            node_map[i] = node
        for u, v in edges:
            u_node = node_map[u]
            v_node = node_map[v]
            u_node.adjacent.add(v_node)
            v_node.adjacent.add(u_node)
        g = Graph()
        print g.find_articulation_points(node_map)
