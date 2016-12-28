# -*- coding: utf-8 -*-
"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
 NOTE : For the purpose of this problem ( as also conveyed by the sample case )
, assume that elements that appear more than once in both arrays should be
included multiple times in the final outp
"""


def get_intersection(arr1, arr2):
    common_elements = []
    i = j = 0
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] == arr2[j]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return common_elements

if __name__ == '__main__':
    arr1 = [1, 2, 3, 3, 4, 5, 6]
    arr2 = [3, 5]
    arr1 = [1,2,3,3,4,5,6]
    arr2 = [3,3,5]
    print get_intersection(arr1, arr2)
