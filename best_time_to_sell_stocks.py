

class Solution:
    def __init__(self):
        pass

    def best_time_to_sell_stocks_advanced(self, stock_report):
        pass

    def best_time_to_sell_stocks_intermediate(self, stock_report):
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
        """
        total_worth = 0
        for cur_day in xrange(1, len(stock_report)):
            if stock_report[cur_day] > stock_report[cur_day-1]:
                total_worth += stock_report[cur_day] - stock_report[cur_day-1]
        return total_worth

    def best_time_to_sell_stocks_basic(self, stock_report):
        """
        Say you have an array for which the ith element is the price of a given
        stock on day i.

        If you were only permitted to complete at most one transaction
        (ie, buy one and sell one share of the stock), design an algorithm to
        find the maximum profit.

        Example 1:
        Input: [7, 1, 5, 3, 6, 4]
        Output: 5

        max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be
        larger than buying price)
        Example 2:
        Input: [7, 6, 4, 3, 1]
        Output: 0

        In this case, no transaction is done, i.e. max profit = 0.
        """
        cur_min = float('inf')
        max_difference = 0
        for cur_stock in stock_report:
            if cur_stock < cur_min:
                cur_min = cur_stock
                continue
            cur_difference = cur_stock - cur_min
            if cur_difference > max_difference:
                max_difference = cur_difference
        return max_difference

if __name__ == '__main__':
    stock_report = [100, 180, 260, 310, 40, 535, 695]
    stock_report = [200, 100, 50, 10]
    stock_report = [200, 100]
    print Solution().best_time_to_sell_stocks_basic(stock_report)
