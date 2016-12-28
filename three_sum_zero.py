# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example,
given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
"""


def get_three_sum_zero(arr):
    arr.sort()
    triplets = []
    triplet_set = set()
    n = len(arr)
    for a in xrange(0, n-2):
        b = a+1
        c = n-1
        while(b < c):
            cur_sum = arr[a] + arr[b] + arr[c]
            if cur_sum == 0:
                triplet = (arr[a], arr[b], arr[c])
                if triplet not in triplet_set:
                    triplets.append(triplet)
                    triplet_set.add(triplet)
                c -= 1
            elif cur_sum > 0:
                c -= 1
            else:
                b += 1

    return triplets

if __name__ == '__main__':
    # arr = [-1, 0, 1, 2, -1, -4]
    arr = [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
    print get_three_sum_zero(arr)
