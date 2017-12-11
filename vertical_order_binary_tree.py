

class Solution:
    def vertical_order(self, root):
        '''
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
