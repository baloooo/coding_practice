# https://discuss.leetcode.com/topic/4417/possibly-simplest-solution-with-o-n-time-complexity/35?page=1
class Solution:
    def max_product_subarray(self, arr):
        '''
        The idea is to not only store max_so_far and cur_max/max_ending_here as we would for
        max_sum_subarray exercise but also store min_so_far/min_ending_here b'coz if you have
        a subarray with a negative product of -100 and a positive product of 150 an element -5
        can come next and make the negative product more superior thus chaning it's
        sign and amplidying it's magnitue too.
        Therefore we need to track min_so_far too notice this isn't a problem when you're adding
        numbers as in max_sum_subarr
        
        # Time: O(n) Space: O(1)
        # store the result that is the max we have found so far'''
        max_so_far = arr[0]
        # These store the min/max product of subarray that ends at cur_index
        min_ending_here = max_ending_here = arr[0]
        for index in xrange(1, len(arr)):
            # multiplied by a negative makes big number smaller, small number
            # bigger, so we redefine the extremums by swapping them
            # Also notice that since this number is negative, max and min will invert b'coz
            # of multiplying by a negative numbers, so we don't need to revert them back
            if arr[cur_index] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here  # noqa
            # max/min product for the current number is either the current
            # number itself or the max/min by the previous number times the
            # current one
            max_ending_here = max(arr[cur_index], arr[cur_index] * max_ending_here)
            min_ending_here = min(arr[cur_index], arr[cur_index] * min_ending_here)
            # the newly computed max value is a candidate for our global result
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def maxProduct_optimized(self, nums):
        '''
        More intutive than below one.
        https://leetcode.com/problems/maximum-product-of-three-numbers/solution/

        Key idea here is that a num can reside in minimum and maximum variables both.
        To deal with the cases like:
            [1, 2, 3]
            [-1, -2, -3]

        '''
        if len(nums) == 1: return nums[0]
        max1 = max2 = max3 = -float('inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

            if num > max3:
                max1 = max2
                max2 = max3
                max3 = num
            elif num > max2:
                max1 = max2
                max2 = num
            elif num > max1:
                max1 = num

        return max(max1*max2*max3, min1*min2*max3)

    def maxProduct_old(self, nums):
        """
        :type nums: List[int]
        :rtype: int
	Can't initialize with float('inf') since float('inf')*0 is NaN and cannot be played with
	https://stackoverflow.com/questions/36016266/how-to-get-a-floating-point-infinity-that-when-multiplied-by-zero-gives-zero
        """
        if len(nums) == 1:
            return nums[0]
        max_product = sys.float_info.max
        cur_max, cur_min = -sys.float_info.max, sys.float_info.max
        for num in nums:
            
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max*num, num)
            cur_min = min(cur_min*num, num)
            max_product = max(max_product, cur_max)
        return max_product

if __name__ == '__main__':
    test_cases = [
        # ([2, 3, -2, 4], 6),
        # ([-2, 3, -4], 24),
        ([0, 2], 2),
    ]
    res = Solution().maxProduct([0, 2])
    for test_case in test_cases:
        res = Solution().max_product_subarray(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
