'''
This exercise is very similar to combinational sum, just replaced addition operation with
mulitplication.
'''

class Solution(object):
    def backtrack(self, n, start, cur, res):
        if n == 1:
            if len(cur) != 1:
                res.append(cur[:])
            return
        for i in xrange(start, n+1):
            if n % i == 0:
                cur.append(i)
                self.backtrack(n/i, i, cur, res)
                cur.pop()
                
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
	The same solution for java gets accepted, python can't pass last one test case.
    https://leetcode.com/problems/factor-combinations/discuss/68040/My-Recursive-DFS-Java-Solution

	Time & space:
	https://github.com/kamyu104/LeetCode/blob/master/Python/factor-combinations.py
        """
        res = []
        if n == 1: return []
        self.backtrack(n, 2, [], res)
        return res

if __name__ == '__main__':
    print Solution().getFactors(12)
