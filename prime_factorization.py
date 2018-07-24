'''
https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
Prime factors of a number can be caluculated using Seive of Erato, which takes O(n loglogn) time and O(n) space, for finding all prime numbers up untill n.
Time complexity is such b'coz of https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes, seive of erato follows sum of reciprocals of prime nos. which has this time complexity.
'''


class Solution:
    def __init__(self):
        pass

    def get_seive(self, n):
        # https://www.geeksforgeeks.org/least-prime-factor-of-numbers-till-n/
        # puts least prime factor for each number up untill n
        seive = [0] * (n+1) # [0, 1, 0, 0, 0....]
        seive[1] = 1
        for i in xrange(2, n+1):
            if seive[i] == 0:
                seive[i] = i
                for j in xrange(2*i, n+1, i):
                    if seive[j] == 0:
                        seive[j] = i
        return seive

    def prime_factorization(self, n):
        '''
        Time: O(nloglogn) + O(logn)
        Space: O(n)
        '''
        seive = self.get_seive(n)
        prime_factors = []
        while n != 1:
            prime_factors.append(seive[n])
            n = n / seive[n]
        return prime_factors



if __name__ == '__main__':
    test_cases = [
        (36, [2, 2, 3, 3]),
        (101, [101]),
    ]
    for test_case in test_cases:
        res = Solution().prime_factorization(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
