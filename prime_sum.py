class Solution:
    '''
    Seive of eratosthenes:
    From: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    The sieve of Eratosthenes is a popular way to benchmark computer performance.[14]
    As can be seen from the above by removing all constant offsets and constant factors and ignoring terms that tend to zero as n approaches infinity, the time complexity of calculating all primes below n in the random access machine model is O(n log log n) operations, a direct consequence of the fact that the prime harmonic series asymptotically approaches log log n.
    https://stackoverflow.com/questions/2582732/time-complexity-of-sieve-of-eratosthenes-algorithm
    '''
    def find_prime_numbers(self, A):
        '''
        Seive of Erato: O(n(loglogn))
        '''
        prime_numbers = []
        num_range = [False]*(A-1)
        for index, cur_num in enumerate(num_range, start=2):
            if cur_num is False:
                prime_numbers.append(index+2)
                i = 2
                while(index*i <= A):
                    num_range[index*i-2] = True
                    i += 1
        return prime_numbers

    def prime_nos(self, upper_limit):
        '''
        same as above, but more straight forward since we don't offset for 2
        and therefore easy calculation at every step.
        '''
        mask = [False]*(upper_limit+1)
        primes = []
        for i in xrange(2, upper_limit):
            if mask[i] is False:
                primes.append(i)
                j = 2
                while i*j <= upper_limit:
                    mask[i*j] = True
                    j += 1
        return primes

    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        O(O(seive) + O(two_sum))
        prime_numbers = self.find_prime_numbers(A)
        '''
        once you have prime numbers, problem breaks down to finding two numbers whose sum is x
        can be done w/ O(nlogn) and constant space or O(n) time with O(n) space hashing.
        '''
        for index, prime1 in enumerate(prime_numbers):
            for prime2 in prime_numbers[index:]:
                if prime1 + prime2 == A:
                    return [prime1, prime2]

if __name__ == '__main__':
    sol_obj = Solution()
    # print sol_obj.primesum(16777214)
    print sol_obj.prime_nos(20)
