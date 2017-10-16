"""
https://discuss.leetcode.com/topic/35840/java-clean-dp-solution-with-explanation/14
Notice this is very similar to climbing stairs exercise wherever one of the two available
step options is further tied with a decision whether it forms a valid number b/w 10 and 26.
And on another level this further can be boiled down to fibonacci sequence which has a more
space optimized form implemented in decode_optimized method here.
"""

class Solution:

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
            cur = 0
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
        dp[0] = 1  # since we've already established above s[0] != '0'
        dp[1] = 1 if s[0] != '0' else 0 # dp[1] tells number of ways s[0] can be decoded, dp[2] tells no_of_ways s[0],s[1] can be decoded and so on.
        for i in xrange(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if '10' <= s[i-2:i] < '27':
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
