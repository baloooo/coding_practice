# -*- coding: utf-8 -*-
"""
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.

"""
def first_occurrence(arr, x):
    n = len(arr)
    start = 0
    end = n-1
    while(start<end):
        # To avoid overflow
        mid = start + (end-start)/2
        if arr[mid] == x:
            if mid-1>=0 and arr[mid-1] == x:
                end = mid-1
                continue
            return mid
        if arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    if arr[start] == x:
        return start
    else:
        return -1

def last_occurrence(arr, x):
    n = len(arr)
    start = 0
    end = n-1
    while(start<end):
        mid = start + (end-start)/2
        if arr[mid] == x:
            if mid+1<n and arr[mid+1] == x:
                start = mid+1
                continue
            return mid
        if arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    if arr[start] == x:
        return start
    else:
        return -1


def count_occurrences(arr, x):
    lptr = first_occurrence(arr, x)
    if lptr == -1:
        return -1
    print 'first occurrence: %d'%lptr
    rptr = last_occurrence(arr, x)
    print 'last occurrence: %d'%rptr
    return rptr - lptr + 1

if __name__ == '__main__':
    # arr = [5 ,7, 7, 8, 8, 10]
    # x = 8
    arr = [1, 1, 2, 2, 2, 2, 3, 3]
    x = 1
    # print first_occurrence(arr, x)
    print count_occurrences(arr, x)
