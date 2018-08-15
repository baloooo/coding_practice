'''
https://leetcode.com/problems/counting-bits/solution/

There's always bruteforce with O(nk) where n is the no. of nums and k the avg. binary length.
'''

class Solution(object):
    def countBits(self, num):
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

