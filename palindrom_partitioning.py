"""
Given a string s, partition s such that every string of the partition is a
palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
"""


class Solution(object):
    def generate_possible_subsets(self, target_str):
        power_set = [[]]
        for each in target_str:
            power_set = power_set + [each+cur_set for cur_set in target_str]
        return power_set

    def is_palindrome(self, target_str):
        left, right = 0, len(target_str)-1
        while(left < right):
            if target_str[left] != target_str[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition_palindrome(self, A):
        target_str = A
        power_set = self.generate_possible_subsets(target_str)
        palindromes = []
        for each_str in power_set:
            if self.is_palindrome(each_str):
                palindromes.append(each_str)
        return palindromes

if __name__ == '__main__':
    sol = Solution()
    target_str = 'aab'
    print sol.partition_palindrome(target_str)
