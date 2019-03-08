class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        Time : O(mn) For each row, height arr is calculated(O(n)) and then processed O(n) so O(m) * O(2n) = O(mn)
        Idea: https://discuss.leetcode.com/topic/27844/ac-python-dp-solutioin-120ms-based-on-largest-rectangle-in-histogram
        [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
[
  ["1","0","1","0","0"],
  ["1","0","1","2","3"],
  ["1","2","3","4","5"],
  ["4","0","0","1","0"]
]
        """
        heights = [0] * (len(matrix[0]) + 1) # appends a zero so as to allow stack to be emptied
        max_area = 0
        '''
        For every row calculate heights array which would give you the cumulative sum at a col
        for each row. Now calculate max_area = h * w where h is the value at heights[i] and w
        is the number of indexes in heights array we can combine. Which is actually largest
        rectangle in histogram problem. So broadly two steps:
        Step 1: Maintain heights array for every column while traversing thru every row
        Step 2: Calculate max area rectangle in histogram for heights at every row.
        '''
        for row in matrix:
            # don't use length of height array here
            for i in xrange(len(matrix[0])):
                # cumulative height for column pillars so to speak.
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = []
            for i in xrange(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i # Note: check if stack is not empty
                    max_area = max(max_area, h*w)
                stack.append(i)
        return max_area

    def maximal_square(self, matrix):
        '''
        Same as above, the only difference being area will be calculated based on min(height, width)
        '''
        if not matrix: return 0
            heights = [0] * (len(matrix[0]) + 1) # appends a zero so as to allow stack to be emptied
            max_area = 0
            for row in matrix:
                # don't use length of height array here
                for i in xrange(len(matrix[0])):
                    # cumulative height for column pillars so to speak.
                    heights[i] = heights[i] + 1 if row[i] == '1' else 0
                stack = []
                for i in xrange(len(heights)):
                    while stack and heights[i] < heights[stack[-1]]:
                        h = heights[stack.pop()]
                        w = i - stack[-1] - 1 if stack else i
                        sq_len = min(h, w)
                        max_area = max(max_area, sq_len*sq_len)
                    stack.append(i)

