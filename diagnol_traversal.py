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
            # order of these ifs is important here Todo: why is this order important.
            if row >= row_len: # went off bottom boundary
                row = row_len - 1
                col += 2
                d = -d
            if col >= col_len: # went off right boundary
                col = col_len - 1
                row += 2 # since row
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
