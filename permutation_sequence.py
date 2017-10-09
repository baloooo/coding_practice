class Solution:
    def permutation_sequence(self, n, k):
        """
        Time: O(n^2) Space: O(n)
        Idea: https://discuss.leetcode.com/topic/17348/explain-like-i-m-five-java-solution-in-o-n
        """
        from math import factorial
        res, arr, k = [], range(1, n+1), k-1
        for i in xrange(1, n+1):
            cur_index = k/factorial(n-i)
            res.append(arr[cur_index])
            del arr[cur_index]
            k = k % factorial(n-i)
            k = k - cur_index * factorial(n-i)  # Number of items we've counted already when including arr[cur_index]
        return res

    def permutation_sequence2(self, n, k):
        from math import factorial
        arr = range(1, n+1)
        # find arr arrangement, and remaining k
        rep = factorial(n-1)
        if k % rep == 0:
            if k/rep == 0:
                swap_index = 0
            else:
                swap_index = (k/rep)-1
        else:
            swap_index = k/rep
        self.count = (k % rep)
        arr[0], arr[swap_index] = arr[swap_index], arr[0]
        # print 'arr: {0} ,swap_index: {1}, count: {2}'.format(
        #    arr, swap_index, self.count)

        def permute(start, end):
            if start == end:
                self.count -= 1
                print arr
                return
            else:
                for index in xrange(start, end):
                    arr[start], arr[index] = arr[index], arr[start]
                    permute(start+1, end)
                    if not self.count:
                        return
                    arr[start], arr[index] = arr[index], arr[start]
        permute(0, len(arr))
        return arr

if __name__ == '__main__':
    sol = Solution()
    n, k = 4, 11
    # n, k = 3, 2
    # n, k = 2, 2
    # n, k = 1, 1
    n, k = 4, 14
    print sol.permutation_sequence(n, k)
