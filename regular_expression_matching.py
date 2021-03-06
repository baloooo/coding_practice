'''
https://articles.leetcode.com/regular-expression-matching/
https://leetcode.com/articles/regular-expression-matching/
'''


class Solution:
    def is_match_bruteforce(self, text, pattern):
        '''
        Time & space: check https://leetcode.com/articles/regular-expression-matching/ 
        If a star is present in the pattern, it will be in the second position pattern[1].
        Then, we may ignore this part of the pattern, or delete a matching character in the text.
        If we have a match on the remaining strings after any of these operations,
        then the initial inputs matched.
        
        If there's no text, we still have to go ahead and check if the pattern allows it
        may be the pattern is a* in which case no text is also fine of .* etc. So no text
        is not a necessary and sufficient condition to return. On the other hand if there's no
        pattern we can't go ahead as that is the yard stick we use for our measurements and if we
        don't have that there are no measurements therefore no point in going ahead. Just check
        if text exists or not. '''
        if not pattern:
            return not text
        # first_match = bool(text) and pattern[0] in [text[0], '.']
        first_match = text and pattern[0] in [text[0], '.']
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.is_match_bruteforce(text, pattern[2:]) or  # Take zero instances of pattern[0]
		    (first_match and self.is_match_bruteforce(text[1:], pattern))) # Take one instance of pattern[0]
        else:
            return first_match and self.is_match_bruteforce(text[1:], pattern[1:])

    def is_match(self, text, text_ptr, pattern, pattern_idx):
        '''
        Bruteforce is_match with indices rather than copies of text and pattern
        '''
        # Base condition
        if pattern_idx >= len(pattern):
            return text_ptr >= len(text)

        cur_char_match = text_ptr < len(text) and pattern[pattern_idx] in [text[text_ptr], '.']

        if pattern_idx + 1 < len(pattern) and pattern[pattern_idx+1] == '*':
                # take current ele with * occurence or leave it.
                return ((cur_char_match and self.is_match(text, text_ptr + 1, pattern, pattern_idx)) or
                            self.is_match(text, text_ptr, pattern, pattern_idx + 2))
        else:
            return cur_char_match and self.is_match(text, text_ptr + 1, pattern, pattern_idx + 1)

    def is_match_dp(self, text, pattern):
        '''
        dp[i][j] is True if text[0..i) matches pattern[0..j), False otherwise.
        Time = Space =  O(len(text)*len(pattern))
        1. No *: check prev index text and prev index pattern if they are same OR
            pattern has '.' at current index.
        2. if we've * at current index, there're 2 sub-cases.
            a) we've zero  repetion of pattern[j], in which case it will be p[i][j-2] whatever we
            had before two indexes before since 'xa*' i.e at index of x
            b) we've one or more repetition, in which case we check prev matches at P[i-1][j]
               ....to complete?
        State equations:
            1. P[i][j] = P[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.')
            2. P[i][j] = P[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 times
            3. P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] == '*'
               and the pattern repeats for at least 1 times.
        '''
        dp = [[False for _ in xrange(len(pattern)+1)] for _ in xrange(len(text)+1)]
        dp[0][0] = True
        # Perhaps you can start from 1 for i also if you set row 0 as True to begin with
        # since for row 0 (which means text len is zero) any pattern will yeild True value.
        for i in xrange(len(text)+1):
            for j in xrange(1, len(pattern)+1): # pattern starts at 1 to take care of a* types
                if pattern[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (
                        i > 0 and (text[i-1] == pattern[j-2] or pattern[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = i>0 and dp[i-1][j-1] and (text[i-1] == pattern[j-1] or pattern[j-1] == '.')
        return dp[len(text)][len(pattern)]


if __name__ == '__main__':
    test_cases = [
        # ('test1', 'sol1'),
        (("aaa", "aaaa"), False),
    ]
    for test_case in test_cases:
        res = Solution().is_match_bruteforce(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
