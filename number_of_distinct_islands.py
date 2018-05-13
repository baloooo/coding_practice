'''https://leetcode.com/problems/number-of-distinct-islands/solution/
We'll have to find the canonical shape for any existing shape if rotations/reflections are also
permitted, this would just include a call to get_canonical_shape before adding the paths in seen_paths.
Though finding a canonical_shape is a bit tricky.
https://leetcode.com/problems/number-of-distinct-islands/solution/
'''

class Solution(object):
    def dfs(self, grid, row, col, row0, col0, cur_path):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == 0:
            return
        
        grid[row][col] = 0
        
	'''
	B'coz we're traversing the array in row major order, to tranform/map all co-ordinates
	to origin we can subtract first row and first column from all co-ordinates and since
	rotation and reflection don't matter we can add them in set else we would have added
	them as an array and finely matched that in seen_paths
	'''
        cur_path.append((row - row0, col - col0))
        
        self.dfs(grid, row, col+1, row0, col0, cur_path)
        self.dfs(grid, row, col-1, row0, col0, cur_path)
        self.dfs(grid, row+1, col, row0, col0, cur_path)
        self.dfs(grid, row-1, col, row0, col0, cur_path)
    
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
	Idea: Store path signatures, while doing DFS
	Time and Space: O(m*n) m:#f rows,n:#f cols.
        """
        seen_paths = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    cur_path = []
                    self.dfs(grid, i, j, i, j, cur_path)
                    '''since in a shape co-ordinate sequence doesn't matter, just the co-ordinates
                    themselves matter, we can use a frozenset for the path which would also
                    help us to match any existing shapes in O(1)'''
                    seen_paths.add(frozenset(cur_path))
        return len(seen_paths)

if __name__ == '__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    '''
    This would give this as the paths
    [(0, 0), (0, 1), (1, 1), (1, 0)]
    [(2, 3), (2, 4), (3, 4), (3, 3)]
    '''
    print Solution().numDistinctIslands(grid)
