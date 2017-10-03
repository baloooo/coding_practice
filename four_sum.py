class Solution(object):
    def n_sum(self, arr, N, start_index, target, cur, result):
        if N == 2:
            # logic for two sum
            start, end = start_index, len(arr)-1
            while start < end:
                cur_sum = arr[start] + arr[end]
                if cur_sum == target:
                    result.append(cur+[arr[start],arr[end]])
                    start += 1
                    while start < end and arr[start] == arr[start-1]:  # powerful optimization when there're lot of duplicates.
                        start += 1
                elif cur_sum > 0:
                    end -= 1
                else:
                    start += 1
        else:
            for i in xrange(start_index, len(arr)):
                if i == start_index or (arr[i] != arr[i-1]):
                    cur.append(arr[i])
                    if arr[i] == 1:
                        import ipdb; ipdb.set_trace()
                    self.n_sum(arr, N-1, i+1, target-arr[i], cur, result)
                    cur.pop()

    def four_sum(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr.sort()
        print arr
        cur, result = [], []
        self.n_sum(arr, 4, 0, target, cur, result)
        return result

    def fourSum(self, arr, target):
        """
        Time: O(n^2) (for base) * O(n) for two pointer, therefore in total O(n^3)
        In general, for k > 1, it is n**(k-1)
        The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum.
        Some optimization can be made knowing the list is sorted.

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
    arr, target = [1,0,-1,0,-2,2], 0
    print Solution().four_sum(arr, target)
    # test_cases = [
    #     # (([1, 0, -1, 0, -2, 2], 0), 'sol1'),
    #     (([-3, -2, -1, 0, 0, 1, 2, 3], 0), ['a']),
    # ]
    # for test_case in test_cases:
    #     # res = Solution().fourSum(test_case[0][0], test_case[0][1])
    #     if res == test_case[1]:
    #         print "Passed"
    #     else:
    #         print "Failed: Test case: {0} Got {1} Expected {2}".format(
    #             test_case[0], res, test_case[1])
