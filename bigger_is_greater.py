import sys

n = int(raw_input().strip())

for i in xrange(n):
    arr = [ord(i) for i in raw_input().strip()]
    i=len(arr)-1
    while(i-1>=0):
        if arr[i]>arr[i-1]:
            pivot = arr[i-1]
            pivot_index = i-1
            break
        i-=1
    else:
        print "no answer" 
        continue
    min_index=len(arr)-1
    i=len(arr)-1
    while(i>pivot_index):
        if arr[i] and arr[i]>pivot:
            min_index = i 
            break
        i-=1
    arr[pivot_index] = arr[min_index]
    arr[min_index] = pivot
    b = arr[pivot_index+1:]
    arr = arr[:pivot_index+1] + b[::-1]
    for i in arr:
        sys.stdout.write(chr(i))
    print
