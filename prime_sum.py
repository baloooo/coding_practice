class Solution:
    def find_prime_numbers(self, A):
        prime_numbers = []
        num_range = [False]*(A-1)
        for index, cur_num in enumerate(num_range, start=2):
            if cur_num==False:
                prime_numbers.append(index+2)
                i=2 
                while(index*i<=A):
                    num_range[index*i-2]=True
                    i+=1
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
