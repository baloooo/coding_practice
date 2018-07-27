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
		Note the definition of tree in the problem statement, it is a bit loose on number of parents any child node
		can have. The more precise definition of tree is realized in findRedundantConnection2
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        redundant_edge = None
        dsu_obj = DSU()
        for src, dest in edges:
            if dsu_obj.make_edge(src, dest):
                redundant_edge = [src, dest]
        return redundant_edge
