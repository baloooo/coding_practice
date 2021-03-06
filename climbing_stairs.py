"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]
"""


class Solution:
    '''
    Idea: http://www.geeksforgeeks.org/count-ways-reach-nth-stair/
    '''
    def __init__(self):
        self.ways_to_climb_map = {}

    def climb_stairs2(self, n):
        # Like Fibonacci https://discuss.leetcode.com/topic/5371/basically-it-s-a-fibonacci  # noqa
        # Space: O(1)
        if n <= 2:
            return n
        dp_prev_prev, dp_prev = 1, 2
        dp_cur = 0
        for i in xrange(2, n):
            dp_cur = dp_prev + dp_prev_prev
            dp_prev, dp_prev_prev = dp_cur, dp_prev
        return dp_cur

    def climb_stairs(self, n):
        # Like Fibonacci https://discuss.leetcode.com/topic/5371/basically-it-s-a-fibonacci  # noqa
        # Time: O(n) Space: O(n)
        if n <= 2:
            return n
        # Note: The size of dp array is n here since we get no. of ways we can reach nth stair on position n-1 of the array.
        dp = [0]*(n)
        dp[0], dp[1] = 1, 2
        for i in xrange(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

    def ways_to_climb_stairs(self, num_of_stairs):
        # ways(n) = ways(n-1) + ways(n-2)
        if num_of_stairs == 1:
            return 1
        if num_of_stairs == 2:
            return 2
        if self.ways_to_climb_map.get(num_of_stairs-2):
            num_ways_two = self.ways_to_climb_map[num_of_stairs-2]
        else:
            num_ways_two = self.ways_to_climb_stairs(num_of_stairs-2)
            self.ways_to_climb_map[num_of_stairs-2] = num_ways_two
        if self.ways_to_climb_map.get(num_of_stairs-1):
            num_ways_one = self.ways_to_climb_map[num_of_stairs-1]
        else:
            num_ways_one = self.ways_to_climb_stairs(num_of_stairs-1)
            self.ways_to_climb_map[num_of_stairs-1] = num_ways_one
        return num_ways_one + num_ways_two

if __name__ == '__main__':
    num_of_stairs = 4
    sol = Solution()
    # print sol.ways_to_climb_stairs(num_of_stairs)
    print sol.climb_stairs(num_of_stairs)
    print sol.climb_stairs2(num_of_stairs)
