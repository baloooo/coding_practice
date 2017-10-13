"""
The idea of disjoint datastructures is more clearly shown with the help of implementation of 
kruskal algorithm where we break each node in the graph to individual nodes and then pick
minimum weight edge and see if it help join two different forests and not nodes with in the same
forest as our end goal is to have minimum number of edges that can join all the nodes in the graph.
Here disjoint set helps in:
Helping find if this min. weight edge joins two nodes of already connected graph or not.

In computer science, a disjoint-set data structure, also called a union–find data structure or merge–find set, is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides near-constant-time operations (bounded by the inverse Ackermann function) to add new sets, to merge existing sets, and to determine whether elements are in the same set. In addition to many other uses (see the Applications section), disjoint-sets play a key role in Kruskal's algorithm for finding the minimum spanning tree of a graph.

Disjoint set data structure using path compression (for better find complexity)
and union by rank.
"""


class Node:
    def __init__(self, **kwargs):
        self.data = None
        self.parent = None
        self.rank = 0
        for key, value in kwargs.items():
            self.key = value


class DisjointSet(object):

    def __init__(self):
        self.data_node_map = {}

    def make_set(self, data):
        if self.data_node_map.get(data):
            return self.data_node_map[data]
        node = Node()
        node.data = data
        node.parent = node
        self.data_node_map[data] = node

    def find_parent_value(self, data):
        """
        @Accepts: data
        @Returns: data
        """
        node = self.data_node_map[data]
        return self.find_parent_node(node).data

    def find_parent_node(self, cur_node):
        """
        finds the representative of the set recursively and
        does the path compression as well.
        @Accepts: node
        @Returns: node
        """
        if cur_node.parent == cur_node:
            return cur_node
        else:
            cur_node.parent = self.find_parent_node(cur_node.parent)
        return cur_node.parent

    def union(self, data1, data2):
        """
        combines two sets, does union by rank
        """
        node1 = self.data_node_map[data1]
        node2 = self.data_node_map[data2]
        node1_parent = self.find_parent_node(node1)
        node2_parent = self.find_parent_node(node2)
        if node1_parent == node2_parent:
            # Both are part of the same set
            return
        if node1_parent.rank >= node2_parent.rank:
            if node1_parent.rank == node2_parent.rank:
                node1_parent.rank += 1
            # Make node1 as the parent of the comnined set
            node2_parent.parent = node1_parent
        else:
            node1_parent.parent = node2_parent

if __name__ == '__main__':
    dj_set = DisjointSet()
    for i in xrange(1, 10):
        dj_set.make_set(i)
    dj_set.union(1, 2)
    dj_set.union(2, 3)
    dj_set.union(4, 5)
    dj_set.union(5, 6)
    dj_set.union(3, 7)
    print dj_set.find_parent_value(7)
    print dj_set.find_parent_value(1)
    print dj_set.find_parent_value(5)
