class Solution(object):
    def _lis(self, nums, prev, cur_pos):
        if cur_pos == len(nums):
            return 0
        taken = 0
        if prev < nums[cur_pos]:
            taken = 1 + self._lis(nums, nums[cur_pos], cur_pos+1)
        
        not_taken = self._lis(nums, prev, cur_pos+1)
        return max(taken, not_taken)
    
    def lengthOfLIS(self, nums):
        """
        https://leetcode.com/problems/longest-increasing-subsequence/solution/
        At every position you can either take the element or not(for an sorted order) this will
        be akin to binary representation of numbers up to length n which have time complexity
        O(2**n)
        :type nums: List[int]
        :rtype: int
        """
        return self._lis(nums, -float('inf'), 0)

########################################################################################################

    def lengthOfLIS_dp(self, nums):
        '''
        Idea: check all subsequences similar to checking all subarrays.
        for each j in i (subarray scan) get max len of subsequence seen before, which has its num
        less than current num(as we want to attach our num in front)

            Time: O(n^2) as loops are similar to finding all subarrays
            Space: O(n)

        Todo: There is a O(nlogn) solution using B.search too.
            '''
        if len(nums) == 0: return 0
        dp = [0]*len(nums)
        dp[0] = 1

        max_len = 1

        for i in xrange(1, len(nums)):
            max_len_for_i = 0
            for j in xrange(0, i):
                if nums[j] < nums[i]:
                    max_len_for_i = max(max_len_for_i, dp[j])

            dp[i] = max_len_for_i + 1
            max_len = max(max_len, dp[i])

        return max_len


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print Solution().lengthOfLIS(nums)
