class Solution:
    def permutation_sequence(self, n, k):
        from math import factorial
        arr = range(1, n+1)
        # find arr arrangement, and remaining k
        start = 0
        rep = factorial(n-1)
        if not k % rep:
            new_sequence_index = (k/rep)-1
            self.count = rep-1
        else:
            new_sequence_index = k/rep
            self.count = (k % rep)
        arr[0], arr[new_sequence_index] = arr[new_sequence_index], arr[0]

        def permutation(start, end):
            if start == end:
                if self.count != 0:
                    self.count -= 1
                print arr
                return
            else:
                for index in xrange(start, end):
                    arr[start], arr[index] = arr[index], arr[start]
                    permutation(index+1, end)
                    if not self.count:
                        print 'final arr', arr
                        return
                    arr[start], arr[index] = arr[index], arr[start]
        permutation(start, len(arr))
        return arr

if __name__ == '__main__':
    sol = Solution()
    n, k = 4, 10
    # n, k = 3, 4
    print sol.permutation_sequence(n, k)
