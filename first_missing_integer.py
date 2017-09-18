'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''


def firstMissingPositive(self, nums):
    """
    https://discuss.leetcode.com/topic/45556/python-o-1-space-o-n-time-solution-with-explanation
    Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    # this helps when nums is empty + it doesn't harm since it will only bump index 0 which
    # we don't care about and set any entry greater than n, to anyways.
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        # Notice the = sign here since we bumped up the n by appending 0 we made it >=
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        '''
        This makes sure any number that is less than n is our number since every other number
        was either removed (which was greater than n in first loop) or bumped up in second loop
        So if you now find a number less than n (nums[i]/n) will be zero only when a number is in the 
        range 1-n you have got your number.
        '''
        if nums[i]/n==0:
            return i
    return n
