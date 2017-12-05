# *-* coding: utf-8 *-*

"""
Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 < index2. Please note that your returned answers
(both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your
function ( Looking at the function signature will make things clearer ).
Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there
are multiple solutions with the minimum index2, choose the one with minimum
index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_map = {}
        for i, num in enumerate(nums):
            if sum_map.get(target-num):
                return [sum_map[target-num]-1, i]
            sum_map[num] = i+1 # Adding 1 to have pointers from 1 to prevent sum_map.get return 0 which would falsify if if-loop even when input is returned. Ex: [3, 3], 6
        return [-1, -1]



# sum not unique
# 2 sum with sorting O(nlogn)
# working solution for above question
def two_sum_with_sorting(arr, target):
    from collections import defaultdict
    inp_map = defaultdict(list)  # {ele: [index1, index2]}
    possible_sol = []
    for index, ele in enumerate(arr):
        inp_map[ele].append(index)
    for index, ele in enumerate(arr):
        second_ele = target-ele
        for cur_index in inp_map[second_ele]:
            if cur_index != index and index < cur_index:
                possible_sol.append([index+1, cur_index+1])
    # Sort for min index2
    # index2_sorted_list = sorted(possible_sol, lambda: x x[1])
    if not possible_sol:
        return []
    elif len(possible_sol) == 1:
        return possible_sol[0]
    possible_sol.sort(key=lambda x: x[1])
    # if multiple combinations with same index2, sort on index1 for this subset
    if possible_sol[0][1] == possible_sol[1][1]:
        index1_sorted_list = [possible_sol[0]]
        index = 1
        while(index1_sorted_list[0][1] == possible_sol[index][1]):
            index1_sorted_list.append(possible_sol[index])
            index += 1
        index1_sorted_list.sort(key=lambda x: x[0])
        return index1_sorted_list[0]
    return possible_sol[0]


# if sum is unique, and input is unique
def two_sum_with_hash(arr, target):
    matches = []
    inp_map = {}  # {ele: index_of_ele in arr}
    for index in xrange(len(arr)-1, -1, -1):
        ele = arr[index]
        inp_map[ele] = index
    for index, ele in enumerate(arr):
        second_ele = inp_map.get(target-ele)
        if (second_ele is not None) and (index < second_ele):
            matches.append([index, second_ele])
    if len(matches) > 1:
        matches.sort(key=lambda match: match[1])
        if matches[0][1] == matches[1][1]:
            new_match_list = [matches[0]]
            i = 1
            while(i < (len(matches)-1) and matches[i][1] == matches[0][1]):
                new_match_list.append(matches[i])
                i += 1
            new_match_list.sort(key=lambda x: x[0])
            return [(new_match_list[0][0])+1, (new_match_list[0][1])+1]
        else:
            return [(matches[0][0])+1, (matches[0][1])+1]
    elif len(matches) == 0:
        return []
    else:
        return [(matches[0][0])+1, (matches[0][1])+1]


# naive O(n*n)
def two_sum(arr, target):
    n = len(arr)
    i = 0
    while(i < n):
        j = i + 1
        while(j < n):
            if (arr[i] + arr[j]) == target:
                return [i+1, j+1]
            j += 1
        i += 1
    return []

if __name__ == '__main__':
    # arr = [1, 1, 2]
    # target = 3
    # arr = [10, -3, 5, -7, -4, 5, 6, -7, 8, -5, 8, 0, 8, -5, -10, -1, 1, -6, 4, -1, -2, -2, 10, -2, -4, -7, 5, 1, 7, -10, 0, 5, 8, 6, -8, 8, -8, -8, 3, -9, -10, -5, -5, -10, 10, -4, 8, 0, -6, -2, 3, 7, -5, 5, 1, -7, 0, -5, 1, -3, 10, -4, -3, 3, 3, 5, 1, -2, -6, 3, -4, 10, -10, -3, -8, 2, -2, -3, 0, 10, -6, -8, -10, 6, 7, 0, 3, 9, -10, -7, 8, -7, -7]
    # target = -2
    # arr = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
    # target = -3
    # arr = [2, 2, 7, 7]
    # target = 9
    # arr = [1, 1, 1]
    # target = 2
    # print two_sum_with_hash(arr, target)
    # arr = [2, 7, 11, 15]
    # target = 9
    # arr = [ -10, -10, -10 ]
    # target = -5
    arr = [7, 2, -5, 10, -3, 4, 9, 1, -6, -10]
    target = 2
    print two_sum_with_sorting(arr, target)
