

class Solution:
    def __init__(self):
        pass

    def best_time_to_sell_stocks_advanced(self, stock_report):
        pass

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
        for index in xrange(1, len(prices)):
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
