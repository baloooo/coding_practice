class Solution(object):
    def backtrack(self, n, k, start, cur, res):
        if k == 0:
            res.append(cur[:])
            return
        # n - k + 2 since we want a window extending from start to k places where start starts from 1 and goes until n
        # [1, 2, 3, 4] n = 4, k = 2, start can go from 1 to 4 where 4th iteration is just used to add values as that makes
        # k zero.
        for index in xrange(start, n-k+2):
            cur.append(index)
            self.backtrack(n, k - 1, index + 1, cur, res)
            cur.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Idea: http://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
        Fix elements and recur
        instead of n we can also be given an array out of which k elements need to selected and returned
        Also that arr can have duplciates, and can be easily dealt with
        // Since the elements are sorted, all occurrences of an element
        // must be together
        while (arr[i] == arr[i+1])
             i++
        """
	res = []
        # start is initialized as 1 since these are the values of arr [1, 2, 3, 4] not the indexes
	self.backtrack(n, k, 1, [], res)
	return res
        

    def combine_dp(self, n, k):
        '''
        https://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
        '''
        pass

if __name__ == '__main__':
    n, k = 5, 3
    n, k = 4, 2
    n, k = 0, 2
    n, k = 4, 2
    print Solution().combine(n, k)
