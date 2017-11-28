"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""
# Key points:
#    Logic: two pointers, closest refers to absolute distance between current sum and target
# Time complexity: O(nlogn) + O(n^2) = O(n^2)


def three_sum(arr, target):
    '''
Actually would be nice idea to use nsum logic from 4 sum here, so as to have minimum overlap and additional
data to keep.
'''
    arr.sort()
    closest_sum = float('inf')
    if len(arr) <= 3:
        return sum(arr)
    for base_index in xrange(len(arr)):
        front = base_index + 1
        rear = len(arr) - 1
        while(front < rear):
            cur_sum = arr[front]+arr[rear]+arr[base_index]
            if cur_sum == target:
                return target
            cur_distance = abs(cur_sum - target)
            if cur_distance < abs(target-closest_sum):
                closest_sum = cur_sum
            if cur_sum > target:
                rear -= 1
            else:
                front += 1
    return closest_sum

if __name__ == '__main__':
    # arr, target = [1, 2, 3, 4, 5, 6, 7], 18
    # arr, target = [-1, 2, 1, -4], 1
    arr, target = [7, -6, 2, 10], 3
    print three_sum(arr, target)
