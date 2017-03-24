"""
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways
to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution:
    def __init__(self):
        self.encoded_text = ''
        self.text_len_to_num_ways_map = {}

    def decode(self, encoded_text):
        if not encoded_text:
            return 0
        self.encoded_text = encoded_text.strip('0')
        return self.ways_to_decode(0)

    def ways_to_decode(self, text_end_delimeter):
        if text_end_delimeter == len(self.encoded_text)-1:
            return 1
        if text_end_delimeter == len(self.encoded_text)-2:
            if int(self.encoded_text[text_end_delimeter:]) <= 26:
                return 2
            else:
                return 1
        if self.text_len_to_num_ways_map.get(text_end_delimeter+1):
            lh = self.text_len_to_num_ways_map[text_end_delimeter+1]
        else:
            lh = self.ways_to_decode(text_end_delimeter+1)
            # memoization
            self.text_len_to_num_ways_map[text_end_delimeter+1] = lh
        if self.text_len_to_num_ways_map.get(text_end_delimeter+2):
            rh = self.text_len_to_num_ways_map[text_end_delimeter+2]
        else:
            rh = self.ways_to_decode(text_end_delimeter+2)
            self.text_len_to_num_ways_map[text_end_delimeter+2] = rh
        return lh+rh

if __name__ == '__main__':
    test_cases = [('1234', 3),
                  ('10', 1),
                  ('101', 1),
                  ('1102', 1),
                  ('0', 0),
                  ('01', 0),
                  ('1100', 0),
                  ('1002', 0),
                  ('261155971756562', True)]
    for test_case in test_cases:
        result = Solution().decode(test_case[0])
        if result == test_case[1]:
            print "Test case: {0} Passed".format(test_case[0])
        else:
            print ("Test case: {0} Failed: Got result: {1}, Expected: {2}".
                   format(test_case[0], result, test_case[1]))
