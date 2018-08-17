'''
A more efficent solution of O(n) time exists using manacher algo.
https://leetcode.com/problems/palindromic-substrings/solution/
'''

class Solution(object):
    def _is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
    
    def countSubstrings_recur(self, s):
        """
        :type s: str
        :rtype: int
	Time: O(n^3), n^2 for number of substrings and for each we check palindrome of O(n)
        """
        count = 0
        for i in xrange(len(s)):
            for j in xrange(i, len(s)):
                if self._is_palindrome(s, i, j):
                    count += 1
        
        return count
################################################################################################################

    def extend_palindrome(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            self.count += 1
            low -= 1
            high += 1
    
    def countSubstrings(self, s):
        """
        https://leetcode.com/problems/palindromic-substrings/discuss/105689/Java-solution-8-lines-extendPalindrome
        :type s: str
        :rtype: int
	There will be at max (2n-1) centers (odd + even), and for each center we can at max spread
	across the entire string of len(n) therefore: (2n-1) * n
	Time: O(n^2)
        """
        self.count = 0
        for center in xrange(len(s)):
            self.extend_palindrome(s, center, center) # odd length
            self.extend_palindrome(s, center, center+1) # even length
        
        return self.count
