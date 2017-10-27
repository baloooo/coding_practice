class Solution(object):
    def find_combinations(self, arr, start, remaining_sum):
        if remaining_sum < 0:
            return
        if remaining_sum == 0:
            self.combs.append(self.cur_comb[::])
        else:
            for index in xrange(start, len(arr)):
                self.cur_comb.append(arr[index])
                self.find_combinations(arr, index, remaining_sum-arr[index])
                self.cur_comb.pop()
        
    def combinationSum(self, candidates, target):
        """
        The input of Combination Sum has no dups, but each element can be used for MORE than one time.
        Time: check kamyu and https://discuss.leetcode.com/topic/25900/if-asked-to-discuss-the-time-complexity-of-your-solution-what-would-you-say/8
        """
        self.combs = []
        self.cur_comb = []
        self.find_combinations(candidates, 0, target)
        return self.combs


class Solution(object):
    def find_combinations(self, arr, start, remaining_sum):
        if remaining_sum < 0:
            return
        if remaining_sum == 0:
            #self.cur_comb.sort()
            #if self.cur_comb not in self.combs:
            self.combs.append(self.cur_comb[::])
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
