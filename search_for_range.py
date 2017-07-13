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
    def last_occurrence(self, arr, x): 
        n = len(arr)
        start = 0 
        end = n-1 
        while(start<end):
            mid = start + (end-start)/2
            if arr[mid] == x:
                if mid+1<n and arr[mid+1] == x:
                    start = mid+1
                    continue
                return mid 
            if arr[mid] < x:
                start = mid+1
            else:
                end = mid-1
        if arr[start] == x:
            return start
        else:
            return -1
            
    def first_occurrence(self, arr, x):
        n = len(arr)
        start = 0
        end = n-1
        while(start<end):
            # To avoid overflow
            mid = start + (end-start)/2
            if arr[mid] == x:
                if mid-1>=0 and arr[mid-1] == x:
                    end = mid-1
                    continue
                return mid
            if arr[mid] < x:
                start = mid+1
            else:
                end = mid-1
        if arr[start] == x:
            return start
        else:
            return -1

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        """
        alternate soln = https://discuss.leetcode.com/topic/16486/9-11-lines-o-log-n
        """
        lptr = self.first_occurrence(A, B)
        if lptr == -1:
            return [-1, -1]
        rptr = self.last_occurrence(A, B)
        return [lptr, rptr]
