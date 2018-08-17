'''
Given numbers [2, 3, 4, 5], regarding the third number 4, the product of array except 4 is 2*3*5 which consists of two parts: left 2*3 and right 5. The product is left*right. We can get lefts and rights:

Numbers:     2    3    4     5
Lefts:            2  2*3 2*3*4
Rights:  3*4*5  4*5    5      
Let’s fill the empty with 1:

Numbers:     2    3    4     5
Lefts:       1    2  2*3 2*3*4
Rights:  3*4*5  4*5    5     1
We can calculate lefts and rights in 2 loops. The time complexity is O(n).

'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
	Time: O(n)
	Space: O(n)
	https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space
	https://www.geeksforgeeks.org/a-product-array-puzzle/
        """
        prod_left = [1]*len(nums)
        prod_right = [1]*len(nums)
        prod = [0]*len(nums)
        
        for idx in xrange(1, len(nums)):
            prod_left[idx] = prod_left[idx-1] * nums[idx-1]
        
        for idx in xrange(len(nums)-2, -1, -1):
            prod_right[idx] = prod_right[idx+1] * nums[idx+1]
        
        for idx in xrange(len(nums)):
            prod[idx] = prod_left[idx] * prod_right[idx]
        
        return prod

    def productExceptSelf(self, nums):
        """
        https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space
	Time: O(n)
	Space: O(1)
        """
        prod = [1]*len(nums)
        # simulate prod_left
        for idx in xrange(1, len(nums)):
            prod[idx] = prod[idx-1] * nums[idx-1]
        
        # calculate prod_right and prod simultaneously
        right = 1
        for idx in xrange(len(nums)-1, -1, -1):
            prod[idx] *= right
            right *= nums[idx]
        
        return prod
