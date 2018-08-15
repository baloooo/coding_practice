'''
https://www.geeksforgeeks.org/ugly-numbers/
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        Time: Max of (log2(n), log3(n), log5(n)) therefore log2(n)
        """
        if num in [0, 1]: return bool(num)
        while num % 2 == 0: num = num/2
        while num % 3 == 0: num = num/3
        while num % 5 == 0: num = num/5
        return num == 1

    def nthUglyNumber(self, n):
        """
        Idea is very similar to seive of eratosthesis.
        The fact that if 12 is a ugly number: 2*2*3, then multiplying 2 or 3 or 5 will
        definitely result in a ugly number since we're just bumping up the number of 2 or 3 or 5
        in a combination that already only has 2, 3, or 5.
        So the idea is to just start with one ugly number and keep multiplying it by
        2, 3, and 5  and pick the minimum of these since we need them in sorted order
        + it would also help in avoiding duplicates.
        http://www.geeksforgeeks.org/ugly-numbers/
        Good explanation in comments here: https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C++-DP-solution-with-short-explanation
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        next_i2 = ugly[i2] * 2
        next_i3 = ugly[i3] * 3
        next_i5 = ugly[i5] * 5
        for i in xrange(1, n):
            ugly.append(min(next_i2, next_i3, next_i5))
            if ugly[i] == next_i2:
                i2 += 1
                next_i2 = ugly[i2] * 2
            if ugly[i] == next_i3: # Note: These all are if and not elif
                i3 += 1
                next_i3 = ugly[i3] * 3
            if ugly[i] == next_i5:
                i5 += 1
                next_i5 = ugly[i5] * 5
        return ugly[-1]

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
	https://leetcode.com/problems/super-ugly-number/discuss/76330/Using-min-heap-Accepted-Java-and-Python-code
        """
        import heapq
        next_ugly_min_heap = []
        for prime in primes:
            next_ugly_min_heap.append((prime, 0, prime))
            
        heapq.heapify(next_ugly_min_heap)
        ugly_nums = [1]
        for _ in xrange(1, n):
            old_x, i, p = next_ugly_min_heap[0]
            ugly_nums.append(old_x)
            
            while next_ugly_min_heap and old_x == next_ugly_min_heap[0][0]:
                x, i, p = heapq.heappop(next_ugly_min_heap)
                heapq.heappush(next_ugly_min_heap, (p*ugly_nums[i+1], i+1, p))
        
        return ugly_nums[-1]
        

if __name__ == '__main__':
    test_cases = [
        ((12, [2,7,13,19]), 32),
    ]
    for test_case in test_cases:
        # res = Solution().nthUglyNumber(test_case[0])
        res = Solution().nthSuperUglyNumber(*test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
