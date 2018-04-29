class Solution(object):
    def minCut(self, s):
        """
        check recursive version (bruteforce) for min cut too here:
        https://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/

        Time: O(n^2)
        Space: O(n)

        https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space/62
        The definition of 'cut' array is the minimum number of cuts of a sub string.
        More specifically, cut[n] stores the cut number of string s[0, n-1].

        Here is the basic idea of the solution:

        Initialize the 'cut' array: For a string with n characters s[0, n-1],
        it needs at most n-1 cut.
        cut[0] -> s[0, -1] # dummy to tell if
        cut[1] corresponds to string[0, 0] and since its just one char it needs 0 cuts to make it palindrome.
        Therefore, the 'cut' array is initialized as cut[i] = i-1

        When the loops finish, you'll get the answer at cut[s.length]
        """
        cut = range(-1, len(s))
        for idx in xrange(1, len(s)):
            for low, high in (idx, idx), (idx-1, idx): # odd and even palindromes respectively.
                while low >= 0 and high < len(s) and s[low] == s[high]:
                    # cut[high+1] is analogous to cut[i+j+1]
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low -= 1
                    high += 1
        return cut[-1]

    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def dfs(self, s, start, end):
        if start == end: return 0
        if self.is_palindrome(s, start, end):
            return 0
        min_cut = float('inf')
	for k in xrange(start, end):
            min_cut = min(min_cut, 1 + self.dfs(s, start, k) + self.dfs(s, k+1, end))
        return min_cut

    def min_cut_recursion(self, s):
	# Time: Perhaps O(2^n) since it try to put cut at every place in n locations b/w start and end.
        return self.dfs(s, 0, len(s)-1)



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
    ex: "aaaaaaaaa"
        """
        self.cur_pal_parts = []
        self.palindromic_parts = []
        self.get_palindromic_parts(0, given_str)
        return self.palindromic_parts


if __name__ == '__main__':
    print Solution().min_cut_recursion("aab")
