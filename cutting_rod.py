'''
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
'''


class Solution:
    def cut_rod(self, prices):
        # Time: O(n^2), without DP: 2^n
        # Idea: https://www.youtube.com/watch?v=ElFrskby_7M
	dp = [0]*(len(prices)+1) # dp[i] is the optimal price for the rod up to length i
	for i in xrange(len(prices)+1):
            for k in xrange(1, i+1):
                dp[i] = max(dp[i], prices[k - 1] + dp[i - k])
        return dp[len(prices)]

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 8, 9, 10, 17, 17, 20], 22),
        ([3, 5, 8, 9, 10, 17, 17, 20], 24),
    ]
    for test_case in test_cases:
        res = Solution().cut_rod(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
