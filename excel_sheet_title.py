'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    #  https://discuss.leetcode.com/topic/6245/python-solution-with-explanation
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = list(string.uppercase)
        res = []
        while n > 0:
            res.append(capitals[(n-1)%26])
            n = (n-1) /26
        res.reverse()
        return ''.join(res)
