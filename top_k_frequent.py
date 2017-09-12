'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import heapify, heappop
        import collections

        freq_map = collections.defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        max_heap = [(-freq, num) for num, freq in freq_map.items()]
        heapify(max_heap)
        most_frequent = []
        for _ in xrange(k):
            most_frequent.append(heappop(max_heap)[1])
        return most_frequent

if __name__ == '__main__':
    test_cases = [
        ([1, 1, 1, 2, 2, 3], [1, 2]),
    ]
    for test_case in test_cases:
        res = Solution().topKFrequent(test_case[0], 2)
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
