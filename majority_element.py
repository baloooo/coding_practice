# coding: utf-8

class Solution:
    def majority_element_one_third(self, nums):
        """
        Can be done using hashing for any majority k elements by maintaining a frequency map.
        Though would take n space.

        Given an integer array of size n, find all elements that appear more
        than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1)
        space.
        """
        candidates = []
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for ele in nums:
            '''
            This order of if-else matters. Always check for element equivalence first,
            as candidate's count may go to zero and then come up back, but if you check
            count first, whenever first time count gets to zero, candidate can be thrown out.
            Also, notice that this opposite to what we do in n/2 majority element.
            '''
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
        # ([3, 2, 3], [3]),
        # ([1, 2], [1, 2]),
        # ([8, 8, 7, 7, 7], [8, 7]),
	([1,2,2,3,2,1,1,3], [1, 2]),
    ]
    for test_case in test_cases:
        # res = Solution().majority_element(test_case[0])
        res = Solution().majority_element_one_third2(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
