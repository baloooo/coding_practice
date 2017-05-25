"""
Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists of one or more
adjacent X's (diagonals not included)

Example:

OOOXOOO
OOXXOXO
OXOOOXO

answer is 3 shapes are  :
(i)    X
     X X
(ii)
      X
 (iii)
      X
      X

Note that we are looking for connected shapes here.

For example,

XXX
XXX
XXX

is just one single connected black shape.

"""


class Solution:
    def __init__(self):
        pass

    def dfs(self, grid, row, col):
        if grid[row][col] == '0':
            return
        # Add current position as visited
        grid[row][col] = '0'
        if row+1 < len(grid) and grid[row+1][col] == 'X':
            self.dfs(grid, row+1, col)
        if row-1 >= 0 and grid[row-1][col] == 'X':
            self.dfs(grid, row-1, col)
        if col+1 < len(grid[0]) and grid[row][col+1] == 'X':
            self.dfs(grid, row, col+1)
        if col-1 >= 0 and grid[row][col-1] == 'X':
            self.dfs(grid, row, col-1)

    def connected_components(self, graph):
        """
        This exercise basically boils down to finding connected components
        in a graph.
        """
        connected_component = 0
        grid = [list(row) for row in graph]
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if grid[row][col] == 'X':
                    connected_component += 1
                    self.dfs(grid, row, col)
        return connected_component

if __name__ == '__main__':
    test_cases = [
        ([
            "OOOXOOO",
            "OOXXOXO",
            "OXOOOXO"], 3),
        ([
            'XX',
            'XX'], 1),
        ([
            '00'], 0),
    ]
    for test_case in test_cases:
        res = Solution().connected_components(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
