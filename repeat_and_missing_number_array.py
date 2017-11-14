import math

# array_sum = sum(a)
# sum_of_n = sum(range(n+1))
# product_of_array = 1
# product_of_n = 1
# for i in xrange(1,n+1):
#     product_of_array*=a[i-1]
#     product_of_n*=i
# repeating_num = math.ceil((sum_of_n - array_sum)/((product_of_n/product_of_array)-1))
# missing_num = sum_of_n - sum_of_array + repeating_nu
#A='1 2 3 3 4'

"""
3 alternate methods
http://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
Idea: https://stackoverflow.com/a/5767648/2795050
"""
# method 2
A = [int(x) for x in A.split(' ')]
n=len(A)
xor_inp_arr = 0
xor_num_range = 0
combined_xor = 0
right_most_set_bit = 0
set_a = set_b = 0
for ele in A:
    xor_inp_arr^=ele
for num in xrange(1, n+1):
    xor_num_range^=num
combined_xor = xor_inp_arr ^ xor_num_range
# finding rightmost set bit in combined_xor
right_most_set_bit = combined_xor & ~(combined_xor-1)
# dividing numbers to two sets based on right most set bit in combined_xor
for ele in A:
    if ele & right_most_set_bit:
        set_a=set_a^ele
    else:
        set_b=set_b^ele
for ele in xrange(1, n+1):
    if ele & right_most_set_bit:
        set_a=set_a^ele
    else:
        set_b=set_b^ele


print "Missing element is %d and repeating element is %d" % (set_b, set_a)

# method 1
# succeptible to stack overflows, so should be avoided
# https://stackoverflow.com/a/5767117/2795050
