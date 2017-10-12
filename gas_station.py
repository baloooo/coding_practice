# coding: utf-8
"""
There are N gas stations along a circular route, where the amount of gas at
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to
travel from station i to its next station (i+1). You begin the journey with
an empty tank at one of the gas stations.

Return the minimum starting gas station’s index if you can travel around the
circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
Completing the circuit means starting at i and ending up at i again.

Example :

Input :
    Gas :   [1, 2]
    Cost :  [2, 1]

    Output : 1

If you start from index 0, you can fill in gas[0] = 1 amount of gas.
Now your tank has 1 unit of gas. But you need cost[0] = 2 gas to travel to
station 1.
If you start from index 1, you can fill in gas[1] = 2 amount of gas.
Now your tank has 2 units of gas. You need cost[1] = 1 gas to get to station 0.
So, you travel to station 0 and still have 1 unit of gas left over.
You fill in gas[0] = 1 unit of additional gas, making your current gas = 2.
It costs you cost[0] = 2 to get to station 1, which you do and complete the
circuit.
"""


class Solution:
    def __init__(self):
        pass

    def gas_station_route_possible_optimized(self, gas_arr, cost_arr):
        """
        https://discuss.leetcode.com/topic/1344/share-some-of-my-ideas
        Idea:
        1. If car starts at A and can not reach B. Any station between A and B
           can not reach B.(B is the first station that A can not reach.)
        2. If the total number of gas is bigger than the total number of cost.
           There must be a solution.
        """
        start, total_deficency, tank = 0, 0, 0
        # total_deficency is the total amount of fuel we're short of when we reach the last station
        for i in xrange(len(gas_arr)):
            tank += gas_arr[i] - cost_arr[i]
            if tank < 0:
                start = i + 1
                # This accumulates all the deficiency in the gas till reset point  # noqa
                total_deficency += tank
                tank = 0
        # Can total(deficiencies till last reset point) +
        # tank (existing gas in tank) be greater than equal to zero i.e possible to cover.  # noqa
        return -1 if (total_deficency + tank) < 0 else start

    def gas_station_route_possible(self, gas_arr, cost_arr):
        # Time: O(n^2) Space: O(1)
        # Total Gas should be greater than total cost
        if sum(gas_arr) < sum(cost_arr):
            return -1
        for index in xrange(len(gas_arr)):
            cur_gas = 0
            cur_gas = gas_arr[index] - cost_arr[index]
            cur_index = index+1
            if cur_gas < 0:
                continue
            while(cur_index % len(gas_arr) != index):
                cur_gas += gas_arr[cur_index % len(gas_arr)] - cost_arr[cur_index % len(gas_arr)]  # noqa
                cur_index = cur_index+1
                if cur_gas < 0:
                    break
            else:
                return index
        return -1

if __name__ == '__main__':
    # gas_arr, cost_arr = [1, 2], [2, 1]
    # gas_arr, cost_arr = [2, 4], [3, 4]
    gas_arr, cost_arr = [4], [5]
    print Solution().gas_station_route_possible(gas_arr, cost_arr)
