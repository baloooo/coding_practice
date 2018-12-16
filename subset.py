"""
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
"""
class Solution(object):
    """
    Time: O(2^n)
    Space: O(n + 2^n) = O(n) as max depth of recursive tree/stack will be when all elements are added to get the
    set consisting of all elements, the other 2^n for storing 2^n lists each being a set in the power set.
    """
    def backtrack(self, nums, result, cur_subset, start):
        result.append(cur_subset[:])
        for index in xrange(start, len(nums)):
            if index > start and nums[index] == nums[index-1]:
                continue
            cur_subset.append(nums[index])
            self.backtrack(nums, result, cur_subset, index+1)
            cur_subset.pop()

    def subsetsWithDup(self, nums):
        result, cur_subset = [], []
        nums.sort()
        self.backtrack(nums, result, cur_subset, 0)
        return result

class Solution2(object):
    def backtrack(self, nums, result, cur_subset, start):
        result.append(cur_subset[:])
        for index in xrange(start, len(nums)):
            cur_subset.append(nums[index])
            self.backtrack(nums, result, cur_subset, index+1)
            cur_subset.pop()
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Must see Visualization of the idea in comments @jeremy:
            https://discuss.leetcode.com/topic/46159/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/26
        """
        result, cur_subset = [], []
        self.backtrack(nums, result, cur_subset, 0)
        return result

################################################################################################

def subset_without_duplicates_iteratively(arr):
    res = [[]]
    for ele in arr:
        res = res + [each+[ele] for each in res]
    return res


if __name__ == "__main__":
    inp_arr = [1, 2, 3]
    # inp_arr = [1]
    # inp_arr = []
    # inp_arr = [1, 2, 3, 4]
    # inp_arr = [1, 1, 2]
    # inp_arr = [1, 1]
    # inp_arr = [3, 2, 1]
    # inp_arr = [3, 2, 2, 1]
    # inp_arr = [4, 4, 3, 2]
    # inp_arr = [4, 3, 2, 1, 1]
    # print subset_without_duplicates(inp_arr)
    # print subset_duplicate_allowed(inp_arr)
    # inp_arr = [4, 4, 4, 1, 4]
    print Solution2().subsets(inp_arr)
