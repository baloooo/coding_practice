"""
We define f(X, Y) as number of different corresponding bits in binary representation of X and Y. For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.

For example,

A=[1, 3, 5]

We return

f(1, 1) + f(1, 3) + f(1, 5) + 
f(3, 1) + f(3, 3) + f(3, 5) +
f(5, 1) + f(5, 3) + f(5, 5) =

0 + 1 + 1 +
1 + 0 + 2 +
1 + 2 + 0 = 8
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, nums):
        mask, res = 1, 0
        for index in range(32):
            # check at cur index
            set_bits = 0
            for num in nums:
                if num & mask:
                    set_bits += 1
            res += (set_bits*(len(nums)-set_bits))
            mask <<= 1
        return (2*res) % ((10**9)+7)

