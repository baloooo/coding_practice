

class Solution:
    def vertical_order(self, root):
        '''
        One idea is to use a dictionary with mapping of distance from root node to list of nodes at
        that distance. And then run a tree traversal (preorder) on the whole tree finally 
        ort the keys and return it.

        The only catch here is that nodes on same distance from root will be ordered from bottom to top.
        If you want it to be top to bottom, you can use BFS for tree traversal, both ideas would
        provide left to right ordering though.
        http://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/
        '''
        from collections import defaultdict
        from collections import deque
        cols = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue: # Level order traversal
            node, index = queue.popleft()
            if node:
                queue.append((node.left, index-1))
                queue.append((node.right, index+1))
                cols[index].append(node)
        return [cols[col] for col in sorted(cols)]

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
