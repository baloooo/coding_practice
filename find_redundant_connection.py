class Node(object):
    def __init__(self, label, **kwargs):
        self.label = label
        self.parent = self
        self.rank = 0
        '''
        for key, value in kwargs.items():
            self.key = value
        '''

class DSU(object):
    def __init__(self):
        self.node_graph = {}

    def _make_set(self, data):
        node = Node(data)
        self.node_graph[data] = node

    def _find_parent(self, node):
        if node.parent == node:
            return node
        else:
            return self._find_parent(node.parent)

    def _union(self, data1, data2):
        '''returns True if data1 and data2 were a part of the same forest and therefore no union was done'''
        node1, node2 = self.node_graph[data1], self.node_graph[data2]
        node1_parent, node2_parent = self._find_parent(node1), self._find_parent(node2)
        if node1_parent == node2_parent:
            return True
        if node1_parent.rank >= node2_parent.rank:
            if node1_parent.rank == node2_parent.rank:
                node1_parent.rank += 1
            node2_parent.parent = node1_parent
        else:
            node1_parent.parent = node2_parent

        return False


    def make_edge(self, data1, data2):
        'returns True if edge already existed else False'
        for data in [data1, data2]:
            if data not in self.node_graph:
                self._make_set(data)
        return self._union(data1, data2)


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        redundant_edge = None
        dsu_obj = DSU()
        for src, dest in edges:
            if dsu_obj.make_edge(src, dest):
                redundant_edge = [src, dest]
        return redundant_edge

########################################################################################################################

'''
We can not simply apply the code from REDUNDANT CONNECTION I, and add codes checking duplicated-parent only.
Here are 2 sample failed test cases:
[[4,2],[1,5],[5,2],[5,3],[2,4]]
got [5,2] but [4,2] expected
and
[[2,1],[3,1],[4,2],[1,4]]
got [3,1] but [2,1] expected
(Thanks @niwota and @wzypangpang )
The problem is we can not consider the two conditions separately, I mean the duplicated-parents and cycle.
This problem should be discussed and solved by checking 3 different situations:

No-Cycle, but 2 parents pointed to one same child
No dup parents but with Cycle
Possessing Cycle and dup-parents
Those 2 failed test cases are all in situation 3), where we can not return immediately current edge when we found something against the tree's requirements.
The correct solution is detecting and recording the whole cycle, then check edges in that cycle by reverse order to find the one with the same child as the duplicated one we found.
A more clear explanation and code have been posted by @niwota
https://discuss.leetcode.com/topic/105087/share-my-solution-c


https://leetcode.com/problems/redundant-connection-ii/discuss/108046/most-posted-answers-are-wrong
https://leetcode.com/problems/redundant-connection-ii/discuss/108073/share-my-solution-c
https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases

'''

class Node(object):
    def __init__(self, label, **kwargs):
        self.label = label
        self.parent = self
        self.rank = 0
        '''
        for key, value in kwargs.items():
            self.key = value
        '''

class DSU(object):
    def __init__(self):
        self.node_graph = {}

    def _make_set(self, data):
        node = Node(data)
        self.node_graph[data] = node

    def _find_parent(self, node):
        if node.parent == node:
            return node
        else:
            return self._find_parent(node.parent)

    def _union(self, data1, data2):
        '''returns True if data1 and data2 were a part of the same forest and therefore no union was done'''
        node1, node2 = self.node_graph[data1], self.node_graph[data2]
        node1_parent, node2_parent = self._find_parent(node1), self._find_parent(node2)
        if node1_parent == node2_parent:
            return True
        if node1_parent.rank >= node2_parent.rank:
            if node1_parent.rank == node2_parent.rank:
                node1_parent.rank += 1
            node2_parent.parent = node1_parent
        else:
            node1_parent.parent = node2_parent

        return False


    def make_edge(self, data1, data2):
        'returns True if edge already existed else False'
        for data in [data1, data2]:
            if data not in self.node_graph:
                self._make_set(data)
        return self._union(data1, data2)


class Solution(object):
    def dfs(self, graph, cur, orig_node, visited):
        if cur == orig_node:
            return 
        if cur in visited:
            return
        visited.add(adj)
        for adj in graph[cur]:
            if adj not in visited:
                self.dfs(graph, adj, orig_node, visited)

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        cyclic_edge = None # Edge making graph cyclic, found using Disjoint DS.
        dsu_obj = DSU()
        # check cycles
        for src, dest in edges:
            if dsu_obj.make_edge(src, dest):
                cyclic_edge = [src, dest]
        # check if a node has multiple parents
        multiple_parents = None # candidate nodes that have multiple parents
        for src, dest in edges:
            if graph[src]:
                multiple_parents = dest
            graph[src].append(dest)
        # if one or the other is True return else do dfs
        if multiple_parents and cyclic_edge:
            last_cyclic_edge = None
            for adj in graph[multiple_parents]:
                last_cyclic_edge = self.dfs(graph, adj, multiple_parents, set())
            return last_cyclic_edge
        else:
            return cyclic_edge or multiple_parents
