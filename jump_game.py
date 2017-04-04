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
    def __init__(self):
        pass

    def min_jumps_to_end(self, arr):
        """
        https://discuss.leetcode.com/topic/3191/o-n-bfs-solution/4
        """
        pass

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
        """
        reachable = 0
        for cur_index, jump_length in enumerate(arr):
            if cur_index > reachable:
                return False
            if reachable == len(arr) - 1:
                return True
            reachable = max(reachable, cur_index + jump_length)
        return True


if __name__ == '__main__':
    test_cases = [
        ([2, 3, 1, 1, 4],  True),
        ([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6], False),  # noqa
        ([1, 1, 1], True),
    ]
    for test_case in test_cases:
        result = Solution().can_jump_to_end(test_case[0])
        if result == test_case[1]:
            print "PASSED"
        else:
            print "Failed: Test case {0}, expected {1} got {2}".format(
                test_case[0], test_case[1], result)
    # print Solution().min_jumps_to_end(arr)
