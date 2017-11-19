# -*- coding: utf-8 -*-
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
"""
class Solution:
    def search_range(self, nums, target):
        '''
        code: https://discuss.leetcode.com/topic/16486/9-11-lines-o-log-n

        Article explanation: https://leetcode.com/articles/search-for-a-range/
        
        Here, search method is a simple binary search, telling us the first
        index where we could insert 'n' into nums to keep it sorted. Thus,
        if nums contains target, we'll return the first occurrence with search(target).
        we do that, and if target isn't actually there, then I return [-1, -1].
        Otherwise, I ask search(target+1), which tells me the first index where I
        could insert target+1, which of course is one index behind the last index containing
        target, so all I have left to do is subtract 1.
        '''
        def search(n):
            '''
            Also works for https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
            '''
            # This search method can as it is be used for search insert position logic
            lo, hi = 0, len(nums) # this should be len(nums) and not len(nums)-1 to deal w/ size 1 array.
            while lo < hi:
                mid = lo + (hi-lo)/2
                # we don't want to do if mid == target since we want the first occurrence not any occurrence
                if nums[mid] >= n:
                    # also since nums[mid] can be 'n' hi = mid but if this fails lo != mid so lo = mid+1
                    # This means "first" (not any)  occurrence of n will be b/w lo and mid if nums[mid]>=n
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
        '''
        return [lo, search(target+1)-1] if len(nums) and lo < len(nums) and target == nums[lo] else [-1, -1]
        nums[lo:lo+1] gives handles with above three conds stringed with 'AND'.

if __name__ == '__main__':
    arr, target = [5, 7, 7, 8, 8, 10], 8
    arr, target = [1], 1 # [0, 0]
    print Solution().search_range(arr, target)

	
