"""
Given a non-empty array containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both
subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def __init__(self):
        pass

    def canPartition(self, nums):
        """
        Time: O(KN) where N is number of element in nums and K is sum of elements in nums.
        Space: O((k+1)* (N+1))
        Idea: https://discuss.leetcode.com/topic/67539/0-1-knapsack-detailed-explanation
        http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
        Todo: Also return the partitions, asked on IB
        Has bunch of other variations too, http://www.cs.cornell.edu/~wdtseng/icpc/notes/dp3.pdf
        """
        target_sum = 0
        for num in nums:
            target_sum += num
        if (target_sum & 1) == 1:
            return False
        target_sum = target_sum/2
        dp = [[False for _ in xrange(len(nums)+1)] for _ in xrange(target_sum+1)]
        # zero sum can be made from any of denoms
        for col in xrange(len(nums)+1): dp[0][col] = True

        for cur_sum in xrange(1, target_sum+1):
            for cur_denoms in xrange(1, len(nums)+1):
                dp[cur_sum][cur_denoms] = dp[cur_sum][cur_denoms-1]
                if cur_sum >= nums[cur_denoms-1]:
                    dp[cur_sum][cur_denoms] = (
                        dp[cur_sum][cur_denoms-1] or
                        dp[cur_sum - nums[cur_denoms - 1]][cur_denoms-1])
        for row in dp:
            print row
        return dp[target_sum][len(nums)]

    def canPartitionKSubsets(self, nums, k):
        '''
        can be done by just recursion but not DP.
        https://discuss.leetcode.com/topic/107185/java-c-straightforward-dfs-solution
        '''
        pass


if __name__ == '__main__':
    arr = [1, 5, 11, 5]
    arr = [ 1, 7, 15, 29, 11, 9]
    print Solution().canPartition(arr)
