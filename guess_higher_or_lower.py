# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber_binary_search(self, n):
        """
        :type n: int
        :rtype: int
        Apart from the solution for this case, this article also has a very nice
        implementation of ternary search, also explains why ternary search is not
        better than binary search.

		https://leetcode.com/problems/guess-number-higher-or-lower/solution/
        Checkout https://stackoverflow.com/questions/20512642/big-o-confusion-log2n-vs-log3n#20512708
        for difference b/w log2n and log3n and so on.
        """
        start, end = 1, n
        while start <= end:
            mid = start + (end-start)/2
            response = guess(mid)
            if response == 0:
                return mid
            elif response == -1:
                end = mid - 1
            else:
                start = mid + 1

    def guessNumber_ternary_search(self, n):
        start, end = 1, n
        while start <= end:
            mid1 = start + (end-start)/2
            mid2 = end - (end-start)/2

            response1 = guess(mid1)
            response2 = guess(mid2)

            if response1 == 0:
                return mid1
            elif response2 == 0:
                return mid2
            elif response1 == -1:
                end = mid1 - 1
            elif response2 == 1:
                start = mid2 + 1
            else:
                start = mid1 + 1
                end = mid2 - 1

    def get_cost(self, start, end):
        self.n += 1
        print self.n
        if start >= end:
            return 0

        min_cost = float('inf')

        for i in xrange((start+end)/2, end+1):
            left_half = self.min_cost_map[(start, i-1)] if self.min_cost_map.get((start, i-1)) else self.get_cost(start, i-1)
            right_half = self.min_cost_map[(i+1, end)] if self.min_cost_map.get((i+1, end)) else self.get_cost(i+1, end)
            cur_cost = i + max(left_half, right_half)
            min_cost = min(min_cost, cur_cost)

        self.min_cost_map[(start, end)] = min_cost

        return min_cost


    def getMoneyAmount(self, n):
        """
        Idea is very similar to brute force, just started storing calls already made and re-using their
        data.
        Time: since number of subarrays possible are O(n^2) which will be the number of method calls and also
        the number of entries in min_cost_map.
        https://math.stackexchange.com/questions/1194584/the-total-number-of-subarrays

        Revisit Bruteforce algo's time complexity and check it against permutations algo, since
        both have n! time complexity.

        Concept: https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84766/Clarification-on-the-problem-description.-Problem-description-need-to-be-updated-!!!
        """
        # min (cost(1, n) = cost(i) + max(cost(1, i-1), cost(i+1, n))) 1 <= i <= n
        self.n = 0 # this tells the number of calls made(to test time complexity)
        self.min_cost_map = {} # (start, end): min cost for guessing a no. in range start to end
        ret_val =  self.get_cost(1, n)
        print self.min_cost_map
        return ret_val

if __name__ == '__main__':
    n = 10
    print Solution().getMoneyAmount(n)
