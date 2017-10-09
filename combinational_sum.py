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
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.combs = []
        self.cur_comb = []
        self.find_combinations(candidates, 0, target)
        return self.combs
