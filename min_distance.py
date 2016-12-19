import sys

n = int(raw_input().strip())
arr = [int(x) for x in raw_input().strip().split(' ')]
min_distance = sys.maxint
for i in xrange(n):
    for j in xrange(i+1, n):
        if arr[i] == arr[j]:
            if j-i < min_distance:
                min_distance = j-i

if min_distance!=sys.maxint:
    print min_distance
else:
    print -1
