"""
Given a non-empty array containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both
subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def __init__(self):
        pass

    def canPartition(self, arr):
        """
        :type nums: List[int]
        :rtype: bool
        """


if __name__ == '__main__':
    arr = [1, 5, 11, 5]
    print Solution().canPartition(arr)
