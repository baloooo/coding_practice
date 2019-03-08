'''
https://leetcode.com/problems/counting-bits/solution/

There's always bruteforce with O(nk) where n is the no. of nums and k the avg. binary length.
'''

class Solution(object):
    def countBits(self, num):
        '''
        Approach #3 DP + Least Significant Bit
        Core idea:
        Number of 1s in a num is equal to number of 1s in number/2 (as that is what you would get if you
        do a >> operation on num.) + whatever is on the LSB
        '''
        dp = [0] * (num+1)
        for i in xrange(1, num+1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


    def countBits_old(self, num):
        '''
        Approach1 for bruteforce, and approach 2 for dp
        https://leetcode.com/problems/counting-bits/solution/
        transition function:f(x+b) = f(x) + 1 
        '''
        base = 1
        counts = [0]*(num+1)
        idx = 0
        while base <= num:
            while idx <= base and base + idx <= num:
                counts[base + idx] = counts[idx] + 1
                idx += 1
            
            idx = 0
            base = base << 1
        
        return counts

if __name__ == '__main__':
    num = 5 # [0,1,1,2,1,2]
    num = 2 # [0, 1, 1]
    print Solution().countBits(num)
