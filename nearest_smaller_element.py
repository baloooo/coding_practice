"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

Input : A : [4, 5, 2, 10]
Return : [-1, 4, -1, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
"""


class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prev_smaller(self, arr):
        """
        S = new empty stack data structure
        for x in the input sequence:
            while S is nonempty and the top element of S is greater than or equal to x:
                pop S
            if S is empty:
                x has no preceding smaller value
            else:
                the nearest smaller value to x is the top element of S
            push x onto S
        https://stackoverflow.com/questions/9493853/given-an-array-find-out-the-next-smaller-element-for-each-element
        """
        stack = []
        res_arr = []
        for ele in arr:
            if stack:
                while stack and ele <= stack[-1]:
                    stack.pop()
                if stack:
                    res_arr.append(stack[-1])
                else:
                    res_arr.append(-1)
            else:
                res_arr.append(-1)
            stack.append(ele)
        return res_arr

if __name__ == '__main__':
    test_cases = [
        ([34, 35, 27, 42, 5, 28, 39, 20, 28], [-1, 34, -1, 27, -1, 5, 28, 5, 20])
    ]
    for test_case in test_cases:
        res = Solution().prev_smaller(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
