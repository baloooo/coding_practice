"""

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

    A : [3 5 4 2]

    Output : 2 
    for the pair (3, 4)

"""


class Solution:
    def __init__(self):
        pass

    def max_distance(self, arr):
        cur_min = arr[0]
        lmin = [arr[0]]
        for index in xrange(1, len(arr)):
            cur_min = min(cur_min, arr[index])
            lmin.append(cur_min)
        cur_max = arr[len(arr)-1]
        rmax = [arr[len(arr)-1]]
        for index in xrange(len(arr)-2, -1, -1):
            cur_max = max(cur_max, arr[index])
            rmax.append(cur_max)
        rmax = rmax[::-1]
        lindex = rindex = 0
        max_distance = 0
        print 'arr: ', arr
        print 'lmin: ', lmin
        print 'rmax: ', rmax
        while (lindex < len(arr) and rindex < len(arr)):
            if lmin[lindex] > rmax[rindex]:
                lindex += 1
            else:
                max_distance = max(max_distance, rindex-lindex)
                rindex += 1
        return max_distance


if __name__ == '__main__':
    test_cases = [
        ([3, 5, 4, 2], 2),
        ([34, 8, 10, 3, 2, 80, 30, 33, 1], 6),
        ([9, 2, 3, 4, 5, 6, 7, 8, 18, 0], 8),
        ([1, 2, 3, 4, 5, 6], 5),
        ([6, 5, 4, 3, 2, 1], -1),
    ]
    for test_case in test_cases:
        res = Solution().max_distance(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
