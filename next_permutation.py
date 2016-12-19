arr = [1, 2, 3, 6, 5, 4]
target_index = -1
for i in xrange(len(arr)-1):
    if arr[i]>arr[i+1]:
        target_index = i
        break
else:
    print arr[::-1]
    exit()
arr = arr[0:target_index]+arr[target_index:][::-1]
arr[index-1], arr[target_index] = arr[target_index], arr[target_index-1]
print arr
