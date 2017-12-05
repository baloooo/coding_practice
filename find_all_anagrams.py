class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
	http://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
	Idea is to create a window of size of pattern, now after initial population of pattern and string
	dicts, for each new char in s starting from len(p) onwards add it to s_dict as this comes in to 
	window and remove whatever went out of the window since length of window is constant at len(p).
        """
	if not s or not p or len(p) > len(s):
            return []
        anagrams = []
        s_dict = collections.defaultdict(int)
        p_dict = collections.defaultdict(int)
        for i in xrange(len(p)): # Add initial window (len(p)) chars to dicts
            p_dict[p[i]] += 1
            s_dict[s[i]] += 1
        for i in xrange(len(p), len(s)):
            if p_dict == s_dict: # At each step see if current s_dict is == to p_dict (we want)
                anagrams.append(i-len(p))
            s_dict[s[i]] += 1 # Add new cur character to string dict
            s_dict[s[i-len(p)]] -= 1 # remove character that went out of window
            if s_dict[s[i-len(p)]] == 0:
                del s_dict[s[i-len(p)]]

        if p_dict == s_dict: # check last window
            anagrams.append(len(s)-len(p))
        return anagrams
