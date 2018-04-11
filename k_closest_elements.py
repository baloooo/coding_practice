'''
https://discuss.leetcode.com/topic/99281/o-log-n-java-1-line-o-log-n-k-ruby/13
https://leetcode.com/articles/find-k-closest-elements/
'''


class Solution:
    def bisect_left(self, arr, target):
        '''yanked from search for range exercise. This works exactly like bisect_left(tested already)'''
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi-lo)/2
            if arr[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def k_closest_elements(self, arr, k, x):
        # Time: O(logn + k), logn for bisect and k for expanding left and right boundary for k length
        import bisect
        # lands you on first occurrence of x (incase of duplicates), bisect_right lands you on last occurnce
        left = right = bisect.bisect_left(arr, x)
        # start from the x as center and expand in both directions till you reach k radius
        while right - left < k:
            if left == 0: # since left indicates what has already been included in the final list(unlike right which indicates right border which may/maynot be included), if we've reached 0 we cannot go anywhere left than this so we can just take k elements starting from the start of the list.
                return arr[:k]
            elif right == len(arr):
                return arr[-k:]
            '''notice (left-1) as in current test case when x is not in list.
            we get back an index that is on first number over x which is correctly returned
            by bisec_left as the index where you can insert x if it's not already there.
            So in first iteration left-1 gives you actual prev index and right has already the
            index of number just greater than x.  '''
            elif x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left:right]


if __name__ == '__main__':
    # arr, k, x = [0,1,2,2,2,3,6,8,8,9], 5, 9
    arr, k, x = [0,0,0,1,3,5,6,7,8,8], 2, 2
    print Solution().k_closest_elements(arr, k, x)
    # test_cases = [
    #     ('test1', 'sol1'),
    # ]
    # for test_case in test_cases:
    #     res = Solution().my_func(test_case[0])
    #     if res == test_case[1]:
    #         print "Passed"
    #     else:
    #         print "Failed: Test case: {0} Got {1} Expected {2}".format(
    #             test_case[0], res, test_case[1])
