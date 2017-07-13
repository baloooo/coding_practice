"""
Idea wikipedia:
Find the largest index k such that nums[k] < nums[k + 1]. If no such index
exists, the permutation is sorted in descending order, just reverse it to
ascending order and we are done. For example, the next permutation of
[3, 2, 1] is [1, 2, 3].
Find the largest index l greater than k such that nums[k] < nums[l].
Swap the value of nums[k] with that of nums[l].
Reverse the sequence from nums[k + 1] up to and including the final element
nums[nums.size() - 1].
https://discuss.leetcode.com/topic/15216/a-simple-algorithm-from-wikipedia-with-c-implementation-can-be-used-in-permutations-and-permutations-ii
"""


class Solution:
    def __init__(self):
        pass

    def next_permutation(self, arr):
        if len(arr) <= 1:
            return arr
        for index in xrange(len(arr)-2, -1, -1):
            if arr[index] < arr[index+1]:
                break
        else:
            arr.reverse()
            return arr
        for next_index in xrange(len(arr)-1, index, -1):
            if arr[next_index] > arr[index]:
                break
        arr[index], arr[next_index] = arr[next_index], arr[index]
        for i, j in zip(
                xrange(index+1, len(arr)), xrange(len(arr)-1, index, -1)):
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        return arr

if __name__ == '__main__':
    test_cases = [
        # ([1, 2, 3], [1, 3, 2]),
        # ([1, 3, 2], [2, 1, 3]),
        # ([5, 4, 7, 5, 3, 2], [5, 5, 2, 3, 4, 7]),
        ([769, 533], [533, 769]),
    ]
    for test_case in test_cases:
        res = Solution().next_permutation(test_case[0][:])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
