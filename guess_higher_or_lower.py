# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber_binary_search(self, n):
        """
        :type n: int
        :rtype: int
        Apart from the solution for this case, this article also has a very nice
        implementation of ternary search, also explains why ternary search is not
        better than binary search.

		https://leetcode.com/problems/guess-number-higher-or-lower/solution/
        Checkout https://stackoverflow.com/questions/20512642/big-o-confusion-log2n-vs-log3n#20512708
        for difference b/w log2n and log3n and so on.
        """
        start, end = 1, n
        while start <= end:
            mid = start + (end-start)/2
            response = guess(mid)
            if response == 0:
                return mid
            elif response == -1:
                end = mid - 1
            else:
                start = mid + 1

	def guessNumber_ternary_search(self, n):
        """
            :type n: int
            :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid1 = start + (end-start)/2
			mid2 = end - (end-start)/2

			response1 = guess(mid1)
			response2 = guess(mid2)

			if response1 == 0:
				return mid1
			elif response2 == 0:
				return mid2
			elif response1 == -1:
				end = mid1 - 1
			elif response2 == 1:
				start = mid2 + 1
			else:
				start = mid1 + 1
				end = mid2 - 1
