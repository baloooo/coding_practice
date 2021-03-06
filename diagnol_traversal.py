class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        Time: O(mn), Space: O(1)
        :type matrix: List[List[int]]
        :rtype: List[int]
        https://discuss.leetcode.com/topic/77865/concise-java-solution?page=1
        """
        if not matrix: return []
        res, row_len, col_len = [], len(matrix), len(matrix[0])
        row, col, d = 0, 0, 1
        for _ in xrange(row_len * col_len):
            # d is the direction while going down keep decrementing this from col and 
            # adding this to row and vice-versa while going up.
            res.append(matrix[row][col])
            row -= d
            col += d
            '''
            # order of these ifs is important here
            This is because for when we go off from top right corner we should use 'violated right boundary'
            condition solution and not 'violated top boundary' as we can see from the diagram in problem statement
            when we go off from top right corner 'violated right boundary' conditions can help pointers bring back
            to actual course required.
            Same is true when we go off from bottom right corner
            Therefore bottom line is to have bottom and right conditions before the other two.
            '''
            if row >= row_len: # went off bottom boundary
                row = row_len - 1
                col += 2
                d = -d
            if col >= col_len: # went off right boundary
                col = col_len - 1
                row += 2 # This will make more sense when you visualize the trajectory of going off right boundary.
                d = -d
            if row < 0: # went off top border
                row = 0 # col is already at correct pos'n
                d = -d
            if col < 0: # went off left boundary
                col = 0
                d = -d
        return res

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print Solution().findDiagonalOrder(matrix)
