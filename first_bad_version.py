# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
		Strategy: https://leetcode.com/articles/first-bad-version/
        """
        start, end = 1, n
        while start < end:
            mid = start + (end-start)/2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid - 1
        return end if isBadVersion(end) else end + 1
