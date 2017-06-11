
class Solution:

    def __init__(self):
        # memoization map: {sum-denomination: #of ways}
        self.memo = {}

    def count(self, coins, index, target_sum):
        if index >= len(coins):
            return 0
        if target_sum == 0:
            return 1
        if target_sum < 0:
            return 0
        return min(self.count(coins, index+1, target_sum),
                   1 + self.count(coins, index, target_sum-coins[index]))

    def min_coin_change_recursive(self, coins, target_sum):
        min_coins = self.count(coins, 0, target_sum)
        print 'min coins are', min_coins
        return min_coins if min_coins else -1

    def make_change(self, coins, amount):
        return self.total_ways_to_coin_change(coins, amount, 0)

    def total_ways_to_coin_change(self, coins, amount, index):
        """
        rather than making copy of coins on each recursion level, it's better
        to use index to mark the start of array
        """
        if amount == 0:
            return 1
        if index >= len(coins):
            return 0
        try:
            return self.memo['%s-%s' % (amount, coins[index:])]
        except KeyError:
            total_ways = (
                self.total_ways_to_coin_change(
                    coins, amount-coins[index], index) +
                self.total_ways_to_coin_change(coins, amount, index+1))
            self.memo['%s-%s' % (amount, coins[index:])] = total_ways
            return total_ways

    def min_coin_change(self, coins, amount):
        """
        You are given coins of different denominations and a total amount of
        money amount. Write a function to compute the fewest number of coins
        that you need to make up that amount. If that amount of money cannot
        be made up by any combination of the coins, return -1.

        Example 1:
        coins = [1, 2, 5], amount = 11
        return 3 (11 = 5 + 5 + 1)

        Example 2:
        coins = [2], amount = 3
        return -1.

        Note:
        You may assume that you have an infinite number of each kind of coin.
        """
        # dp=[min_coins_needed_to_make_cur_index_amount]
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for cur_amount in xrange(1, amount+1):
            for cur_coin in xrange(len(coins)):
                # If we can make cur_amount with current coin
                if coins[cur_coin] <= cur_amount:
                    dp[cur_amount] = min(
                        dp[cur_amount], dp[cur_amount-coins[cur_coin]]+1)
        return dp[amount] if dp[amount] != MAX else -1

if __name__ == '__main__':
    # coins, amount = [186, 419, 83, 408], 6249
    # print Solution().min_coin_change(coins, amount)
    coins, amount = [1, 2, 3], 4
    # sol = Solution()
    # print sol.make_change(coins, amount)
    # print sol.memo
    # print Solution().min_coin_change(coins, amount)
    print Solution().min_coin_change_recursive(coins, amount)
