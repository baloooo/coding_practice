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
