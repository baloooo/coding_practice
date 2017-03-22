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
    def __init__(self):
        self.ways_to_climb_map = {}

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
    num_of_stairs = 5
    sol = Solution()
    print sol.ways_to_climb_stairs(num_of_stairs)
    import ipdb
    ipdb.set_trace()
