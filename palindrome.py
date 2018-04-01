def is_palindrome(self, s):
    '''
    Idea: https://discuss.leetcode.com/topic/22479/python-in-place-two-pointer-solution/8
    '''
    # s = s.lower()
    if len(s) < 2: return True
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
