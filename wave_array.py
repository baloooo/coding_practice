# coding: utf-8
"""
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
"""


class Solution:

    def wave_arr(self, arr):
		'''
		Idea is same as below, but execution is much more straight forward just run
		two loops in parallell with zip
		'''
		arr.sort()
		for i, j in zip(xrange(len(arr), 2), xrange(1, len(arr), 2)):
			arr[i], arr[j] = arr[j], arr[i]

		return arr

    def wave_arr_optimized(self, arr):
        '''
        Idea: http://www.geeksforgeeks.org/sort-array-wave-form-2/
        The idea is based on the fact that if we make sure that all even positioned
        (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements,
        we don’t need to worry about odd positioned element. Following are simple steps.
        1) Traverse all even positioned elements of input array, and do following.
            a) If current element is smaller than previous odd element, swap previous and current.
            b) If current element is smaller than next odd element, swap next and current.
        Time: O(n)
        '''
        for index in xrange(0, len(arr), 2):
            if index > 0 and arr[index-1] > arr[index]:
                arr[index-1], arr[index] = arr[index], arr[index-1]
            if index < len(arr)-1 and arr[index+1] > arr[index]:
                arr[index+1], arr[index] = arr[index], arr[index+1]
        return arr
    def wave_arr_basic(self, A):
        # O(nlogn)
        A.sort()
        for i in xrange(0, len(A), 2):
            try:
                A[i], A[i+1] = A[i+1], A[i]
            except IndexError:
                pass
        return A

if __name__ == '__main__':
    test_cases = [
        ([ 6, 17, 15, 13 ], [13, 6, 17, 15]),
    ]
    for test_case in test_cases:
        res = Solution().wave_arr_optimized(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
