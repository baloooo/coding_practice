# coding: utf-8
'''
https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
https://www.geeksforgeeks.org/count-pairs-difference-equal-k/
Notice that tricky part in this exercise is to deal with k = 0
'''
import pytest

class Solution(object):
    def findPairs_hash(self, arr, k):
        """
        a - b = k, can be written as a = b + k
        b - a = k, can be written as b = a + k
        Therefore we're indirectly searching for a and b below, using the other element and k similar to two sum logic

        Time: O(n), space: O(n)
        """
        if k < 0 or len(arr) < 2:
            return 0
        if k == 0:
            ele_dict = collections.defaultdict(int)
            for ele in arr:
                ele_dict[ele] += 1
            return sum([1 for freq in ele_dict.values() if freq >= 2])
        count = 0
        ele_dict = {ele: True for ele in arr}
        for ele in arr:
            if ele_dict[ele] is True:
                if ele_dict.get(ele + k) is True:
                    count += 1
                if ele_dict.get(ele - k) is True:
                    count += 1
                ele_dict[ele] = False
        return count

    def findPairs_sorting(self, arr, target):
        '''
		Sort the array arr
		Take two pointers, l and r, both pointing to 1st element
		Take the difference arr[r] – arr[l]
		If value diff is K, increment count and move both pointers to next element
		if value diff > k, move l to next element
		if value diff < k, move r to next element
		return count

        nlogn
        '''
        if len(arr) < 2 or target < 0: return 0
        arr.sort()
        count = 0
        l, r = 0, 1
        while r < len(arr):
            if l == r:
                r += 1 # base prerequisite i != j
            else:
                cur_diff = arr[r] - arr[l]
                if cur_diff == target:
                    count += 1
                    l += 1
                    while l < len(arr) and arr[l] == arr[l-1]:
                        l += 1
                    r += 1
                    while r < len(arr) and arr[r] == arr[r-1]:
                        r += 1
                elif cur_diff < target:
                    r += 1
                else:
                    l += 1
        return count

    def findPairs_bruteforce(self, arr, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Time: O(n^2), space: O(1)
        """
        arr.sort()
        count = 0
        for i in xrange(0, len(arr)):
            start, end = i, len(arr)-1
            if i != 0 and arr[i] == arr[i-1]:
                continue
            while start < end:
                cur_diff = arr[end] - arr[start]
                if cur_diff == target:
                    count += 1
                    start += 1
                    while start < end and arr[start] == arr[start-1]:
                        start += 1
                    while start < end and arr[end] == arr[end-1]:
                        end -= 1
                if cur_diff < target:
                    start += 1
                else:
                    end -= 1
        return count

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (([3,1,4,1,5], 2), 2),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.findPairs(*args) == result

if __name__ == '__main__':
    arr, target = [3,1,4,1,5], 2
    arr, target = [3,1,4,1,5], 0
    # arr = [1, 1, 3, 4, 5]
    print Solution().findPairs_sorting(arr, target)
