class Solution(object):
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col]!='1': return
        # mark all adjacent connected nodes as 0
        grid[row][col] = 0
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row-1, col)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Idea: no. of connected components
        Time: O(n)
        Space: O(size of grid + stack_depth for dfs i.e total_no_of_nodes) = O(2n) = O(n) where n = total_no_of_nodes
        """
        from copy import deepcopy
        grid_map = deepcopy(grid) # incase we're not allowed to modify existing grid
        islands = 0
        for row in xrange(len(grid_map)):
            for col in xrange(len(grid_map[0])):
                if grid_map[row][col] == '1':
                    self.dfs(grid_map, row, col)
                    islands += 1
        return islands

class Solution(object):
  def numIslands_optimized(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    Need to go over this
    """
    if not grid or not grid[0]:
            return 0
        
    root = []

    m, n = len(grid), len(grid[0])
    res = 0
    for i in xrange(m):
        for j in xrange(n):
            if grid[i][j] == '1':
                flag = True
                if i > 0 and grid[i-1][j] != '0':
                    flag = False
                    grid[i][j] = root[grid[i-1][j]]
                if j > 0 and grid[i][j-1] != '0':
                    if flag:
                        grid[i][j] = root[grid[i][j-1]]
                    else:
                        root[grid[i][j-1]] = grid[i][j]
                    flag = False
                if flag:
                    grid[i][j] = res
                    root.append(res)
                    res += 1
    return sum(root[i] == i for i in xrange(len(root)))
