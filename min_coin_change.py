'''
min_coin_change: https://leetcode.com/articles/coin-change/
'''

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
        '''
        Time: O(S**n) where S=target_sum and n = len(coins)
        S/c1 * S/c2 * ...S/cn = (S**n)/cn
        S/c1 is the total number of ways we can use c1 to contribute in a combination that makes up total_sum
        '''
        min_coins = self.count(coins, 0, target_sum)
        print 'min coins are', min_coins
        return min_coins if min_coins else -1
    '''
    Don't know (for now atleast) how this is more efficient or better than recursive one.
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
    '''
    def min_coin_change(self, coins, amount):
        """
        You may assume that you have an infinite number of each kind of coin.
        Time: O(S*N) where S=amount and N = len(coins)
        """
        # dp=[min_coins_needed_to_make_cur_index_amount]
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for cur_amount in xrange(1, amount+1):
            for cur_coin in coins:
                # If we can make cur_amount with current coin
                if cur_coin <= cur_amount:
                    # minimum of already calculated min_coins_needed for this amount from prev. coins and
                    # number of min coins needed if we supply one current denomination coin thereby subtracting it's cost/amount
                    # from the total amount.
                    dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - cur_coin] + 1)
        return dp[amount] if dp[amount] != MAX else -1

    def coin_change2(self, coins, amount):
        '''
        This implementation is just to demonstrate this doesn't work. For correct implementation
        check count_dp_optimized in way_to_coin_change.py
        # swapping loops for amount and coin doesn't work for number of ways but does work for min coins.(perhaps)
        # explanation: https://discuss.leetcode.com/topic/78798/7-lines-simple-java-dp-solution/4
        '''
        dp = [1] + [0]*amount
        for cur_amount in xrange(1, amount+1):
            for coin in coins:
                if coin <= cur_amount:
                    dp[cur_amount] += dp[cur_amount-coin]
        print dp
        return dp[-1]

if __name__ == '__main__':
    # coins, amount = [186, 419, 83, 408], 6249
    # print Solution().min_coin_change(coins, amount)
    # coins, amount = [1, 2, 3], 4
    coins, amount = [1, 2, 5], 5
    print Solution().coin_change2(coins, amount)
    # sol = Solution()
    # print sol.make_change(coins, amount)
    # print sol.memo
    # print Solution().min_coin_change(coins, amount)
    # print Solution().min_coin_change_recursive(coins, amount)
