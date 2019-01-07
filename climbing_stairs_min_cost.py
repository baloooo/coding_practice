# coding: utf-8
'''
https://leetcode.com/problems/min-cost-climbing-stairs/discuss/110111/Easy-to-understand-C++-using-DP-with-detailed-explanation
'''

import pytest

class Solution():
    def min_cost_climbing_stairs(self, cost):
		'''
		Time: O(n) Space: O(1)
		'''
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        # dp[i] = cost(i) + min(dp[i-1], dp[i-2])
        dp = [0 for _ in xrange(len(cost))]
        dp[0], dp[1] = cost[0], cost[1]
        for i in xrange(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
		# since you can jump either one step or 2 from the last/second_last step.
        return min(dp[len(cost)-1], dp[len(cost)-2])

	def min_cost_climbing_stairs_optimized(self, cost):
		'''
		Time: O(n) Space: O(1)
		'''
		if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        else:
            second_last, last = cost[0], cost[1]
            for i in xrange(2, len(cost)):
                cur = cost[i] + min(last, second_last)
                second_last = last
                last = cur
            return min(last, second_last)


class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ([10, 20], 30),
        ([30, 40], 70),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.task(*args) == result
