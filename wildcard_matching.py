'''
We define the state P[i][j] to be whether s[0..i) matches p[0..j). The state equations are as follows:

P[i][j] = P[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '?'), if p[j - 1] != '*';
P[i][j] = P[i][j - 1] || P[i - 1][j], if p[j - 1] == '*'.

Equation 1). means that if p[j-1] is not *, f(i,j) is determined
by if s[0:i-2] matches p[0:j-2] and if (s[i-1]==p[j-1] or
p[j-1]=='?').

Equation 2). means that if p[j-1] is *, f(i,j) is true if either
f(i,j-1) is true: s[0:i-1] matches p[0:j-2] and * is not used
here; or f(i-1,j) is true: s[0:i-2] matches p[0:j-1] and * is
used to match s[i-1].
'''
class Solution(object):
    def isMatch(self, text, pattern):
        """
	Idea: http://www.geeksforgeeks.org/wildcard-pattern-matching/
	Time:  O(m x n).
	Space: O(m x n).
        For details on cur impl. and further improvement.
        https://discuss.leetcode.com/topic/17901/accepted-c-dp-solution-with-a-trick
        """
        if len(pattern) == 0:
            return len(text) == 0
        dp = [[False for _ in xrange(len(pattern)+1)] for _ in xrange(len(text)+1)]
        
        dp[0][0] = True
    
        for j in xrange(1, len(pattern)+1):
            if pattern[j-1] == '*':
                dp[0][j] = dp[0][j-1]
            
        for i in xrange(1, len(text)+1):
            for j in xrange(1,len(pattern)+1):
                if pattern[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif pattern[j-1] == '?' or text[i-1] == pattern[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return dp[len(text)][len(pattern)]
    def is_match_optimized(self, text, pattern):
	'''
	Time: O(m+n)
	Space: O(1)
	https://github.com/kamyu104/LeetCode/blob/master/Python/wildcard-matching.py
	https://discuss.leetcode.com/topic/3040/linear-runtime-and-constant-space-solution/78
	'''
	pass
