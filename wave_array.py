"""
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
"""


class Solution:
    def my_func(self, arr):
        # Idea: http://www.geeksforgeeks.org/sort-array-wave-form-2/
        for index in xrange(len(arr), 2):
            if index > 0 and arr[index-1] > arr[index]:
                arr[index-1], arr[index] = arr[index], arr[index-1]
            if index < len(arr)-1 and arr[index+1] > arr[index]:
                arr[index+1], arr[index] = arr[index], arr[index+1]
        return arr

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
