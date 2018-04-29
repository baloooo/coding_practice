class Solution(object):
    '''
    https://leetcode.com/problems/valid-anagram/solution/
    '''

    def isAnagram(self, s, t):
        """
        Tech1: create frequency maps for both and compare these maps.
        Time:  O(n)
        Space: O(n)
        """
        import collections
        if len(s) != len(t):
        	return False
        freq_map1, freq_map2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in xrange(len(s)):
        	freq_map1[s[i]] += 1
        	freq_map2[t[i]] += 1
        return freq_map1 == freq_map2

    def isAnagram_sorting(self, s, t):
        """
        Tech2: If you don't want to use extra space, sort both strings and compare. 
        Time:  O(nlogn)
        Space: O(1)
        """
        a = ''.join(sorted(list(s)))
        b = ''.join(sorted(list(t)))
        return a == b
     
