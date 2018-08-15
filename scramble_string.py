'''
https://leetcode.com/problems/scramble-string/discuss/29459/Python-recursive-solution
https://leetcode.com/problems/scramble-string/discuss/29394/My-C++-solutions-(recursion-with-cache-DP-recursion-with-cache-and-pruning)-with-explanation-(4ms)

'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # check if their lens are equal
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        if s1 == s2: return True
        
        for i in xrange(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        
        return False
        
class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def isScramble(self, s1, s2):
        """
	Added cache for storing intermediate results
	In case we use indexes we can start storing start indices along with lengths instead of just s1, s2
	Todo: Use indices instead of using string copies
	Confirm time complexity: Looks like O(n^4) b'coz of similarities to substring logic
        """
        # check if their lens are equal
        if (s1, s2) in self.cache:
            return self.cache[(s1, s2)]
        
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.cache[(s1, s2)] = False
            return False
        
        if s1 == s2: 
            self.cache[(s1, s2)] = True
            return True
        
        for i in xrange(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                self.cache[(s1, s2)] = True
                return True
        self.cache[(s1, s2)] = False
        return False
        
