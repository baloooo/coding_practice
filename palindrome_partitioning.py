"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def is_palindrome(self, target_str, start_index, end_index):
        front, back = start_index, end_index
        while front < back:
            if target_str[front] != target_str[back]:
                break
            front += 1
            back -= 1
        else:
            return True
        return False

    def get_palindromic_parts(self, start, given_str):
        if start == len(given_str):
            self.palindromic_parts.append(self.cur_pal_parts[::])
        else:
            for index in xrange(start, len(given_str)):
                if self.is_palindrome(given_str, start, index):
                    self.cur_pal_parts.append(given_str[start:index+1])
                    # Standard DFS approach
                    self.get_palindromic_parts(index+1, given_str)
                    self.cur_pal_parts.pop()
                    
    def partition(self, given_str):
        """
        :type s: str
        :rtype: List[List[str]]
	Idea: https://discuss.leetcode.com/topic/6186/java-backtracking-solution/24
	Time: O(n*2^n) You are basically trying out every possible partition out there.
	For a string with length n, you will have 2^(n - 1) ways to partition it.
	This is because, a partition is equivalent of putting a "|" in b/t two chars.
	There are n - 1 such slots to place a "|". There are only two choice for each
	slot - placing a "|" or not placing a "|". Thus 2^(n - 1) ways to place "|"s.

	Then for each unique partitioning, you have to traverse the entire string
	(in the worst case when you have repeating chars) to make sure every partition
	is a palindrome. so n * 2 ^ (n - 1) = O(n*2^n).
	Space: O(2^n) As there can be max of 2^n partitions, so to store each one of them
        """
        self.cur_pal_parts = []
        self.palindromic_parts = []
        self.get_palindromic_parts(0, given_str)
        return self.palindromic_parts
