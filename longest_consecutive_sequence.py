https://leetcode.com/problems/longest-consecutive-sequence/solution/
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        There're two key ideas, one that we can use set instead of list for nums.
        Second and major one is that we only want to start a streak search for numbers that don't have
        a number less than them in nums_set. This guarantees for a sequence [100, 4, 200, 1, 3, 2] we only
        iterate with 100, 200 and 1 and two of these will end soon since they don't have a sequence and 1 will
        follow thru to cover all of it's sequence.
        """
        if not nums: return 0
        nums_set = set(nums)
        max_streak = 1
        for num in nums_set:
            if num-1 not in nums_set:
                cur_streak = 1
                
                while num + 1 in nums_set:
                    num = num + 1
                    cur_streak  += 1
                
                max_streak = max(cur_streak, max_streak)
        return max_streak
