class Solution(object):
    def candy(self, ratings):
        """
        Idea: https://discuss.leetcode.com/topic/37971/the-simplest-and-well-explained-solution-accepted-as-best-submission-in-c
        https://discuss.leetcode.com/topic/37924/very-simple-java-solution-with-detail-explanation
        https://discuss.leetcode.com/topic/4274/c-easy-to-understand-solution-with-lot-of-comments-o-n-constant-space-one-pass/2
        """
        n = len(ratings)
        if n <= 1:
            return n
            
        # initial state: each kid gets one candy    
        nums = [1] * n
        # kids on upwards curve get candies
        for i in xrange(1, n):
            if ratings[i] > ratings[i-1]: # You get more candies if you're better than your left peer.
                nums[i] = nums[i-1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        # Pay little more attention to this loop structure.
        for i in xrange(n-1, 0, -1):
            if ratings[i-1] > ratings[i]: # You get more candies if you're better than your right peer.
                nums[i-1] = max(nums[i]+1, nums[i-1])
   
        return sum(nums)
