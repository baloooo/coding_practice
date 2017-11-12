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
    # For a rod of length 8 there are 128(2^(n-1)) ways to cut it.
    def cut_rod_recursion(self, prices, n): # n=length of rod
        '''
        Time: 2^n, Space: O(n) stack depth
        when you try to visualize how this executes you'll get to know how this generates all possible
        combinations
        '''
        if n <= 0: return 0
        max_profit = -float('inf')
        for i in xrange(n):
            max_profit = max(max_profit, prices[i] + self.cut_rod_recursion(prices, n-i-1))
        return max_profit

    def cut_rod_dp_td(self, prices, n, dp):
        # Top down https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture12.pdf
        # Time: O(n^2) Space: O(n + log(n)) {dp, and call stack respectively}
        if dp[n] >= 0:
            return dp[n]
        if n == 0:
            max_profit = 0
        else:
            max_profit = -float('inf')
            for i in xrange(n):
                max_profit = max(max_profit, prices[i] + self.cut_rod_dp(prices, n-i-1, dp))
        dp[n] = max_profit
        return dp[n]

    def cut_rod_dp_bu_optimized(self, prices):
        '''
        Time: O(n^2) Space: O(n)
        Bottom up https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture12.pdf
        https://www.youtube.com/watch?v=IRwVmTmN6go
        Preferred since doesn't needs call stack as in Top down approach
        '''
        dp = [0]*(len(prices)+1)
        for i in xrange(1, len(prices)+1):
            max_profit = -float('inf')
            for j in xrange(1, i):
                max_profit = max(max_profit, prices[j] + dp[i-j])
            dp[i] = max_profit
        return dp[len(prices)]


    def cut_rod_dp1(self, prices):
        # Time: O(n^2), without DP: 2^n
        # Idea: https://www.youtube.com/watch?v=ElFrskby_7M
	dp = [0]*(len(prices)+1) # dp[i] is the optimal price for the rod up to length i
        '''
        C(i) is the price of the optimal cut of a rod up untill length i
        Vk is the price of the cut at length k
        C(i) = max(Vk, C(i-k)) where 1<=k<=i
        '''
	for i in xrange(len(prices)+1):
            for k in xrange(1, i+1):
                dp[i] = max(dp[i], prices[k - 1] + dp[i - k])
        return dp[len(prices)]


if __name__ == '__main__':
    test_cases = [
        ([1, 5, 8, 9, 10, 17, 17, 20], 22),
        ([3, 5, 8, 9, 10, 17, 17, 20], 24),
        ([3], 3),
    ]
    for test_case in test_cases:
        res = Solution().cut_rod_dp_bu_optimized(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
