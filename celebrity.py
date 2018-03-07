'''
https://leetcode.com/problems/find-the-celebrity/discuss/71227/Java-Solution.-Two-Pass
https://stackoverflow.com/questions/29814436/optimal-solution-for-the-celebrity-algorithm
https://www.geeksforgeeks.org/the-celebrity-problem/
'''
import pytest

class Solution():
    # The knows API is already defined for you.
    # @param a, person a
    # @param b, person b
    # @return a boolean, whether a knows b
    # def knows(a, b):

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # find candidate for celebrity
        for i in xrange(1, n):
            # Notice here that if candidiate knows i, our current candidate
			# cannot be a celebrity as celebrity knows no one in the party,
            # whereas if candidate doesn't know i, we can be very sure that
			# for all intents and purposes "i" is not a celebrity since there
            # is atleast one member in the party, (i.e candidate) who doesn't
			# know "i".So safe to ignore him for any future calculations.
            if knows(candidate, i):
                candidate = i
        # check if celebrity is actually a celebrity and not a miscalculated
		# candidate, by asking everyone in the party if they know candidate
        for i in xrange(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate
