"""

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

    A : [3 5 4 2]

    Output : 2 
    for the pair (3, 4)

"""


class Solution:
    '''
    There are 3 variations to this problem:
	max diff b/w the indexes of elements where arr[i] <= arr[j]
		http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
	max diff b/w two elements where only cond'n is first should be smaller
		http://www.geeksforgeeks.org/maximum-difference-between-two-elements/
	this says max diff b/w consecutive elements only
		https://leetcode.com/problems/maximum-gap/description/
    '''
    def __init__(self):
        pass
    def max_gap(self, nums):
        # https://leetcode.com/problems/maximum-gap/description/
	# https://discuss.leetcode.com/topic/5999/bucket-sort-java-solution-with-explanation-o-n-time-and-space
	pass

    def max_distance(self, arr):
        # http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
        # check simple and optimized solns there
		if not arr: return 0
		cur_min = arr[0]
		arr_l = [cur_min]
		for i in xrange(1, len(arr)):
			cur_min = min(cur_min, arr[i])
			arr_l.append(cur_min)
		cur_max = arr[-1]
		arr_r = [0]*len(arr)
		arr_r[-1] = cur_max
		for i in xrange(len(arr)-2, -1, -1):
			cur_max = max(cur_max, arr[i])
			arr_r[i] = cur_max
		i = j = 0
		max_distance = -float('inf')
		while i < len(arr_l) and j < len(arr_r):
			if arr_l[i] > arr_r[j]:
				i += 1 # since arr[i] has to be smaller than arr[j] (base condition)
			else:
				max_distance = max(max_distance, j-i)
				j += 1
		return max_distance
        # cur_min = arr[0]
        # lmin = [arr[0]]
        # for index in xrange(1, len(arr)):
        #     cur_min = min(cur_min, arr[index])
        #     lmin.append(cur_min)
        # cur_max = arr[len(arr)-1]
        # rmax = [arr[len(arr)-1]]
        # for index in xrange(len(arr)-2, -1, -1):
        #     cur_max = max(cur_max, arr[index])
        #     rmax.append(cur_max)
        # rmax.reverse()
        # lindex = rindex = 0
        # max_distance = 0
        # while (lindex < len(arr) and rindex < len(arr)):
        #     if lmin[lindex] > rmax[rindex]:
        #         lindex += 1
        #     else:
        #         max_distance = max(max_distance, rindex-lindex)
        #         rindex += 1
        # return max_distance


if __name__ == '__main__':
    test_cases = [
		# ([1, 10], 1),
		([100, 100, 100, 100], 4),
		# ([1, 3, 100], 97),
        # ([3, 5, 4, 2], 2),
        # ([34, 8, 10, 3, 2, 80, 30, 33, 1], 6),
        # ([9, 2, 3, 4, 5, 6, 7, 8, 18, 0], 8),
        # ([1, 2, 3, 4, 5, 6], 5),
        # ([6, 5, 4, 3, 2, 1], -1),
    ]
    for test_case in test_cases:
        res = Solution().max_distance(test_case[0])
        # res = Solution().max_gap(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
