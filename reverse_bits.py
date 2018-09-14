class Solution(object):
    def reverse_bits_optimized(self, num):
        https://articles.leetcode.com/reverse-bits/
        pass

    def reverse_bits2(self, num):
        lsb = 1
        msb = 1 << 31
        reversed_num = 0
        for i in xrange(32):
            if num & lsb:
                reversed_num = reversed_num | msb
            lsb = lsb << 1
            msb = msb >> 1
        return reversed_num

if __name__ == '__main__':
    bit_op = BitOperations()
    # print bit_op.reverse_bits(3)
    print bit_op.reverse_bits(8)
