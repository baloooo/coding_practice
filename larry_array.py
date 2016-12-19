n_tc = int(raw_input().strip())

for i in xrange(n_tc):
    n = int(raw_input().strip())
    arr = [int(x) for x in raw_input().strip().split(' ')]
    for index, ele in enumerate(arr[2:], start=2):
        if arr[index]<arr[index-1] and arr[index-2]<arr[index]:
            print "NO"
            break
    else:
        print "YES"
            


