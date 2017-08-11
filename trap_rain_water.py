"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
Idea is to traverse every array element and find the highest bars on left and right sides. Take the smaller of two heights. The difference between smaller height and height of current element is the amount of water that can be stored in this array element.
"""
class Solution(object):
    def trap(self, heights):
        """
        Idea: As lower wall defines the amount of water that can be stored over
            a building, keep moving the lower wall whichever it is from left or right.
        """
        
