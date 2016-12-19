import sys

max_until_here = max_so_far = -sys.maxint-1
for x in A:
    max_until_here = max(x, max_until_here)
    max_so_far = max(max_until_here, max_so_far)
print max_so_far
