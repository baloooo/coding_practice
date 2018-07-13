class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        Time: O(m)*(2**n), where m is the length of s and n is the number of alphabets in s
		https://leetcode.com/problems/letter-case-permutation/solution/
        """
        res, chars = [], 0
        for ch in s:
            if ch.isalpha():
                chars += 1

        for val in xrange(2**chars):
            cur = []
            for ch in s:
                if ch.isalpha():
                    if val & 1:
                        cur.append(ch.uppercase())
                    else:
                        cur.append(ch.lowercase())
                    val >>= 1
                else:
                    cur.append(ch)
            res.append(''.join(cur))
        return res
