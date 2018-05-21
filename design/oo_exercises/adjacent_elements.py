

class Solution:
    def __init__(self):
        pass

    def my_func(self, arr):
        if len(arr) < 2: return -1
        index_val_arr = []
        for index, ele in enumerate(arr):
            index_val_arr.append((index, ele))
        index_val_arr.sort(key=lambda x: x[1]) # O(nlogn)
        max_diff = -float('inf')
        prev = index_val_arr[0]
        for index in xrange(1, len(index_val_arr)):
            if (index +1) < len(arr) and index_val_arr[index][1] != index_val_arr[index+1][1] and prev[1] != index_val_arr[index][1]:
                max_diff = max(max_diff, abs(prev[0] - index_val_arr[index][0]))
                prev = index_val_arr[index]
        else:
            max_diff = max(max_diff, abs(prev[0] - index_val_arr[-1][0])) if prev[1] != index_val_arr[-1][1] else -1
        return max_diff

    # def my_func2(self, arr):
    #     if len(arr) < 2: return -1
    #     index_val_arr = []
    #     for index, ele in enumerate(arr):
    #         index_val_arr.append((index, ele))
    #     index_val_arr.sort(key=lambda x: x[1]) # O(nlogn)
    #     max_diff = -float('inf')
    #     prev_index, cur_index = 0, 1
    #     while cur_index < len(arr):
    #         while index_val_arr[cur_index] 


    #     prev = index_val_arr[0]
    #     for index in xrange(1, len(index_val_arr)):
    #         if (index +1) < len(arr) and index_val_arr[index][1] != index_val_arr[index+1][1]:
    #             max_diff = max(max_diff, abs(prev[0] - index_val_arr[index][0]))
    #             prev = index_val_arr[index]
    #     else:
    #         import ipdb; ipdb.set_trace()
    #         max_diff = max(max_diff, abs(prev[0] - index_val_arr[-1][0])) if prev[1] != index_val_arr[-1][1] else -1
    #     return max_diff


if __name__ == '__main__':
    test_cases = [
        ([0, 3, 3, 7, 5, 3, 11, 1], 7),
        ([1, 4, 7, 3, 3, 5], 4),
        ([1], -1),
        ([1, 1], -1),
        ([1, 1, 1, 1, 1], -1),
        ([1, 1, 1, 1, 2], 4),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])

'''
[1, 1, 1, 1, 1, 1, 1], 7
[1, 2, 2, 2, 2], 5
[1, 1, 1, 1, 2], 5
[1], 1
[], 0
[1, 2, 2, 2, 1], 5
[2, 2, 1], 3
[2, 1], 2
[1, 2], 2
[1, 2, 3, 4, 5], 2
'''
