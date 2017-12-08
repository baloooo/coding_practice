class Solution(object):
    
    """
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Time: O(nk)

        http://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
        below implementation cannot be trusted
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]] # s[low] will give the char in the string that has lowest index, now delete this char from dictionary
                low += 1 # this will be new low since we deleted first minimum, this would also work when our low had duplicates since we already would have updated it with the max value for low char.
            ret = max(i - low + 1, ret)
        return ret
