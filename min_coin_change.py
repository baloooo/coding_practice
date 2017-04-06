"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    def __init__(self):
        pass

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        cur_sum = 0
        denom_count = 0
        while cur_sum != amount and coins:
            if cur_sum+coins[-1]<=amount:
                cur_sum += coins[-1]
                denom_count += 1
            else:
                coins.pop()
        if cur_sum == amount:
            return denom_count
        else:

            import ipdb; ipdb.set_trace()
            return -1
        

if __name__ == '__main__':
    coins, amount = [186, 419, 83, 408], 6249
    print Solution().coinChange(coins, amount)
