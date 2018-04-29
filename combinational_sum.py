'''
https://leetcode.com/problems/combination-sum-iv/discuss/85120/C++-template-for-ALL-Combination-Problem-Set
'''
class Solution(object):
    def combinationSum4_recursive(self, arr, target):
        """
        
        """
        res = 0
        if target == 0:
            return 1
        else:
            for i in xrange(len(arr)):
                res += self.combinationSum4(arr, target-arr[i])
        return res

    def combinationSum4_dp(self, arr, target):
        '''
        https://discuss.leetcode.com/topic/52302/1ms-java-dp-solution-with-detailed-explanation/43
        '''
	public int combinationSum4(int[] nums, int target) {
	    int[] dp = new int[target + 1];
	    dp[0] = 1;
	    for(int i = 1; i <= target; i++){
	      for(int j = 0; j < nums.length; j++){
		 if(i - nums[j] >= 0){
		   dp[i] += dp[i - nums[j]];  
		 }  
	      }  
	    }  
	    return dp[target];  
        }
        
    def find_combinations(self, arr, start, remaining_sum):
        if remaining_sum == 0:
            self.combs.append(self.cur_comb[:])
        else:
            for index in xrange(start, len(arr)):
                if arr[index] <= remaining_sum:
                    self.cur_comb.append(arr[index])
                    self.find_combinations(arr, index, remaining_sum-arr[index])
                    self.cur_comb.pop()

    def combinationSum(self, candidates, target):
        """
        Idea is same as coin change 2 exercise with the only difference that dp can
        tell you the number of ways to find the combination but not the combinations themselves.
        For that you'll have to do recursion perhaps.
        The input of Combination Sum has no dups, but each element can be used
        for MORE than one time.
        Time: https://discuss.leetcode.com/topic/25900/if-asked-to-discuss-the-time-complexity-of-your-solution-what-would-you-say/8
        """
        self.combs = []
        self.cur_comb = []
        self.find_combinations(candidates, 0, target)
        return self.combs


class Solution2(object):
    def find_combinations(self, arr, start, remaining_sum):
        if remaining_sum < 0:
            return
        if remaining_sum == 0:
            #self.cur_comb.sort()
            #if self.cur_comb not in self.combs:
            self.combs.append(self.cur_comb[:])
        else:
            for index in xrange(start, len(arr)):
                if index > start and arr[index] == arr[index-1]:
                    continue
                self.cur_comb.append(arr[index])
                self.find_combinations(arr, index+1, remaining_sum-arr[index])
                self.cur_comb.pop()

    def combinationSum2(self, candidates, target):
        """
        The input of Combination Sum II has dups, but each element can be used ONCE.
        https://discuss.leetcode.com/topic/25900/if-asked-to-discuss-the-time-complexity-of-your-solution-what-would-you-say/8
        Time: O(k * 2^n) where k is the avg. length of the combination, and n is the lenght of candidates
        """
        self.combs = []
        self.cur_comb = []
        candidates.sort()
        self.find_combinations(candidates, 0, target)
        return self.combs
