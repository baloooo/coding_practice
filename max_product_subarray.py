

class Solution:
    def __init__(self):
        pass

    def max_product_subarray(self, arr):
        # store the result that is the max we have found so far
        max_so_far = arr[0]
        # These store the min/max product of subarray that ends at cur_index
        min_ending_here = max_ending_here = arr[0]
        cur_index = 1
        while cur_index < len(arr):
            # multiplied by a negative makes big number smaller, small number
            # bigger, so we redefine the extremums by swapping them
            if arr[cur_index] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here  # noqa
            # max/min product for the current number is either the current
            # number itself or the max/min by the previous number times the
            # current one
            max_ending_here = max(
                arr[cur_index], arr[cur_index]*max_ending_here)
            min_ending_here = min(
                arr[cur_index], arr[cur_index]*min_ending_here)
            # the newly computed max value is a candidate for our global result
            max_so_far = max(max_so_far, max_ending_here)
            cur_index += 1
        return max_so_far

if __name__ == '__main__':
    test_cases = [
        ([2, 3, -2, 4], 6),
        ([-2, 3, -4], 24),
    ]
    for test_case in test_cases:
        res = Solution().max_product_subarray(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
