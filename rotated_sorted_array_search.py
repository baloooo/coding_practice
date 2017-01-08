# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
https://github.com/kamyu104/LeetCode/blob/master/Python/search-in-rotated-sorted-array.py
"""
def r_bs(arr, lo, hi, x):
    while(lo<=hi):
        if lo+1==hi:
            if arr[lo] == x:
                return lo
            elif arr[hi] == x:
                return hi
            else:
                return -1
        mid = lo + (hi-lo)/2
        if arr[mid] == x:
            return mid
        # print 'lo: %d mid: %d hi: %d' % (lo, mid, hi)
        # print 'lo: %d mid: %d hi: %d' % (arr[lo], arr[mid], arr[hi])
        if (arr[lo]<=arr[mid] and (arr[lo]<=x<arr[mid])) or (arr[lo]>arr[mid] and not (arr[mid]<x<=arr[hi])):
            # go left
            hi = mid - 1
            # print 'going left new hi %d' % hi
        else:
            # go right
            lo = mid + 1
            # print 'going right new lo %d' % lo
    return -1

if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    inp = '180 181 182 183 184 187 188 189 191 192 193 194 195 196 201 202 203 204 3 4 5 6 7 8 9 10 14 16 17 18 19 23 26 27 28 29 32 33 36 37 38 39 41 42 43 45 48 51 52 53 54 56 62 63 64 67 69 72 73 75 77 78 79 83 85 87 90 91 92 93 96 98 99 101 102 104 105 106 107 108 109 111 113 115 116 118 119 120 122 123 124 126 127 129 130 135 137 138 139 143 144 145 147 149 152 155 156 160 162 163 164 166 168 169 170 171 172 173 174 175 176 177'
    arr = [int(x) for x in inp.split(' ')]
    n = len(arr) - 1
    print r_bs(arr, 0, n, 42)
