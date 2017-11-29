'''
https://discuss.leetcode.com/topic/99281/o-log-n-java-1-line-o-log-n-k-ruby/13
https://leetcode.com/articles/find-k-closest-elements/
'''


class Solution:
    def k_closest(self, arr):
        lo, hi = 0, len(arr)-1
        while lo < hi:
            mid = lo + (hi-lo)/2

    def findClosestElements(self, arr, k, x):
        import bisect
        left = right = bisect.bisect_left(arr, x) # lands you on first occurrence of x (incase of duplicates)
        # start from the x as center and expand in both directions till you reach k radius
        while right - left < k:
            if left == 0: return arr[:k]
            if right == len(arr): return arr[-k:]
            if x - arr[left - 1] <= arr[right] - x: left -= 1
            else: right += 1
        return arr[left:right]


if __name__ == '__main__':
    print Solution().findClosestElements([1, 2, 3, 4, 5, 6, 7, 8], 3, 5)
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
