import pytest

class Solution():
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums[0], -1]
        stack = []
        next_greater_eles = []
        num_nextGreater_map = {}
        for num in nums:
            while stack and num > stack[-1]:
                num_nextGreater_map[stack.pop()] = num
            stack.append(num)
        for num in findNums:
        	next_greater_eles.append(num_nextGreater_map.get(num, -1))
        return next_greater_eles

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (([4,1,2], [1,3,4,2]), [-1, 3, -1]),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.nextGreaterElement(*args) == result
