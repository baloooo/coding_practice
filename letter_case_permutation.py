class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        Time: O(m)*(2**n), where m is the length of s and n is the number of alphabets in s
        as to get each combination of length "m", we have to iterate over complete "s",
        and there are total 2**n combinations possible.
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

    def get_lc_perms(self, start, cur, res):
        res.append(''.join(cur))
        if start >= len(cur):
            return
        for idx in xrange(start, len(cur)):
            if cur[idx].isalpha():
                if cur[idx].isupper():
                    cur[idx] = cur[idx].lower()
                elif cur[idx].islower():
                    cur[idx] = cur[idx].capitalize()
                self.get_lc_perms(idx + 1, cur, res)
                if cur[idx].isupper():
                    cur[idx] = cur[idx].lower()
                elif cur[idx].islower():
                    cur[idx] = cur[idx].capitalize()

    def letterCasePermutation_recur(self, target):
        """
        This implementation is not optimized as this uses recursion and is thereby limited by stack space.
        :type S: str
        :rtype: List[str]
        """
        if not target:
            return [""]
        res = []
        self.get_lc_perms(0, list(target), res)
        return res
