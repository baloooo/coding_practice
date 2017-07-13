def selection_sort(arr):
    for i in xrange(len(arr)):
        max_ele = arr[i]
        max_index = i
        for j in xrange(i+1, len(arr)):
            if (str(arr[j])+str(max_ele))>(str(max_ele)+str(arr[j])):
                max_ele = arr[j]
                max_index = j
        print i, max_index
        arr[i], arr[max_index] = arr[max_index], arr[i]
        print "arr after iteration is", arr

    print ''.join(map(str, arr))

def largest_number(arr):
    """
    Idea is to concat strings and compare their ASCIIs to check which is smaller and bigger
    """
    nums = [str(x) for x in arr]
    # https://docs.python.org/3/howto/sorting.html#the-old-way-using-the-cmp-parameter
    nums.sort(cmp=lambda x,y: cmp(y+x, x+y))
    return ''.join(nums).lstrip('0') or '0'

if __name__ == '__main__':
    # arr = [54, 546, 548, 60]
    # arr = [12, 45, 92, 67]
    # arr = [3, 30, 34, 5, 9]
    # arr = [0, 0, 0]
    arr = [0, 1, 2]
    print arr
    # selection_sort(arr)
    print 'result ', largest_number(arr)
