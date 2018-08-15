class Solution(object):
    def minimumTotal(self, triangle):
        '''
	https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle

	Time: O(n^2)
	Space: O(n)
        One thing to notice is that each row has one more elements than before.
        This will help us to write loop lengths.
        '''
        # path lenght will be equal to last row columns. + we can make base the last row/layer and start with row -2 index
        min_path = triangle[-1] 
        
        for layer in xrange(len(triangle)-2, -1, -1):
            for col in xrange(0, layer+1, 1):
                min_path[col] = min(min_path[col], min_path[col+1]) + triangle[layer][col]
        
        return min_path[0]
