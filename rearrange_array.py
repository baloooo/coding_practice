

class Solution:

    def rearrange(self, arr):
        '''
        Both are Time O(n) and O(1) space
        Can cause overflow, but simple formulae
        http://www.geeksforgeeks.org/rearrange-given-array-place/
        Detect all cycles and keep replacing
        http://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/
        '''
        n = len(arr)
        for i in xrange(n):
            '''
            arr[arr[i]]%n is to get the original value at arr[arr[i]] since this value
            might have already been bumped up. This happens when there is a cycle [0, 2, 1]
            Now initially idx 1 will bump up idx2, but when we get to idx we want it's original
            value to be used to get to idx1 to bump it.
            Notice this causes overflow so use the other one.
            '''
            arr[i] += (arr[arr[i]]%n)*n
        for i in xrange(n):
            arr[i] = arr[i]/n
        return arr

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
