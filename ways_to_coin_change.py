

class Solution:
    def __init__(self):
        pass

    def ways_to_coin_change(self, denoms, total_sum):
        self.dp = [0 for _ in xrange(total_sum+1)]
        self.dp[0] = 0
        total_ways = self.count(denoms, 0, total_sum)
        return total_ways if total_ways else -1

    def count(self, denoms, index, total_sum):
        print 'index: %d, total_sum remaining: %d' % (index, total_sum)
        if self.dp[total_sum]:
            return self.dp[total_sum]
        # no more coins left
        if index == len(denoms):
            return 0
        # target sum acheived
        if total_sum == 0:
            return 1
        # adding this coin surpasses target sum, so don't include
        if total_sum < 0:
            return 0
        return (self.count(denoms, index+1, total_sum) +
                self.count(denoms, index, total_sum-denoms[index]))

if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3], 4), 4),
        (([2, 5, 3, 6], 10), 5),
    ]
    for test_case in test_cases:
        res = Solution().ways_to_coin_change(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
