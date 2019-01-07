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


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        '''
        This seems like better implemntation than the one below, though algos are same.
        '''
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

def largest_number(arr):
    """
    Idea is to concat strings and compare their ASCIIs to check which is smaller and bigger
    O(nlogn)
    Proof why this works, instead of str(num1) + str(num2) they mathemetically append it(by
    multiplying and then adding it).
    https://leetcode.com/problems/largest-number/solution/
    """
    nums = [str(x) for x in arr]
    # https://docs.python.org/3/howto/sorting.html#the-old-way-using-the-cmp-parameter
    '''
    That function should take two arguments to be compared and then return a negative value for
    less-than, return zero if they are equal, or return a positive value for greater-than
    '''
    # b'coz you need larger number first, therefore y+x first
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
