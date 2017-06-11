"""
1211
"""
arr = '3 1 2 1 1'
arr = [int(x) for x in arr.split(' ')]
num = int(arr.pop(0))
result = [[] for _ in xrange(num+1)]
result[0] = arr
for res_index in xrange(1, num+1):
    cur_char, char_count  = arr[0], 1
    for index in xrange(1, len(arr)):
        if arr[index] != cur_char:
            result[res_index].append(char_count)
            result[res_index].append(cur_char)
            cur_char = arr[index]
            char_count = 1
        else:
            char_count+=1
    result[res_index].append(char_count)
    result[res_index].append(cur_char)
    arr = result[res_index][:]
# printing with even dots on both sides
from math import ceil
import sys
max_len = max(len(result[0]), len(result[-1]))*2
for cur_arr in result:
    dots = max_len - len(cur_arr)*2
    for dots_ahead in xrange(int(ceil(dots/2.0))):
        sys.stdout.write('.')
        # print('.', end='', sep='')
    for ele in cur_arr:
        print ele,
    for dots_ahead in xrange(dots/2):
        sys.stdout.write('.')
        # print('.', end='', sep='')
    print
print len(result[-1])
