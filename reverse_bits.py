class Solution(object):
    def reverse_bits_optimized(self, num):
        lsb = 1
        msb = 1 << 31
        reversed_num = 0
        for i in xrange(32):
            if num & lsb:
                reversed_num = reversed_num | msb
            lsb = lsb << 1
            msb = msb >> 1
        return reversed_num

    def check_and_set_bit(self, num, pos):
        mask = 1 << pos
        if num & mask:
            final_num_mask = pow(2, 31) >> pos
            self.final_num = self.final_num | final_num_mask

    def reverse_bits(self, num):
        self.final_num = 0
        for pos in xrange(32):
            self.check_and_set_bit(num, pos)
        return self.final_num

if __name__ == '__main__':
    bit_op = BitOperations()
    # print bit_op.reverse_bits(3)
    print bit_op.reverse_bits(8)
