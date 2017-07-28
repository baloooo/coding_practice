"""
Problem statement:
    Given an array of integers, every element appears thrice except for one
    which occurs once.

    Find that element which does not appear thrice.

    Note: Your algorithm should have a linear runtime complexity.

    Could you implement it without using extra memory?

    Example :

    Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    Output : 4
"""


def unique_number(arr):
    num_weight_arr = [0]*32
    unique_num = 0
    for current_num in arr:
        for pos in xrange(32):
            if (1 << pos) & current_num:
                num_weight_arr[pos] += 1
    import ipdb; ipdb.set_trace()
    for pos, each in enumerate(num_weight_arr):
        if each % 3 != 0:
            unique_num = unique_num | (1 << pos)
    # print "num_weight_arr is ", num_weight_arr
    return unique_num


def unique_number_with_negative(nums):
    result = 0
    for pos in range(32):
        mask = 1 << pos
        cur_pos_sum = 0
        for num in nums:
            if num & mask:
                cur_pos_sum += 1
        if cur_pos_sum % 3:
            result |= mask
    return result

if __name__ == '__main__':
    # arr = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    # arr = [2, 2, 3, 2]
    arr = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    print unique_number(arr)
    # print unique_number_with_negative(arr)
