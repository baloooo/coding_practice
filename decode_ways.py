"""
https://discuss.leetcode.com/topic/35840/java-clean-dp-solution-with-explanation/14
Notice this is very similar to climbing stairs exercise wherever one of the two available
step options is further tied with a decision whether it forms a valid number b/w 10 and 26.
And on another level this further can be boiled down to fibonacci sequence which has a more
space optimized form implemented in decode_optimized method here.
"""

class Solution:
    def decode_ways(self, s, n):
        if n == 0 or n == 1:
            return 1
        count = 0
        if s[n-1] != '0':
            count = self.decode_ways(s, n-1)
        if s[n-2] == '1' or (s[n-2] == '2' and '0' <= s[n-1] <= '6'):
            count += self.decode_ways(s, n-2)
        return count

    def decode_recursion(self, s)
        """
        http://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
        This is just to give you a sense of basic recursion on top of which DP comes along.
        """
        n = len(s)
        '''Since string can have leading zeros or or anyother malformed string we check for all of them here
        and only pass on to main recursion when it seems valid atleast from the prefix part(having trailing zeros is not dealt here)
        '''
        if n == 0:
            return 0
        if s[0] == '0': # String is treated "invalid" if starts with zeroes
            return 0
        if n <= 0:
            return 0
        if n == 1: # For one length string
            if s[n-1] != '0':
                return 1
            else:
                return 0
        return self.decode_ways(s, len(s)) # For string lenght > 1
        

    def decode_optimized(self, s):
        """
        Time: O(len(s))
        Space optimized: O(1)
        """
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        cur = 0
        prev_prev = 1
        prev = 1 if s[0] != '0' else 0
        for i in xrange(2, len(s)+1):
            """
            Notice similar to dp, you start with base line at start
            of every iteration therefore remember to revert back cur to zero
            and update it's value based on values fetched from previous steps
            """
            cur = 0 # Note: This is the most important step. You need to bring cur back to zero at every iter
            if s[i-1] != '0':
                cur += prev
            if '10' <= s[i-2:i] <= '26':
                cur += prev_prev
            prev, prev_prev = cur, prev
        return cur

    def decode(self, s):
        """
        Time: O(len(s))
        Space : O(len(s))
        """

        # Deal with corner case of zero and one length strings
        # Note: s[0] = '0' makes the string invalid
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # Note: The size of dp array is n+1 here since we get no. of ways we can decode digits up to nth index will be stored at n+1 index of the array.
        dp = [0]*(len(s)+1)
        # dp[1] tells number of ways s[0] can be decoded, dp[2] tells no_of_ways s[0],s[1] can be decoded and so on.
        dp[0] = dp[1] = 1
        for i in xrange(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if s[i-2] == '1' or ('1' <= s[i-2: i] <= '26'):
                dp[i] += dp[i-2]
        return dp[len(s)]

if __name__ == '__main__':
    test_cases = [
        ('12', 2),
        ('0', 0),
        ('27', 1),
        ('100', 0),
    ]
    for test_case in test_cases:
        res = Solution().decode_optimized(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
