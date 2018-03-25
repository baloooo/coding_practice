'''
https://leetcode.com/problems/partition-labels/solution/
'''
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_ocur_map = {ele: i for i, ele in enumerate(S)}
        anchor = j = 0
        res = []
        for i, ele in enumerate(S):
            j = max(j, last_ocur_map[ele])
            if i == j: # If this is the last occurrence of this window
                res.append(j-anchor+1)
                anchor = j+1
        return res
