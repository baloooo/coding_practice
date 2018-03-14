import pytest

class Solution():
    def move_zeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Time: O(n), Space: O(1)
        https://leetcode.com/problems/move-zeroes/solution/
        """
        last_non_zero_found_at = 0
        for cur in xrange(len(arr)):
            if arr[cur] != 0:
                arr[last_non_zero_found_at], arr[cur] = arr[cur], arr[last_non_zero_found_at]
                last_non_zero_found_at += 1

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
