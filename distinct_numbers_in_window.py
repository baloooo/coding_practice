# -*- coding: utf-8 -*-
"""
You are given an array of N integers, A1, A2 ,…, AN and an integer window_size.
Return the of count of distinct numbers in all windows of size window_size.

Formally, return an array of size N-window_size+1 where i’th element in this
array
contains number of distinct elements in sequence Ai, Ai+1 ,…, Ai+window_size-1.

Note:
- If window_size > N, return empty array.

For example,

A=[1, 2, 1, 3, 4, 3] and window_size = 3

All windows of size window_size are

[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]

So, we return an array [2, 3, 3, 2].
"""

def distinct_number_in_window(inp_arr, window_size):
    from collections import defaultdict
    # {number: number_count}
    if window_size > len(inp_arr):
        return []
    distinct_window_map = defaultdict(int)
    result = []
    for ele in inp_arr[:window_size]:
        distinct_window_map[ele] += 1
    for index, ele in enumerate(inp_arr[window_size:], start=window_size):
        result.append(len(distinct_window_map))
        distinct_window_map[inp_arr[index-window_size]] -= 1
        # remove ele that went out of the cur window in this iteration
        if distinct_window_map[inp_arr[index-window_size]] == 0:
            del distinct_window_map[inp_arr[index-window_size]]
        # add ele that came inside of the cur window in this iteration
        distinct_window_map[ele] += 1
    result.append(len(distinct_window_map))
    return result


if __name__ == '__main__':
    inp_arr = [1, 2, 1, 3, 4, 3]
    # inp_arr = [1, 1, 3, 4, 5]
    window_size = 3
    # print distinct_number_in_window(inp_arr, window_size)
    print distinct_number_in_window_set(inp_arr, window_size)
