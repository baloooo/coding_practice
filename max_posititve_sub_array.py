import sys

inp_arr = [int(x) for x in raw_input().strip().split(' ')]
max_so_far = max_ending_here = max_so_far_start_index = max_so_far_end_index = max_ending_here_starting_index = max_ending_here_ending_index =  0
for index, ele in enumerate(inp_arr):
    if ele>=0:
        if max_ending_here:
            max_ending_here+=ele
            max_ending_here_ending_index+=1
        else:
            max_ending_here=ele
            max_ending_here_starting_index=max_ending_here_ending_index=index
    else:
        if max_ending_here>max_so_far:
            max_so_far = max_ending_here
            max_so_far_starting_index = max_ending_here_starting_index
            max_so_far_ending_index = max_ending_here_ending_index
        elif max_ending_here == max_so_far:
            if (max_ending_here_ending_index -
                    max_ending_here_starting_index)>(max_so_far_ending_index -
                            max_so_far_starting_index):
                        max_so_far_starting_index = max_ending_here_starting_index
                        max_so_far_ending_index = max_ending_here_ending_index

        max_ending_here = 0

print "max so far is", max_so_far
print "max array is", inp_arr[max_so_far_starting_index:max_so_far_ending_index+1]
