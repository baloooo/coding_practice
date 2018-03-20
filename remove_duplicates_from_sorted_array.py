"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 
"""
def remove_duplicates_generalized(arr):
        """
        Idea: https://discuss.leetcode.com/topic/7673/share-my-o-n-time-and-o-1-solution-when-duplicates-are-allowed-at-most-k-times/12
        """
        if len(arr) <= 1: return len(arr)
        count = 1
        unique_index = 0
        for iter_index in xrange(1, len(arr)):
            if arr[iter_index] != arr[unique_index]:
                count = 1
                unique_index += 1
                arr[unique_index] = arr[iter_index]
            else:
                if count < 2:
                    count += 1
                    unique_index += 1
                    arr[unique_index] = arr[iter_index]
        return unique_index + 1
        # if not arr:
        #     return 0
        # k = 1 # This depicts the number of tolerable duplicates.
        # i = j = count = 1
        # while j < len(arr):
        #     if arr[j] != arr[j-1]:
        #         count = 1
        #         arr[i] = arr[j]
        #         i += 1
        #     else:
        #         if count < k:
        #             arr[i] = arr[j]
        #             i += 1
        #             count += 1
        #     j += 1
        # return i

def remove_duplicates_optimized(arr):
    """
    Time: O(n)
    Space: O(1)
    """
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers: one for the unique elements, one for iterating over arr
        if len(arr) < 2:
            return len(arr)
        k = 1
        for i in xrange(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[k] = arr[i]
                k += 1
        return k

if __name__ == '__main__':
    # arr = [1,1]
    # arr = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8]
    # arr = [1, 1, 2, 3]
    # arr = [1]
    # arr = [1, 2, 3]
    # arr = [0]
    arr = [1, 1, 2, 3, 4, 4]
    print remove_duplicates_generalized(arr)
