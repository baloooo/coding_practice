

class Solution:

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        https://discuss.leetcode.com/topic/19513/beautiful-python-solution/20

        Idea here is to place i, j, k at the end of nums1, nums2 actual input
        arrays and k at the physical end of nums1 (including white spaces as
        mentioned in PStatement for accomodating merged part).
        Now scan backwards from nums1 and nums2 using i, and j and keep adding
        elements to nums1 rear using k.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0: # Since i cannot reach zero as it has space for both m and n, we can be sure j is the only thing we would want to check
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

if __name__ == '__main__':
    test_cases = [
        ([[5,10],2,[1,2,6,8,12],5], [1,2,5,6,8,10,12]),
    ]
    for test_case in test_cases:
        res = Solution().my_func(*test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
