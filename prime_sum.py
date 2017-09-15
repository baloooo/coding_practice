class Solution:
    '''
    Seive of eratosthesis:
    From: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    The sieve of Eratosthenes is a popular way to benchmark computer performance.[14] As can be seen from the above by removing all constant offsets and constant factors and ignoring terms that tend to zero as n approaches infinity, the time complexity of calculating all primes below n in the random access machine model is O(n log log n) operations, a direct consequence of the fact that the prime harmonic series asymptotically approaches log log n.
    https://stackoverflow.com/questions/2582732/time-complexity-of-sieve-of-eratosthenes-algorithm
    '''
    def find_prime_numbers(self, A):
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

    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        prime_numbers = self.find_prime_numbers(A)
        print prime_numbers
        for index, prime1 in enumerate(prime_numbers):
            for prime2 in prime_numbers[index:]:
                if prime1 + prime2 == A:
                    return [prime1, prime2]

if __name__ == '__main__':
    sol_obj = Solution()
    print sol_obj.primesum(16777214)
