"""
Minimum number of jumps to reach end
Given an array of integers where each element represents the max number of
steps that can be made forward from that element. Write a function to
return the minimum number of jumps to reach the end of the array
(starting from the first element). If an element is 0, then cannot move through
that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3,
so can make at most 3 steps eg to 5 or 8 or 9.
"""


class Solution:
    """
    Both exercises are of Greedy type
    https://discuss.leetcode.com/topic/11761/easy-python-greedy-solution-with-explanation
    """
    def min_jumps_to_end(self, arr):
        cur_max_reach, last_max_reach = 0, 0
        jumps, cur_index = 0, 0
        while cur_max_reach < len(arr)-1:
            while cur_index <= last_max_reach:
                """
                Progress cur_index untill last known max reachable distance.
                """
                # Meanwhile keep updating cur_max_reach to be the index
                # furthest reachable untill last_max_reach point is encountered
                cur_max_reach = max(cur_max_reach, cur_index + arr[cur_index])
                cur_index += 1
            # This means you cannot go any further from this index as your max
            # span didn't extend from last known location.
            if last_max_reach == cur_max_reach:
                return -1
            # copy cur_max_reachable distance to last_max_reach and then
            # progress cur_index upto last_max_reach to find the max reachable
            # point.
            last_max_reach = cur_max_reach
            jumps += 1
        return jumps

    def can_jump_to_end(self, arr):
        """
        Easier version of min_jumps_to_end with just to tell if end is
        reachable
        Given an array of non-negative integers, you are initially positioned
        at the first index of the array.

        Each element in the array represents your maximum jump length at that
        position.

        Determine if you are able to reach the last index.
        A = [2,3,1,1,4], return true.

        A = [3,2,1,0,4], return false.
        Algo: The idea is to have a reachable variable that essentially is a
        yard stick to know what is the maximum index we can reach from any
        given index. And just the fact that you can reach a index is a measure
        that this is reachable using some jump at previous index and you can
        just add current index to current jump length to know max reach from
        current index.
        """
        reachable = 0
        for cur_index, jump_length in enumerate(arr):
            """
            max jump from any of the previous indexes cannot reach till
            this index so nothing moving forward (including this) is reachable
            """
            if cur_index > reachable:
                return False
            if reachable == len(arr) - 1:
                return True
            reachable = max(reachable, cur_index + jump_length)
        return True


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 1, 1, 1], 3),
        ([2, 3, 1, 1, 4],  2),
        ([2, 1],  1),
        ([1, 2],  1),
        ([0], 0),
        ([1, 4, 1, 1, 1, 7, 1, 2, 3], 3),
        ([1, 1, 1, 1], 3),
        # ([2, 3, 1, 1, 4],  True),
        # ([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], True),
        # ([3, 2, 1, 0, 4], False),
        # ([0], True),
        # ([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6], False),  # noqa
        # ([1, 1, 1], True),
    ]
    for test_case in test_cases:
        # result = Solution().can_jump_to_end(test_case[0])
        result = Solution().min_jumps_to_end(test_case[0])
        if result == test_case[1]:
            print "PASSED"
        else:
            print "Failed: Test case {0}, expected {1} got {2}".format(
                test_case[0], test_case[1], result)
    # print Solution().min_jumps_to_end(arr)
