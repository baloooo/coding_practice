class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
	This is the sane version of the Idea ATOI where illegal chars in the given string 's' are ignored as one would.
	The version leetcode required was to quit and when an illegal char is encountered and can be found here
	https://discuss.leetcode.com/topic/26920/60ms-python-solution-oj-says-this-beats-100-python-submissions/7
	The main idea is jotted here and other subtelties are subject to discussion.
        """
        s = s.strip() # strips all spaces on left and right
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        val = 0
        for c in s:
            if c.isdigit():
                val = val*10 + ord(c) - ord('0') # assumes there're no invalid chars in given string
        return sign*val

    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
	Leetcode and IB req satisfying version
        """
        s = s.strip() # strips all spaces on left and right
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        val, index = 0, 0
        if s[0] in ['+', '-']: index = 1
        while index < len(s) and s[index].isdigit():
            val = val*10 + ord(s[index]) - ord('0') # assumes there're no invalid chars in given string
            index += 1
        return max(-2**31, min(sign * val,2**31-1))
