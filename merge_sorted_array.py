

class Solution:

    def my_func(self, arr1, len_arr1, arr2, len_arr2):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # shift arr1 to end
        arr1.extend([0]*len_arr2)
        for i in xrange(len_arr1):
            arr1[i-len_arr1] = arr1[i]
        i = len_arr2
        j = k = 0
        while i < (len_arr1+len_arr2) and j < len_arr2:
            if arr1[i] < arr2[j]:
                arr1[k] = arr1[i]
                i += 1
            else:
                arr1[k] = arr2[j]
                j += 1
            k += 1
        while i < (len_arr1+len_arr2):
            arr1[k] = arr1[i]
            k += 1
            i += 1
        while j < len_arr2:
            arr1[k] = arr2[j]
            k += 1
            j += 1

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
