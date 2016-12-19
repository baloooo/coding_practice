n, k = [int(x) for x in raw_input().strip().split(' ')]

arr = [int(x) for x in raw_input().strip().split(' ')]
div_sum_pair = 0

for index, ele in enumerate(arr):
    for j in xrange(index+1, n):
        if ((ele + arr[j]) % k)==0:
            div_sum_pair+=1

print div_sum_pair
