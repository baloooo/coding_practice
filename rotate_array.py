class Solution(object):
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
		https://leetcode.com/problems/rotate-array/solution/
        """
        k = k % len(arr) # ignore redundant iterations
        self.reverse(arr, 0, len(arr)-1)
        self.reverse(arr, 0, k-1)
        self.reverse(arr, k, len(arr)-1)
