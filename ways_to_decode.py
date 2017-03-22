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
        self.sum = 0
        self.encoded_text = ''

    def decode(self, encoded_text):
        self.ways_to_decode(len(encoded_text)-2)
        self.encoded_text = encoded_text
        return self.sum

    def ways_to_decode(self, text_end_delimeter):
        if text_end_delimeter == len(self.encoded_text)-2:
            return 1
        if text_end_delimeter == len(self.encoded_text)-3:
            if int(self.encoded_text[text_end_delimeter:]) <= 26:
                return 2
            else:
                return 1
        return (self.ways_to_decode(text_end_delimeter+1) +
                self.ways_to_decode(text_end_delimeter+2))

if __name__ == '__main__':
    encoded_text = '1234'
    print Solution().decode(encoded_text)
