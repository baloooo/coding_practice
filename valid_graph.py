'''
1. Construct adjacency list based graph.
2. DFS traversal marking visited node in process, the moment we encounter a node already visited and this is not the
    parent of cur node, we've a redundant path from current node to this already visited node, which would mean
    there is a cycle which would mean this not a Tree(DAG).
'''

import pytest
import collections

class Node(object):
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.adjacent = []

class Solution(object):
    def create_graph(self, n, edges):
        graph = collections.defaultdict()
        for i in xrange(n):
            node = Node(i)
            graph[i] = node
        for src, dest in edges:
            graph[i].adjacent.append(graph[dest])
        return graph

    def dfs(self, graph, cur, parent):
        cur.visited = True
        for adjacent in cur.adjacent:
            if adjacent.visited is not True:
                return self.dfs(graph, adjacent, cur)
            elif adjacent != parent:
                return False
        return True

    def connected(self, graph):
        # Makes sure all nodes of the graph are visited
        for node in graph.values():
            if node.visited is False:
                return False
        return True

    def validTree(self, n, edges):
        if n == 0:
            return False
        elif n == 1:
            return True
        graph = self.create_graph(n, edges)
        return self.dfs(graph, graph[0], -1) and self.connected(graph)

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("n, edges, result", [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
        (0, [[]], False),
        ])
    def test_task(self, n, edges, result):
        sol = Solution()
        cur_res = sol.validTree(n, edges)
        # import ipdb; ipdb.set_trace()
        assert cur_res == result

if __name__ == '__main__':
    n, edges, result = (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True)
    sol = Solution()
    cur_res = sol.validTree(n, edges)
    if cur_res == result:
        print 'passed'
    else:
        print 'failed'
