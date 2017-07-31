"""
n-bit Gray Codes can be generated from list of (n-1)-bit Gray codes using
following steps.
1) Let the list of (n-1)-bit Gray codes be L1. Create another list L2 which is
reverse of L1.
2) Modify the list L1 by prefixing a ‘0’ in all codes of L1.
3) Modify the list L2 by prefixing a ‘1’ in all codes of L2.
4) Concatenate L1 and L2. The concatenated list is required list of n-bit Gray
codes.
"""


class Solution:
    def __init__(self):
        self.two_bit_gray = ['00', '01', '11', '10']

    def gray_code(self, bits):
        def generate_gray(bits):
            if bits == 2:
                return self.two_bit_gray
            else:
                # gray code for n-1
                gray_sub = generate_gray(bits-1)
                gray_first_half = ['0'+each for each in gray_sub]
                gray_second_half = ['1'+each for each in gray_sub[::-1]]
                return gray_first_half+gray_second_half
        gray_codes = generate_gray(bits)
        gray_decimal = [int(gray_code, 2)for gray_code in gray_codes]
        return gray_decimal

    def gray_code_leet(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [(num >> 1) ^ num for num in xrange(2**n)]

if __name__ == '__main__':
    sol = Solution()
    bits = 3
    # print sol.gray_code(bits)
    print sol.gray_code_leet(bits)
