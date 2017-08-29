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
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
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
