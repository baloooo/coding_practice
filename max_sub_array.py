import sys

inp_arr = [int(x) for x in raw_input().strip().split(' ')]
max_ending_here = max_so_far = inp_arr[0]
for ele in inp_arr[1:]:
    max_ending_here = max(ele, ele+max_ending_here)
    max_so_far = max(max_so_far, max_ending_here)

print "max so far is", max_so_far
