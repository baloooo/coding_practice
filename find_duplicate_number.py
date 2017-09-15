'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution(object):
    def findDuplicate(self, arr):
        """
        Idea is same as the one used for finding cycle in linkedlists
        since duplicated number can be repeated our xor logic won't work therefore this
        """
        Note: Notice the starting values for start and slo
        slow = arr[0]
        fast = arr[arr[0]]
        while slow != fast:
            slow = arr[slow]     
            fast = arr[arr[fast]]
        fast = 0 
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow
