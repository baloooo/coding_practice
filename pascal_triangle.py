"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def pascal_triangle(self, n):
        result, pend = [], [1]
        for _ in xrange(n):
            result.append(pend)
            pend = [1] + [pend[k] + pend[k+1] for k in xrange(len(pend)-1)] + [1]
        return result

    def pascal_triangle_latest(self, num_rows):
        # Time: O(n^2)
        # Idea: https://github.com/kamyu104/LeetCode/blob/master/Python/pascals-triangle.py
        # probably easy to comprehend and reproducible in other langs
        res = []
        for i in xrange(num_rows):
            res.append([])
            for j in xrange(i+1):
                if j in [0, i]:
                    res[i].append(1) # since first and last values of a pascal row are always 1
                else:
                    '''
                    res[i-1][j-1] gives above row(i-1) prev col(j-1) and cur col(j) which is what
                    normally done in pascal
                    '''
                    res[i].append(res[i-1][j-1] + res[i-1][j])
        return res

	def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        pascal = [1]
        for row in xrange(numRows-1):
            cur_row = []
            for i, j in zip(xrange(len(pascal), xrange(1, len(pascal)))):
                cur_row = pascal[-1][i] + pascal[-1][j]
            pascal.append([1] + cur_row + [1])
        return pascal


    def kth_row_pascal(self, k):
        # Time: O(n^2)	
        '''
        Using the same logic as above but only using O(k) space and O(K^2) time
        '''
        res = [0 for _ in xrange(rowIndex+1)]
        for i in xrange(rowIndex+1):
            temp = [0 for _ in xrange(i+1)]
            for j in xrange(i+1):
                if j in [0, i]:
                    temp[j] = 1
                else:
                    temp[j] = res[j-1] + res[j]
            res = temp
        return res

if __name__ == '__main__':
    test_cases = [
        (5, [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]),
    ]
    for test_case in test_cases:
        res = Solution().pascal_triangle(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
