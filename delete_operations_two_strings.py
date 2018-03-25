class Solution(object):
    def min_distance(self, word1, i, word2, j):
        if i == len(word1):
            return len(word2) - j
        elif j == len(word2):
            return len(word1) - i

        if word1[i] == word2[j]:
            return self.min_distance(word1, i+1, word2, j+1)
        else:
            return 1 + min(self.min_distance(word1, i+1, word2, j), self.min_distance(word1, i, word2, j+1))

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
	Time: O(2^m), similar to edit distance without the replace part
        """
        return self.min_distance(word1, 0, word2, 0)

    def minDistance_dp(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
	Time: O(mn), space: O(mn)
	https://leetcode.com/articles/delete-operation-for-two-strings/
        """
        dp = [[0 for _ in xrange(len(word1)+1)] for _ in xrange(len(word2)+1)]
        
        for i in xrange(len(word2)+1):
            for j in xrange(len(word1)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[len(word2)][len(word1)]
