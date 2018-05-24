'''

https://leetcode.com/problems/rectangle-area/discuss/62138/My-Java-solution-Sum-of-areas-Overlapped-area
'''


class Solution(object):
    def computeArea(self, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        box1_area = (x2 - x1) * (y2 - y1)
        box2_area = (x4  - x3) * (y4 - y3)

        left = max(x1, x3)
        right = min(x2, x4)
        top = min(y2, y4)
        bottom = max(y1, y3)

        overlapped_area = 0

        if left  < right and top > bottom:
            overlapped_area = (right - left) * (top - bottom)

        return box1_area + box2_area - overlapped_area
