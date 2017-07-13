# *-* coding: utf-8
# Time:  O(1)
# Space: O(1)

# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#       ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
class Solution(object):
    def hammingDistance(self, x, y):
        xor = x^y
        count = 0
        while xor:
            if xor & 1:
                count+=1
            xor = xor >> 1
        return count

def hamming_distance(num1, num2):
    # integer to binary conversion http://stackoverflow.com/questions/16926130/python-convert-to-binary-and-keep-leading-zeros
    bin1 = '{0:015b}'.format(num1)
    bin2 = '{0:015b}'.format(num2)
    # print bin1, bin2
    return (sum(cur_bit_num1!=cur_bit_num2 for cur_bit_num1, cur_bit_num2 in zip(bin1, bin2)))

if __name__ == '__main__':
    num1, num2 = 1, 4
    print hamming_distance(num1, num2)
