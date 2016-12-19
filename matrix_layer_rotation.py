m, n, rotations = [int(x) for x in raw_input().strip().split(' ')]
arr = []
layers = []
for i in xrange(m):
    arr.append([int(x) for x in raw_input().strip().split(' ')])
print "initial arr is", arr 
for r in xrange(rotations):
    for i in xrange(m/2):
        if not i:
            layers.append(arr[i][i:])
        else:
            layers.append(arr[i][i:-(i)])
        for each in arr[i+1:-(i+1)]:
            layers[i].append(each[-(i+1)])
        for each in arr[-(i+1)][::-1]: layers[i].append(each)
        for each in arr[i+1:-1][::-1]:
            layers[i].append(each[i])
for each in layers:
    print each
