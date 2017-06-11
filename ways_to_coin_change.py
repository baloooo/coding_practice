"""
https://discuss.leetcode.com/topic/79071/knapsack-problem-java-solution-with-thinking-process-o-nm-time-and-o-m-space
"""

class Solution:
    def __init__(self):
        pass

    def ways_to_coin_change(self, coins, total_sum):
        total_ways = self.count(coins, 0, total_sum)
        print 'total_ways using just recursion', total_ways
        total_ways = self.count_dp(coins, total_sum)
        print 'total_ways using DP', total_ways
        total_ways = self.count_dp_optimized(coins, total_sum)
        return total_ways if total_ways else -1

    def count_dp(self, coins, total_sum):
        dp = [[0 for _ in xrange(total_sum+1)] for _ in xrange(len(coins)+1)]  # noqa
        dp[0][0] = 1
        """
        dp[i][j] : the number of combinations to make up total_sum j by using
                   the first i types of coins
        State transition:
            Case 1: not using the ith coin, only using the first i-1 coins to
            make up total_sum j, then we have dp[i-1][j] ways.
            Case 2: using the ith coin, since we can use unlimited same coin,
            we need to know how many way to make up total_sum j - coins[i] by
            using first i coins(including ith), which is dp[i][j-coins[i]]
            Notice: we only go for using all coins upuntill last coin from
            cur_pos if that coin's value is greater than equal to the cur_sum
            since if we can't make cur_sum with all the coins up untill last
            coin we can't do anything with last coin and using current one with
            it.
        Initialization: dp[i][0] = 1
        m = len(coins), n = total_sum
        Space: O(m*n)
        Time: O(m*n)
        """
        for cur_coin in xrange(1, len(coins)+1):
            dp[cur_coin][0] = 1
            for cur_sum in xrange(1, total_sum+1):
                for row in xrange(len(dp)):
                    for col in xrange(len(dp[0])):
                        print dp[row][col],
                    print
                print '-'*10
                dp[cur_coin][cur_sum] = (
                    dp[cur_coin-1][cur_sum] +
                    (dp[cur_coin][cur_sum-coins[cur_coin-1]] if
                        cur_sum >= coins[cur_coin-1] else 0))
            # notice 'cur_coin-1' here since indexes start from 1
            # dp[cur_coin-1] means last row, but coins[cur_coin-1] means cur coin
            # with indexing on an array which is zero based
        return dp[len(coins)][total_sum]

    def count_dp_optimized(self, coins, total_sum):
        """
        Optimizes on space
        m = len(coins), n = total_sum
        Space: O(total_sum)
        Time: O(m*n)
        """
        dp = [1] + [0]*total_sum
        for cur_coin in coins:
            for cur_sum in xrange(cur_coin, total_sum+1):
                dp[cur_sum] += dp[cur_sum-cur_coin]
        return dp[-1]

    def count_recursive(self, coins, index, total_sum):
        # no more coins left
        if index == len(coins):
            return 0
        # target sum acheived
        if total_sum == 0:
            return 1
        # adding this coin surpasses target sum, so don't include
        if total_sum < 0:
            return 0
        return (self.count(coins, index+1, total_sum) +
                self.count(coins, index, total_sum-coins[index]))

if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3], 4), 4),
        # (([2, 5, 3, 6], 10), 5),
        # (([1, 101, 102, 103], 100), 1),
        # (([3, 5, 7, 8, 9, 10, 11], 500), 50),
    ]
    for test_case in test_cases:
        res = Solution().ways_to_coin_change(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
