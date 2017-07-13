# coding: utf-8
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

    def majority_element_one_third(self, nums):
        """
        Given an integer array of size n, find all elements that appear more
        than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1)
        space.
        """
        candidates = []
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for ele in nums:
            # this order of if-else matters
            if ele == cand1:
                count1 += 1
            if ele == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = ele
                count1 = 1
            elif count2 == 0:
                cand2 = ele
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # confirm cand1 or cand 2 has the majority
        count1, count2 = 0, 0
        for ele in nums:
            if ele == cand1: count1 += 1
            elif ele == cand2: count2 += 1
        if count1 > len(nums)/3.0: candidates.append(cand1)
        if count2 > len(nums)/3.0: candidates.append(cand2)
        return candidates


    def majority_element_half(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Idea:
            https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
            http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
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
        # confirm if not sure whether there is always a majority element
        # with one scan counting the occurrences of candidate.
        return candidate

if __name__ == '__main__':
    test_cases = [
        # ([3, 2, 3], 3),
        # ([1, 2], [1, 2]),
        ([8, 8, 7, 7, 7], [8, 7]),
    ]
    for test_case in test_cases:
        # res = Solution().majority_element(test_case[0])
        res = Solution().majority_element_one_third(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
