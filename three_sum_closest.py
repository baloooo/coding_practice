"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def nsum(self, arr, n, start_index, target, cur):
        if n < 2: # don't add all the other conditions since we need CLOSEST not EXACT.
            return
        if n == 2:
            start, end = start_index, len(arr)-1
            while start < end:
                cur_sum = arr[start] + arr[end]
                if cur_sum == target:
                    # Returning true will back propogate that we found the target.
                    return True
                if abs(target-self.closest) > abs(target-(sum(cur)+cur_sum)):
                    self.closest = sum(cur)+cur_sum
                '''
                self.closest = min(abs(self.closest), abs(cur_sum)) doesn't work, we absolutely need to store cur, since
                the trick is to always store cur and cur_sum in closest and not the difference which can be false as for 
                test_case [0, 0, 1] and target 1 '''
                if cur_sum < target:
                    start += 1
                else:
                    end -= 1
        else:
            for i in xrange(start_index, len(arr)-2):
                if i == start_index or arr[i] != arr[i-1]:
                    if self.nsum(arr, n-1, i+1, target-arr[i], cur+[arr[i]]):
                        return True
                    
    def threeSumClosest(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cur = []
        self.closest = float('inf')
        arr.sort()
        return target if self.nsum(arr, 3, 0, target, cur) else self.closest


class Solution2:
    def __init__(self):
        pass

    def my_func(self, arr, target):
        import sys
        arr.sort()
        closest = sys.maxint
        for index in xrange(len(arr)-2):
            start, end = index + 1, len(arr)-1
            while start < end:
                cur_closest = arr[index] + arr[start] + arr[end]
                if cur_closest == target:
                    return target
                elif cur_closest < target:
                    start += 1
                else:
                    end -= 1
                if abs(target-closest) > abs(target-cur_closest):
                    closest = cur_closest
        return closest

if __name__ == '__main__':
    # arr, target = [-1,2,1,-4], 1
    arr, target = [0,2,1,-3], 1
    # arr, target = [-10,0,-2,3,-8,1,-10,8,-8,6,-7,0,-7,2,2,-5,-8,1,-4,6], 18
    print Solution().threeSumClosest(arr, target)
    # test_cases = [
    #     (([-1, 2, 1, -4], 1), 2),
    # ]
    # for test_case in test_cases:
    #     res = Solution().my_func(test_case[0][0], test_case[0][1])
    #     if res == test_case[1]:
    #         print "Passed"
    #     else:
    #         print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
