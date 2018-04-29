class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                cur_sum = nums[lo] + nums[hi]
                if cur_sum == target:
                    res.append([nums[lo], nums[hi], nums[i]])
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1
        return res
