"""
Find all bridges in a graph.
Algo is similar to one used in articulation points i.e tarjan's algo.
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
                self.dfs(adjacent_node)
                cur_node.low_time = min(cur_node.low_time,
                                        adjacent_node.low_time)
                if cur_node.low_time == cur_node.visited_time:
                    # This means an edge b/w cur_node and adjacent_node will be a bridge.  # noqa
                    self.bridges.add((cur_node, adjacent_node))
            elif adjacent_node != cur_node.parent:
                cur_node.low_time = min(cur_node.low_time,
                                        adjacent_node.visited_time)

        for adjacent_node in cur_node.adjacent:
            if adjacent_node == cur_node.parent:
                continue
            if not adjacent_node.visited:
                adjacent_node.parent = cur_node
                cur_node.child_count += 1
                self.dfs(adjacent_node)
                if cur_node.visited_time <= adjacent_node.low_time:
                    """
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
