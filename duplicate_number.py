"""
https://leetcode.com/problems/find-the-duplicate-number/#/description
Idea: tortoise hare strategy, diagram: https://discuss.leetcode.com/topic/25685/java-o-n-time-and-o-1-space-solution-similar-to-find-loop-in-linkedlist
"""


class Solution:
    def __init__(self):
        pass

    def duplicate_number(self, arr):
	slow = arr[0]
	fast = arr[arr[0]]
	while slow != fast:
            slow = arr[slow]	
            fast = arr[arr[fast]]
        fast = 0
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow

if __name__ == '__main__':
    test_cases = [
        ([3, 2, 1, 2, 4, 9, 5], 2),
    ]
    for test_case in test_cases:
        res = Solution().duplicate_number(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
