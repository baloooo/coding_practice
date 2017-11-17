"""
Idea: https://discuss.leetcode.com/topic/72092/java-o-n-time-o-1-space/2
"""


class Solution:
    def __init__(self):
        pass

    def my_func(self, arr):
        '''
        Idea:
            For each bit position 1-32 in a 32-bit integer, we count the number of
            integers in the array which have that bit set. Then, if there are n integers
            in the array and k of them have a particular bit set and (n-k) do not, then
            that bit contributes k*(n-k) hamming distance to the total.
        Time: O(nlogm) where n is the total number of elements in arr and m is the biggest
        element
        '''
        if not arr:
            return 0
        max_num = max(arr)
        count = 0
        # Loop will run untill largest number has all it's bits traversed.
        # Alternate would have been while (cur_bit<32) if we had known number can only be 32 bit.
        while max_num:
            # k is the number of numbers which have current bit set out of n
            k = 0
            for index in xrange(len(arr)):
                k += (arr[index] & 1)
                arr[index] = arr[index] >> 1
            count += (k * (len(arr)-k))
            max_num = max_num >> 1
        return count

    def totalHammingDistance(self, arr):
        """
        Just an alternate way where mask moves rather than each number as in above case.
        """
        max_num, mask, ham_dis = max(arr), 1, 0
        while max_num:
            k = 0
            for num in arr:
                if num & mask:
                    k += 1
            ham_dis += (k*(len(arr)-k))
            mask = mask << 1
            max_num = max_num >> 1
        return ham_dis

if __name__ == '__main__':
    test_cases = [
        ([4, 14, 2], 6),
        # ([2, 4, 6], 8),
    ]
    for test_case in test_cases:
        # res = Solution().my_func(test_case[0])
        res = Solution().totalHammingDistance(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
