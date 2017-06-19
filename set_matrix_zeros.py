

class Solution:
    def __init__(self):
        pass

    def set_matrix_zero(self, arr):
        col0 = 1
        for row in xrange(len(arr)):
            if arr[row][0] == 0:
                col0 = 0
            for col in xrange(len(arr)):
                if arr[row][col] == 0:
                    arr[row][0] = 0
                    arr[0][col] = 0
        # start setting from bottom up way
        print arr
        for row in xrange(len(arr)-1, -1, -1):
            for col in xrange(len(arr)-1, -1, -1):
                if arr[row][0] == 0 or arr[0][col] == 0:
                    arr[row][col] = 0
            if col0 == 0:
                arr[row][0] = 0
        # for row in xrange(len(arr)):
        #     if arr[row][0] == 0:
        #         for col in xrange(len(arr)):
        #             arr[row][col] = 0
        # for col in xrange(len(arr)):
        #     if arr[col][0] == 0:
        #         for row in xrange(len(arr)):
        #             arr[row][col] = 0
        # if not col0:
        #     for row in xrange(len(arr)):
        #         arr[row][0] = 0
        #     for col in xrange(len(arr)):
        #         arr[0][col] = 0
        return arr

if __name__ == '__main__':
    test_cases = [
        ([[1, 0, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [1, 0, 1], [1, 0, 1]])
    ]
    for test_case in test_cases:
        res = Solution().set_matrix_zero(test_case[0][:])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
