class Solution(object):
    def minCut(self, s):
        """
        https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space/62
        The definition of 'cut' array is the minimum number of cuts of a sub string.
        More specifically, cut[n] stores the cut number of string s[0, n-1].

        Here is the basic idea of the solution:

        Initialize the 'cut' array: For a string with n characters s[0, n-1],
        it needs at most n-1 cut.
        Therefore, the 'cut' array is initialized as cut[i] = i-1

        Use two variables in two loops to represent a palindrome:
        The external loop variable 'i' represents the center of the palindrome.
        The internal loop variable 'j' represents the 'radius' of the palindrome.
        Apparently, j <= i is a must.
        This palindrome can then be represented as s[i-j, i+j].
        If this string is indeed a palindrome, 
        then one possible value of cut[i+j] is cut[i-j] + 1,
        where cut[i-j] corresponds to s[0, i-j-1] and 1 correspond to the palindrome s[i-j, i+j];

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
    ex: "aaaaaaaaa"
        """
        self.cur_pal_parts = []
        self.palindromic_parts = []
        self.get_palindromic_parts(0, given_str)
        return self.palindromic_parts
