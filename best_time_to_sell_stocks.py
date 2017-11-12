

class Solution:
    def __init__(self):
        pass

    def best_time_to_sell_stocks_k(self, prices, k):
        '''
        Time: O(k.n^2)
        Idea: https://www.youtube.com/watch?v=oDhu5uGq_ic
        http://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/

        i(rows) -> transaction,
        j(cols) -> day
        profit[i][j] = max(profit[i][j-1], # no transaction on jth day.
                      price[j] - price[m] + profit[i-1][m] {for m = 0 ... j-1})
                      # best you can get by completing a transaction on jth day
        '''
        '''
        table to store results of subproblems profit[i][j] stores maximum profit using
        atmost i transactions up to day j (including day j)
        '''
        if not prices or not k: return 0
        # Notice that we add zero'th transaction row 
        profit = [[0 for _ in xrange(len(prices)] for _ in xrange(k+1)]
        # For day 0, you can't earn money irrespective of how many times you trade, since you need atleast
        # two days for one transaction, one to buy on and one to sell
        for row in xrange(k+1):
            profit[row][0] = 0
        # profit is 0, if we don't do any transactions, i.e k = 0
        for day in xrange(len(prices)):
            profit[0][day] = 0

        for i in xrange(k+1):
            for j in xrange(len(prices)):
                max_so_far = -float('inf')
                for m in xrange(j):
                    max_so_far = max(max_so_far, prices[j] - prices[m] + profit[i-1][m])
                profit[i][j] = max(profit[i][j-1], max_so_far)
        return profit[k][len(prices)-1]

    def best_time_to_sell_stocks_k_optimized(self, prices, k):
        '''
        One mathemetical optimization (vid: 13:50)
        '''
        if not prices or not k: return 0
        profit = [[0 for _ in xrange(len(prices))] for _ in xrange(k+1)]
        for col in xrange(len(prices)):
            profit[0][col] = 0
        for row in xrange(k+1):
            profit[row][0] = 0
        for i in xrange(1, k+1):
            for j in xrange(1, len(prices)):
                prev_diff = max(prev_diff, profit[i-1][j-1] - price[j-1])
                profit[i][j] = max(profit[i][j-1], price[j] + prev_diff)
        return profit[k][len(prices)-1]


    def best_time_to_sell_stocks_2(self, stock_report):
        """
        Say you have an array for which the ith element is the price of a given
        stock on day i.

        Design an algorithm to find the maximum profit. You may complete as
        many transactions as you like (ie, buy one and sell one share of the
        stock multiple times). However, you may not engage in multiple
        transactions at the same time (ie, you must sell the stock before you
        buy again).

        Example :

        Input : [1 2 3]
        Return : 2
        Idea:
        Basically, if tomorrow's price is higher than today's, we buy it today
        and sell tomorrow. Otherwise, we don't. Here is the code:
        Idea: https://leetcode.com/articles/best-time-buy-and-sell-stock-ii/
        The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.
        instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. In the end,we will be using the peaks and valleys effectively, but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit. 
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i - 1] < prices[i]: # valley --> peak encountered
                max_profit += prices[i - 1] + prices[i]
        return max_profit

    def best_time_to_sell_stocks_1(self, stock_report):
        """
        Preferred: https://leetcode.com/articles/best-time-buy-and-sell-stock/
        alternative: Idea: https://discuss.leetcode.com/topic/5863/sharing-my-simple-and-clear-c-solution/20
        """
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
            # or can be more precisely written as (but for clarity left as above)
            # max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == '__main__':
    stock_report = [100, 180, 260, 310, 40, 535, 695]
    stock_report = [200, 100, 50, 10]
    stock_report = [200, 100]
    print Solution().best_time_to_sell_stocks_basic(stock_report)
