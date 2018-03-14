'''
https://leetcode.com/problems/graph-valid-tree/discuss/69020/8-10-lines-Union-Find-DFS-and-BFS
A  graph is a Tree if it has two properties:
    1. For n nodes there should be n-1 edges.
    2. Graph should be acyclic
Since we're given undirected edges instead of directed, the way we check acyclicity
is that, either graph has n-1 edges but has a redundant edge(as in last test case) therefore
since there are only n-1 edges graph shouldn't be connected now which is checked by our DFS
method.
Else if it has less than n-1 edges we know for sure it can connect all n nodes with less
than n-1 edges and if it has more we can be sure there are redundant edges b/w nodes which
will make a cycle and therefore acyclic property is violated.
The way our DFS works is that we pop a key and traverse all its neighbors in dfs fashion to 
pop their keys to this way all connected nodes should be removed by the end of dfs. And
if by the end of DFS there're any nodes in graph it means this node was not connected to the
rooted tree at zero and therefore this is not a tree.
'''

import pytest
import collections


class Solution(object):
    def dfs(self, graph, cur):
        for neighbor in graph.pop(cur, []):
            self.dfs(graph, neighbor) 

    def validTree(self, n, edges):
        if len(edges) != n-1:
            return False
        # construct adjacency list based graph
        # Cannot use this graph = collections.defaultdict(list)
        graph = {}
        for i in xrange(n):
            graph[i] = []
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        # root can be defaulted to zero
        self.dfs(graph, 0)
        # all nodes should have been popped out of graph
        # other words visited
        return not graph

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("n, edges, result", [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
        (0, [[]], False),
        (2, [[1, 0]], True),
        (6, [[0, 1], [0, 5], [1, 2], [1, 4], [4, 5]], False),
        ])
    def test_task(self, n, edges, result):
        sol = Solution()
        cur_res = sol.validTree(n, edges)
        # import ipdb; ipdb.set_trace()
        assert cur_res == result

if __name__ == '__main__':
    # n, edges, result = (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True)
    n, edges, result = (2, [[1, 0]], True)
    # since root is 1 in this case, and no edge from 1 to 0 loop dies out.
    sol = Solution()
    cur_res = sol.validTree(n, edges)
    if cur_res == result:
        print 'passed'
    else:
        print 'failed'
