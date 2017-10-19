class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        Idea: https://discuss.leetcode.com/topic/27844/ac-python-dp-solutioin-120ms-based-on-largest-rectangle-in-histogram
        """
        heights = [0] * (len(matrix[0]) + 1) # appends a zero so as to allow stack to be emptied
        max_area = 0
        for row in matrix:
            for i in xrange(len(matrix[0])): # don't use length of height array here
                heights[i] = heights[i] + 1 if row[i] == '1' else 0 # cumulative height for column pillars so to speak.
            stack = []
            for i in xrange(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i # Note: check if stack is not empty
                    max_area = max(max_area, h*w)
                stack.append(i)
        return max_area
