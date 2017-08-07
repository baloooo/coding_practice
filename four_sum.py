

class Solution:
    def four_sum(self, arr, target_sum):
        def solve_n_sum(arr, target_sum, n, cur_result, results):
            if n < 0: return
            if n == 2:  # two pointer two sum
                start, end = 0, len(arr)-1
                while start < end:
                    cur_sum = arr[start]+arr[end]
                    if cur_sum == target_sum:
                        results.append(cur_result+[start, end])
                        break
                    elif cur_sum < target_sum:
                        start += 1
                    else:
                        end -= 1
            else:
                for i in xrange(len(arr)-n):
                    if i == 0 or arr[i] != arr[i-1]:
                        solve_n_sum(arr[i+1:], target_sum-arr[i], n-1, cur_result+[arr[i]], results)

        results = []        
        cur_result = []
        solve_n_sum(arr, target_sum, 4, cur_result, results)
        return results

if __name__ == '__main__':
    test_cases = [
        (([1, 0, -1, 0, -2, 2], 0), 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().four_sum(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
