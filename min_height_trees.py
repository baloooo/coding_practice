# coding: utf-8
'''
The idea is to start from leaf and root node(s) and keep adding nodes in a BFS way, as we're starting from extreme ends(leaves
and root) the place we meet has to be the mid way between.
https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
The problem is stated it is “a undirected graph with tree characteristics” which means all vertexes is connected

The node which will minimize the height will be
    mid node if total node count is odd
    or
    mid two node if total node count is even

For additional ideas: https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/
'''


class Solution:
    def __init__(self):
        pass

    def mht(self, n, edges):
        if n == 1:
            return [0]
        # Index as node and value at index is the adjacent set containing all nodes adjacent to this node.
        adj = [set() for _ in xrange(n)]
        for src, dest in edges:
            adj[src].add(dest)
            # since edges are undirected in this case
            adj[dest].add(src)
        leaves = [index for index in xrange(n) if len(adj[index]) == 1]

        # Loop until total vertex remains less than 2
        while n > 2:
            # Note: As we can pop a max of n-2 nodes from n after which we should end up with our root(s).
            # This step is very crucial as this takes care of when to terminate the loop
            n -= len(leaves)
            new_leaves = []
            for leaf_index in leaves:
                adj_to_leaf = adj[leaf_index].pop() # since there would be only 1 adjacent as it is leaf node.
                adj[adj_to_leaf].remove(leaf_index) # remove leaf node as adjacent from whichever node had it.
                if len(adj[adj_to_leaf]) == 1:
                    new_leaves.append(adj_to_leaf)
            leaves = new_leaves
        return leaves


if __name__ == '__main__':
    test_cases = [
        (4, [[1, 0], [1, 2], [1, 3]], [1]),
        (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]], [3, 4]),
    ]
    for test_case in test_cases:
        res = Solution().mht(test_case[0], test_case[1])
        if res == test_case[2]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[1], res, test_case[2])
