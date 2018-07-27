# coding: utf-8
'''We can partition a sorted two-dimensional matrix into four sorted submatrices, two of which might contain target and two
of which definitely do not.

Algorithm

Because this algorithm operates recursively, its correctness can be asserted via the correctness of its base and
recursive cases.

Base Case

For a sorted two-dimensional array, there are two ways to determine in constant time whether an arbitrary element target
can appear in it. First, if the array has zero area, it contains no elements and therefore cannot contain target.
Second, if target is smaller than the array's smallest element (found in the top-left corner) or larger than the array's
largest element (found int he bottom-right corner), then it definitely is not present.

Recursive Case

If the base case conditions have not been met, then the array has positive area and target could potentially be present.
Therefore, we seek along the matrix's middle column for an index row such that matrix[row-1][mid]matrix[row−1][mid]
(obviously, if we find target during this process, we immediately return true). The existing matrix can be partitioned
into four submatrices around this index; the top-left and bottom-right submatrices cannot contain target (via the
argument outlined in Base Case section), so we can prune them from the search space. Additionally, the bottom-left and
top-right submatrices are sorted two-dimensional matrices, so we can recursively apply this algorithm to them.


[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''
class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi)//2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))): # As the shorter dimension define the len of diagonal
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False

if __name__ == '__main__':
    matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
    print 'Yo'
    print Solution().searchMatrix(matrix, 24)