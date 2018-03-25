# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
"""
def search(nums, target):
    '''
    Idea: https://discuss.leetcode.com/topic/16580/java-ac-solution-using-once-binary-search
    '''
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        # equal sign to accomodate when array len is 1
        mid = lo + (hi-lo)/2
        if nums[mid] == target:
            return mid
        '''
        If lo to mid is sorted and target is in b/w lo to mid OR
        lo to mid has rotation and target NOT in mid to hi range.
        Note: take care of < and <= and for opposite sign
        '''
        # target strictly to the left, strictly as hi doesn't rest at mid but mid - 1
        if ((nums[lo] <= nums[mid] and nums[lo] <= target <= nums[mid])
            # OR target not in strictly right
            or (nums[lo] > nums[mid] and not(nums[mid] < target <= nums[hi]))):
                hi = mid - 1 # go left
        else:
            lo = mid + 1  # go right
    return -1

def search_w_repetitions(nums, target):
    '''
    Idea: The logic is entirely the same as above, just remove the repetitions/duplicates
    https://discuss.leetcode.com/topic/19116/easy-c-solution-based-on-version-i-of-the-problem
    '''
    lo, hi = 0, len(nums)-1
    while lo <= hi:

        # remove duplicates
        while lo < hi and nums[lo] == nums[lo+1]: lo+=1
        while hi > lo and nums[hi] == nums[hi-1]: hi-=1

        mid = lo + (hi-lo)/2
        if nums[mid] == target: return True
        if ((nums[lo] <= nums[mid] and nums[lo] <= target < nums[mid])
            or (nums[lo] > nums[mid] and not(nums[mid]<target<=nums[hi]))):
            hi = mid - 1
        else:
            lo = mid + 1
        return False


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    # arr = [int(x) for x in inp.split(' ')]
    arr = [3, 1]
    n = len(arr) - 1
    print search(arr, 2)
