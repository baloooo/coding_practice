

class Solution:
    def __init__(self):
        pass

    def min_size_subarr(self, arr, target_sum):
	'''
	O(n)
	https://leetcode.com/problems/minimum-size-subarray-sum/solution/
	'''
	if not arr: return 0
        if not (0 <= target_sum <= sum(arr)):
            return 0
        left = 0 
        min_subarr = len(arr)
        cur_sum = 0 
        for i in xrange(len(arr)):
            cur_sum += arr[i]
            while cur_sum >= target_sum:
                min_subarr = min(min_subarr, i - left + 1)
                cur_sum -= arr[left]
                left += 1
        return min_subarr

if __name__ == '__main__':
    test_cases = [
        (([2, 3, 1, 2, 4, 3], 7), 2),
    ]
    for test_case in test_cases:
        res = Solution().min_size_subarr(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
