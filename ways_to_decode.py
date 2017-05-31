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

    def ways_to_decode(self, sequence):
        self.count = 0
        self.decode_ways(0, sequence)
        return self.count

    def decode_ways(self, cur_index, sequence):
        if cur_index >= len(sequence)-1:
            return True
        if sequence[cur_index] == '0':
            self.decode_ways(cur_index + 1, sequence)
        else:
            if self.decode_ways(cur_index + 1, sequence):
                self.count += 1
            if (cur_index + 2 <= len(sequence) and
                    int(sequence[cur_index]+sequence[cur_index+1]) <= 26):
                if self.decode_ways(cur_index + 2, sequence):
                    self.count += 1

if __name__ == '__main__':
    test_cases = [
                    ('11', 2),
                    ('1234', 3),
                    ('10', 1),
                    ('101', 1),
                    ('1102', 1),
                    ('0', 0),
                    ('01', 0),
                    ('1002', 0),
                    ('1', 1),
                    ('0', 0),
                    # ('261155971756562', True)
                    # ('1100', 0),
                  ]
    for test_case in test_cases:
        result = Solution().ways_to_decode(test_case[0])
        if result == test_case[1]:
            print "Test case: {0} Passed".format(test_case[0])
        else:
            print ("Test case: {0} Failed: Got result: {1}, Expected: {2}".
                   format(test_case[0], result, test_case[1]))
