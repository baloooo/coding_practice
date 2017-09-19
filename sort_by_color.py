def sortColors(nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

if __name__ == '__main__':
    arr = [2, 1, 0]
    sortColors(arr)
    print arr
