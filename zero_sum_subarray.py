"""
Given an unsorted array of integers, find a continous subarray
which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There may be more than one subarrays with sum as the given sum. The following
solutions print first such subarray.
"""


class Solution:
    def __init__(self):
        pass

    def k_sum_subarray_with_negative_optimized(self, arr, target_sum):
        # Time: O(n) Space: O(n)
        arr_sum_map = {}
        cur_sum = 0
        for index, ele in enumerate(arr):
            if ele == target_sum:
                return (index, index)
            cur_sum += ele
            arr_sum_map[cur_sum] = index
            try:
                second_index = arr_sum_map[cur_sum - target_sum]
                if index == second_index:
                    continue
                return (second_index+1, index)
            except KeyError:
                pass
        return -1

    def k_sum_subarray_with_negative(self, arr, target_sum):
        # Time: O(n^2) Space: O(1)
        for i in xrange(len(arr)):
            for j in xrange(len(arr)):
                if sum(arr[i:j+1]) == target_sum:
                    return (i, j)
        return -1

    def k_sum_subarray_without_negative_optimized(self, arr, target_sum):
        # Time: O(n) Space: O(1)
        i, j = 0, 0
        cur_sum = arr[i]
        while(1):
            # print 'sum: {0} i: {1} j: {2}'.format(cur_sum, i, j)
            if cur_sum == target_sum:
                return (i, j)
            if cur_sum < target_sum:
                if j == len(arr)-1:
                    break
                j += 1
                cur_sum += arr[j]
            else:
                if i == j:
                    break
                cur_sum -= arr[i]
                i += 1
        # sum doesn't exist
        return -1

if __name__ == '__main__':
    test_cases = [
        ([4, 2, 3, 1, 6], 7, (3, 4)),
        ([4, 2, 3, 1, 6], 4, (0, 0)),
        ([4, 2, 3, 1, 16], 16, (4, 4)),
        ([4, 2, 3, 1, 6], 50, -1),
        ([4, 2, 3, 1, 6], 0, -1),
        ([4, 2, 0, 1, 6], 3, (1, 3)),
    ]
    for test_case in test_cases:
        # test_result = Solution().k_sum_subarray_without_negative_optimized(
        #         test_case[0], test_case[1])
        test_result = Solution().k_sum_subarray_with_negative_optimized(
                test_case[0], test_case[1])
        if test_result == test_case[2]:
            print "Passed"
        else:
            print """Failed: arr: {0}, target_sum: {1}, expected_result: {2},
                  Got: {3}""".format(test_case[0], test_case[1], test_case[2],
                                     test_result)
