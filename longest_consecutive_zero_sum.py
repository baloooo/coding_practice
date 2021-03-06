"""
Given an array of integers, find length of the largest subarray with sum equals to 0.

Examples:

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
Output: 5
The largest subarray with 0 sum is -2, 2, -8, 1, 7

Input: arr[] = {1, 2, 3}
Output: 0
There is no subarray with 0 sum

Input: arr[] = {1, 0, 3}
Output: 1
"""

class Solution:
    """
    Idea: http://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/
    The idea is to have a running total of sum until now and keep storing that
    sum in hash map against the index it was acheived at. The moment you see running sum
    as zero or a sum that you have already seen before (in hash map) you got your zero sum
    sub array which can be further extracted from cur_index and the index of cur_sum's index
    in hash map.
    """
    def my_func(self, arr):
        cur_sum, max_len, start = 0, 0, 0
        sum_map = {}
        for index, ele in enumerate(arr):
            cur_sum += ele
            if cur_sum == 0:
                '''Very imp. point: If the running sum reaches zero from the beginning of the array, the longest 
                zero-sum subarray consists of the entire array till the index we reached'''
                max_len = index + 1
                start = 0
            elif cur_sum in sum_map:
                cur_len = index-sum_map[cur_sum] # sum_map[cur_sum] already points to a location one index before actual start so no need to add 1 here for len calculation
                if max_len < cur_len:
                    max_len = cur_len
                    start = sum_map[cur_sum]+1
            else:
                sum_map[cur_sum] = index
        print max_len
        return arr[start: start+max_len]

if __name__ == '__main__':
    test_cases = [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([15, -2, 2, -2, 2, -2, 2, -2], 6),
        ([0, 0, 0, 0, 0, 0, 0], 7),
        ([1, 2, -3, 3], 3),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
