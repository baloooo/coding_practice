"""
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

"""


def min_element(arr):
    # https://discuss.leetcode.com/topic/4100/compact-and-clean-c-solution   broadly defines rotation problems in general too.
    l, r = 0, len(arr)-1
    while l < r:
        # if there is no rotation
        if arr[l] <= arr[r]:
            return arr[l]
        mid = l + (r-l)/2
        # given that there is rotation, where is rotation
        # l > r but l < mid this means l to mid is sorted with anchor somewhere after mid
        if arr[l] <= arr[mid]:
            l = mid + 1
        else:
            r = mid
    return arr[l]

if __name__ == '__main__':
    # arr = [4, 5, 6, 7, 0, 1, 2]
    arr = [int(x) for x in inp.split(' ')]
    print min_element(arr)
