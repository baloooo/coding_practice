"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

    Input : [2, 1, 2]
    Return  : 2 which occurs 2 times which is greater than 3/2. 
"""


class Solution:
    def __init__(self):
        pass

    def majority_element(self, nums):
	"""
        :type nums: List[int]
        :rtype: int
        Idea: http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
        """
        counter = 0
        candidate = None
        for cur_ele in nums:
            if counter == 0:
                candidate = cur_ele
                counter = 1
            elif cur_ele == candidate:
                counter += 1
            else:
                counter -= 1
	return candidate

if __name__ == '__main__':
    test_cases = [
        ([3,2,3], 3),
    ]
    for test_case in test_cases:
        res = Solution().majority_element(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
