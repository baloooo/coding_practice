'''
Single number generalization
https://discuss.leetcode.com/topic/11877/detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
Problem Statement: Given an array of integers, every element appears k (k > 1) times except for one, which appears p times (p >= 1, p % k != 0). Find that single one."
The idea can be broken down in to following steps:
    1. Find what operator to use for counting the number of ones at each index for all nums in arr
    2. How to move counter x2 = x2 ^ (x1 & i), x2 will have a one only when all the previous bits
       are 1 else changing x1 from zero to 1 should be suffice.
    3. Since #f xm variables can count upto 2^m-1 and k can be less than 2^m-1, we have to come
       up with a way to reinitialize counter to zero once it reaches k rather letting it go above k       k to 2^m-1.
    Todo: 3. is not very clear, look in to general case with 32-bit #s, confirm logic with examples
'''


class Solution:
    def single_number(self, arg):
        pass

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
