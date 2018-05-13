'''This problem is exactly same as https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
'''


class DisjointDSNode(object):
    def __init__(self):
        self.val = None
        self.rank = 0
        self.parent = None
        
class DisjoinGraph(object):
    def __init__(self):
        self.node_graph = {} # {position/co-ordinate: Node_object}
        self.islands = 0
        
    def make_set(self, pos, data=0):
        '''
        Default value is zero indicating not a land, and add operation will change this to 1
        '''
        if data in self.node_graph:
            return self.node_graph[pos]
        node = DisjointDSNode()
        node.val = data
        node.parent = node
        self.node_graph[pos] = node
        return self.node_graph[pos]
    
    def find_parent(self, node):
        if node.parent == node:
            return node
        else:
            node.parent = self.find_parent(node.parent)
        return node.parent
    
    def is_island(self, pos_x, pos_y):
        return bool(self.node_graph[(pos_x, pos_y)].val)
    
    def make_island(self, pos_x, pos_y):
        '''
        Each make_island bumps up the number of islands we have now.
        '''
        self.node_graph[(pos_x, pos_y)].val = 1
        self.islands += 1
    
    def union(self, data1, data2):
        '''
        If both data points point to the same forest return, else
        decrease the number of total_islands since now we've merged two different islands.
        '''
        # node1 is the currently being added node, node2 is already a part of islands.
        node1 = self.node_graph[data1]
        node2 = self.node_graph[data2]
        node1_parent = self.find_parent(node1)
        node2_parent = self.find_parent(node2)
        
        if node1_parent == node2_parent: return # they're already a part of the same forest.

        # we're combining two different islands.
        self.islands -= 1
        
        if node1_parent.rank >= node2_parent.rank:
            if node1_parent.rank == node2_parent.rank:
                node1_parent.rank += 1
            
            node2_parent.parent = node1_parent
        else:
            node1_parent.parent = node2_parent
    
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
	https://leetcode.com/problems/number-of-islands-ii/solution/
	Idea is to add all co-ordinates of array m*n in to disjoint set union datastructure.
	Now for each add operation, perform make_island operation which would increase the number
	of islands and also perform union operation with each neighboring cell(if it's valid, as in
	if it has been already added).

	Time complexity : O(m×n+L) where L is the number of operations, m is the number of
	rows and nn is the number of columns. it takes O(m×n) to initialize UnionFind,
	and O(L) to process positions. Note that Union operation takes essentially
	constant time1 when UnionFind is implemented with both path compression and union by rank.

	Space complexity : O(m×n) as required by UnionFind data structure.


        """
        dsu = DisjoinGraph()
        # Step1: Add all nodes to Disjoint set DS
        for i in xrange(m):
            for j in xrange(n):
                dsu.make_set((i, j))
        # Step2: Perform add operations
        islands, cur_islands = [], 0
        for (pos_x, pos_y) in positions:
            dsu.make_island(pos_x, pos_y)
            # merge it with neighboring land
            if 0 <= pos_x+1 < m and dsu.is_island(pos_x+1, pos_y):
                 dsu.union((pos_x, pos_y), (pos_x+1, pos_y))
            if 0 <= pos_x-1 < m and dsu.is_island(pos_x-1, pos_y):
                dsu.union((pos_x, pos_y), (pos_x-1, pos_y))
            if 0 <= pos_y+1 < n and dsu.is_island(pos_x, pos_y+1):
                dsu.union((pos_x, pos_y), (pos_x, pos_y+1))
            if 0 <= pos_y-1 < n and dsu.is_island(pos_x, pos_y-1):
                dsu.union((pos_x, pos_y), (pos_x, pos_y-1))
            islands.append(dsu.islands)
            
        return islands
