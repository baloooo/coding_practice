"""
Find all bridges in a graph.
Algo is similar to one used in articulation points i.e tarjan's algo.
http://stackoverflow.com/questions/11218746/bridges-in-a-connected-graph
"""


class Node:
    def __init__(self, data):
        self.data = data
        # Time stamp when this node was visited
        self.visited_time = None
        # Lowest timestamp node reachable from this node
        self.low_time = None
        self.parent = None
        # nodes directly connected to this node.
        self.adjacent = set()


class Graph:
    def __init__(self):
        self.cur_time = 0
        self.bridges = set()

    def find_bridges(self, node_map):
        """
        This assumes graph is connected else we'll have to call find_bridges in a loop
        unitll all non visited nodes are visited.
        for node in node_map:
            if not node.visited:
                self.dfs(node)
        return [(u.data, v.data) for u, v in self.bridges]
        """
        self.dfs(node_map[0])
        return [(u.data, v.data) for u, v in self.bridges]

    def dfs(self, cur_node):
        # It's just a regular DFS with a bit of book keeping, which helps us to find articulation points.  # noqa
        cur_node.visited_time = self.cur_time
        cur_node.low_time = self.cur_time
        self.cur_time += 1
        for adjacent_node in cur_node.adjacent:
            # if adjacent_node not visited yet.
            if adjacent_node.visited_time is None:
                adjacent_node.parent = cur_node
                self.dfs(adjacent_node)
                cur_node.low_time = min(cur_node.low_time,
                                        adjacent_node.low_time)
                if adjacent_node.low_time == adjacent_node.visited_time:
                    # This means an edge b/w cur_node and adjacent_node will be a bridge, as this adjacent_node doesn't have any back edge (as low_time is what we set at the beginning)  # noqa
                    self.bridges.add((cur_node, adjacent_node))
            elif adjacent_node != cur_node.parent:
                cur_node.low_time = min(cur_node.low_time,
                                        adjacent_node.visited_time)

if __name__ == '__main__':
    test_cases = [
        (5, [[1, 2], [0, 1], [0, 2], [0, 3], [3, 4]]),
        (4, [[0, 1], [1, 2], [2, 3]]),
        (7, [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]]),
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
        print g.find_bridges(node_map)
