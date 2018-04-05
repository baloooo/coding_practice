"""
orbuluh: https://discuss.leetcode.com/topic/7599/o-n-stack-based-java-solution/24
Idea: http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
http://www.informatik.uni-ulm.de/acm/Locals/2003/html/judge.html
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, max_area = [], 0
        heights.append(0)  # To empty the stack by the end of the day.
        for index, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                """
                From leetcode link above: Since in the stack, we are maintaining
                a increasing height in the stack, every time we check a bar that
                is right bounded by h, will also be left bounded by the height
                that is previous stored in the stack. So the width would go from
                stack[-1] + 1 to i - 1 included, which is i - stack[-1] - 1
                """
                w = index - stack[-1] - 1 if stack else index  # Note: check if stack is not empty
                max_area = max(max_area, h*w)
            stack.append(index)  # Notice: We're appending indexes and not values.
        return max_area
