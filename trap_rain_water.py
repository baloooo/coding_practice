"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
Idea is to traverse every array element and find the highest bars on left and right sides. Take the smaller of two heights. The difference between smaller height and height of current element is the amount of water that can be stored in this array element.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        Idea: https://www.youtube.com/watch?v=KV-Eq3wYjxI
        Abstract: "For each bar" calculate what is the max amount of water it can hold.
        The amount of water each bar can hold over itself is defined by
        max height bar on the left and max height bar on the right
        and that is min(left_max, right_max) - cur_bar_height
        And then just move the minimum bar ahead
        Implementation: https://discuss.leetcode.com/topic/3016/share-my-short-solution
        """
        max_water, left_max, right_max, start, end = 0, 0, 0, 0, len(height)-1
        '''
        start and end are the target bars depending on which one is in consideration which
        depends on which one is smaller out of left_max and right_max. As the smaller of
        the left and right maxes will determine the amount of water over any particular
        bar. Notice if we had left_max and right_max arrays populated we could have just
        iterated from start to end but since we wanted it to be done without extra space
        just keep following the smaller of left_max/right_max and move start/end accordingly.
        '''
        while start < end:
            left_max = max(left_max, height[start])
            right_max = max(right_max, height[end])
            if left_max < right_max:
                max_water += (left_max - height[start])
                start += 1
            else:
                max_water += (right_max-height[end])
                end -= 1
        return max_water
        
