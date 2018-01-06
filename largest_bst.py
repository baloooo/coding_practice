'''
https://articles.leetcode.com/largest-binary-search-tree-bst-in/
https://articles.leetcode.com/largest-binary-search-tree-bst-in_22/
'''


class Solution:
    def largest_bst_subtree2(self, root):
        '''
        subtree can be partial tree also covering certain but contiguous nodes.
        '''
        pass


    def largest_bst_subtree(self, root):
        '''
        Below solution seems good, but need to try different test cases
        with Leetcode p
        subtree should be entire tree right to leaf nodes
        https://discuss.leetcode.com/topic/36966/short-python-solution
        '''

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().largest_bst_subtree(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])

