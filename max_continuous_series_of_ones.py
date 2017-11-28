# coding: utf-8

class Solution:

    def findMaxConsecutiveOnes(self, nums):
        """
        Idea: https://discuss.leetcode.com/topic/75437/java-4-lines-concise-solution-with-explanation
        """
        max_here, max_ones = 0, 0
        for index, num in enumerate(nums):
            if num != 1:
                max_here = 0
            else:
                max_here += 1
                max_ones = max(max_ones, max_here)
        return max_ones

    def maxone(self, arr, flips_remaining):
        '''
        The main steps are:
        – While zeroCount is no more than m: expand the window to the right (wR++) and update the count zeroCount.
        – While zeroCount exceeds m, shrink the window from left (wL++), update zeroCount;
        – Update the widest window along the way. The positions of output zeros are inside the best window.
        '''
        cur_wl = cur_wr = best_l = best_r = 0
        while cur_wr < len(arr):
            if arr[cur_wr] == 0:
                if flips_remaining:
                    flips_remaining -= 1
                else:
                    while arr[cur_wl] != 0:
                        cur_wl += 1
                    cur_wl += 1
            # Notice that cur_wr should be updated first before best_r/l match since we've adjusted wl according
            # to the latest value of wr at line 27
            cur_wr += 1
            if best_r - best_l < cur_wr - cur_wl:
                best_r, best_l = cur_wr, cur_wl
        return range(best_l, best_r)

    def my_func(self, arr, k):
        """
        Idea: http://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/
        Similar exercise: http://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/
        """
        # wl: window_left, wr: window_right
        wl, wr = 0, 0
        # Left index and size of the widest window
        best_l, best_window = 0, 0
        # count 0f zeroes
        count_z = 0
        # while right boundary of current window doesn't cross right end
        while wr < len(arr):
            """
            If zero count of current window is less than m,
            widen the window toward right
            """
            if count_z <= k:
                if arr[wr] == 0:
                    count_z += 1
                wr += 1
            # Notice this is an if, therefore as soon as count_z goes over
            # the next if brings it back
            if count_z > k:
                if arr[wl] == 0:
                    count_z -= 1
                wl += 1
            # Update widest window if this window size is more
            if wr-wl > best_window:
                best_window = wr-wl
                best_l = wl
        # Returns indexes flipped
        # return [index for index in xrange(best_l, best_l + best_window) if arr[index] == 0]
        print best_l, best_window
        return range(best_l, best_l+best_window)

if __name__ == '__main__':
    test_cases = [
        # (([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2), [5, 7])
        # (([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 1), [0, 1, 2, 3, 4])
        (([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0 ], 4), [0, 1, 2, 3, 4])
    ]
    for test_case in test_cases:
        res = Solution().maxone(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
