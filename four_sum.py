class Solution(object):
    def fourSum(self, arr, target):
        """
        The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum.
        Some optimization was be made knowing the list is sorted.

        Idea: https://discuss.leetcode.com/topic/22705/python-140ms-beats-100-and-works-for-n-sum-n-2/16
        """
        def find_four_sum(arr, target, n, results, cur):
            # early termination
            if len(arr) < n or n < 2 or target < arr[0]*n or target > arr[-1]*n:
                return
            # two pointers solve sorted 2-sum problem
            if n == 2:
                start, end = 0, len(arr)-1
                while start < end:
                    cur_sum = arr[start] + arr[end]
                    if cur_sum == target:
                        results.append(cur+[arr[start], arr[end]])
                        # For usecases like ([-3, -2, -1, 0, 0, 1, 2, 3], 0)
                        # where -3, 1 has multiple solutions for n ==2, we need to find
                        # all possible combinations and not just stop at the first one
                        # we find.
                        start += 1
                        while start < end and arr[start] == arr[start-1]:
                            start += 1
                    if cur_sum < target:
                        start += 1
                    else:
                        end -= 1
            else:
                # recursively reduce N
                for i in xrange(len(arr)-n+1):
                    if i == 0 or arr[i] != arr[i-1]:
                        find_four_sum(arr[i+1:], target-arr[i], n-1, results, cur+[arr[i]])
        results, cur = [], []
        find_four_sum(sorted(arr), target, 4, results, cur)
        return results

if __name__ == '__main__':
    test_cases = [
        # (([1, 0, -1, 0, -2, 2], 0), 'sol1'),
        (([-3, -2, -1, 0, 0, 1, 2, 3], 0), ['a']),
    ]
    for test_case in test_cases:
        res = Solution().fourSum(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
