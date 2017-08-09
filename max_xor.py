class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        mask = 0
        for i in range(32)[::-1]:
            # The mask will grow like  100..000 , 110..000, 111..000,  then 1111...111
            # for each iteration, we only care about the left parts
            mask = mask | (1<<i)
            # we only care about the left parts, for example, if i = 2, then we have
            #   {1100, 1000, 0100, 0000} from {1110, 1011, 0111, 0010}*/
            interested_bits_nums_set = {num & mask for num in nums}
            next_max_xor = max_xor | (1 << i)
            """
            This is the most tricky part, coming from a fact that if a ^ b = c, then a ^ c = b;
            now we have the 'c', which is greedyTry, and we have the 'a', which is leftPartOfNum
            If we hope the formula a ^ b = c to be valid, then we need the b, 
            and to get b, we need a ^ c, if a ^ c exisited in our set, then we're good to go
            """
            for num in interested_bits_nums_set:
                if (next_max_xor ^ num) in interested_bits_nums_set:
                    max_xor = next_max_xor
                    break
        return max_xor

if __name__ == '__main__':
    test_cases = [
        ([3, 10, 5, 25, 2, 8], 28),
    ]
    for test_case in test_cases:
        res = Solution().findMaximumXOR(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
