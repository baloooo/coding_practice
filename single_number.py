"""
Problem statement:
    Given an array of integers, every element appears twice except for one. Find that single one.

    Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example :

    Input : [1 2 2 3 1]
    Output : 3
"""


def find_num(arr):
    final_num = arr.pop()
    for num in arr:
        final_num = ((final_num & ~num) | (~final_num & num))
    return final_num

if __name__ == '__main__':
    print find_num([1, 2, 2, 3, 1])
