'''
https://en.wikipedia.org/wiki/UTF-8#Description
https://www.youtube.com/watch?v=sqPTR_v4qFA&t=497s
Another option is to take bitwise AND of num with UTF-8 standard prefixes for 1, 2, 3 and 4 bytes respectively.
https://leetcode.com/problems/utf-8-validation/discuss/87464/Bit-Manipulation-Java-6ms
Also this is an interesting approach too:
https://leetcode.com/problems/utf-8-validation/discuss/87462/Concise-C++-implementation
'''
import pytest

class Solution():

    def valid_utf8_char(self, data, start, utf_char_len):
        # Notice that we've already checked the current octet at start
        for i in xrange(start+1, start+utf_char_len+1):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
        return True

    def is_valid_utf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        Starting with Python 2.6 you can express binary literals using the prefix 0b or 0B:
        https://leetcode.com/problems/utf-8-validation/discuss/87494/Short'n'Clean-12-lines-Python-solution
        PS: data will be a list of ints, we've to figure out if the first num is a part of a 4 byte utf-8
        or 2 byte utf-8 and then take repective following bytes(ints) and check if they all cumulative
        make a valid utf-8 representation. If it violates, return False else pick the next int and do the 
        same for it untill the list is exhausted.
        Idea is to check MSB for the first int as in UTF-8 first byte(int in this case) dictates how many
        bytes this char is using to represent itself. Now MSB can be any of these 3 types(0, 110, 1110, 11110).
        If found one of these check the following 1, 2, 3 bytes respectively if they have MSB as 10 or not.
        Move the start pointer to the next char representation depending on how many bytes(integer in our case)
        were used in last char representation.
        """
        start = 0
        # import ipdb; ipdb.set_trace()
        while start < len(data):
            num = data[start]
            if num >> 7 == 0: 
                start += 1
            # Notice that we've already checked the current octet
            elif num >> 5 == 0b110 and self.valid_utf8_char(data, start, 1):
                start += 2
            elif num >> 4 == 0b1110 and self.valid_utf8_char(data, start, 2):
                start += 3
            elif num >> 3 == 0b11110 and self.valid_utf8_char(data, start, 3):
                start += 4
            else: 
                return False
        return True 

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ([197, 130, 1], True),
        ([235, 140, 4], False),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.is_valid_utf8(args) == result
