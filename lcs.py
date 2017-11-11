

class Solution:
    def lcs(self, str1, str2):
        return self.lcs_recursive(str1, str2, len(str1)-1, len(str2)-1)

    def lcs_recursive(self, str1, str2, i, j):
        '''
        Idea: http://www.geeksforgeeks.org/longest-common-subsequence/
        Time: O(2^(max(i, j)))
        Space: O(max(i,j))
        '''
        if i == 0 or j == 0:
            return 0
        elif str1[i] == str2[j]:
            return 1 + self.lcs_recursive(str1, str2, i-1, j-1)
        else:
            return max(self.lcs_recursive(str1, str2, i, j-1), self.lcs_recursive(str1, str2, i-1, j))

    def lcs_dp(self, str1, str2):
        # Time = Space = O(mn)
        dp = [[None for _ in xrange(len(str2))] for _ in xrange(len(str1))]
        for i in xrange(len(str1)+1):
            for j in xrange(len(str2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(str1)][len(str2)]

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
