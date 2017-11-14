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

    def kth_row_pascal(self, k):
        # Time: O(n^2)
        # Idea: https://github.com/kamyu104/LeetCode/blob/master/Python/pascals-triangle-ii.py
        pass

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
