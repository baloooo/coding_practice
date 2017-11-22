def is_palindrome(self, s):
    '''
    Idea: https://discuss.leetcode.com/topic/22479/python-in-place-two-pointer-solution/8
    '''
    # s = s.lower()
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalphanum():
            l += 1
        while l < r and not s[r].isalphanum():
            r -= 1
        if s[l] != s[r] and s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
