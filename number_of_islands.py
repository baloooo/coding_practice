'''https://leetcode.com/articles/number-of-islands/ '''

class Solution(object):
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col]!='0': return
        # mark all adjacent connected nodes as 0
        grid[row][col] = '0'
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
        Notice that using BFS here is a more clever solution here, as BFS would take less space than
        a DFS.
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

    def bfs(self, grid, row, col):
        from Queue import Queue
        bfs_q = Queue()
        bfs_q.put((row, col))
        grid[row][col] = '0'
        while not bfs_q.empty():
            for _ in xrange(len(bfs_q.queue)):
                cur_row, cur_col = bfs_q.get()
                # grid[cur_row][cur_col] = '0'
                if 0 <= cur_row+1 < len(grid) and grid[cur_row+1][cur_col] == '1':
                    bfs_q.put((cur_row+1, cur_col))
		    # Note: mark them invalid right here, so no one else tries to traverse it.
                    grid[cur_row+1][cur_col] = '0'
                if 0 <= cur_row-1 < len(grid) and grid[cur_row-1][cur_col] == '1':
                    bfs_q.put((cur_row-1, cur_col))
                    grid[cur_row-1][cur_col] = '0'
                if 0 <= cur_col+1 < len(grid[0]) and grid[cur_row][cur_col+1] == '1':
                    bfs_q.put((cur_row, cur_col+1))
                    grid[cur_row][cur_col+1] = '0'
                if 0 <= cur_col-1 < len(grid[0]) and grid[cur_row][cur_col-1] == '1':
                    bfs_q.put((cur_row, cur_col-1))
                    grid[cur_row][cur_col-1] = '0'
                    
    def numIslands_bfs(self, grid):
        """
	This is space efficient as the max queue size in bfs can be of min(m, n) with grid m*n dimension.
	We will get a queue with all diagnols(which can be of size min(m,n)) when there are all
	one's in the grid.
        """
        islands = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    islands += 1
        return islands
