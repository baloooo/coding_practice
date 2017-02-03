"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if
reverse(S) = S.

Incase of conflict, return the substring which occurs first
( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""


# manachers algorithm
# O(n)
def longest_palindromic_substring_optimized(target):
    pass


# O(n^2)
def longest_palindromic_substring_even_odd_palindromes(target):
    longest_palindrome_substring_start = 0
    longest_palindrome_substring_len = 1
    for cur_index in xrange(1, len(target)):
        # even len palindrome starting from cur_index
        start = cur_index - 1
        end = cur_index
        while(start >= 0 and end < len(target) and
              target[start] == target[end]):
            start -= 1
            end += 1
        if (end-start+1) > longest_palindrome_substring_len:
            longest_palindrome_substring_start = start
            longest_palindrome_substring_len = end-start+1
        # odd len palindrome starting from cur_index
        start = cur_index - 1
        end = cur_index + 1
        while(start >= 0 and end < len(target) and
              target[start] == target[end]):
            start -= 1
            end += 1
        if (end-start+1) > longest_palindrome_substring_len:
            longest_palindrome_substring_start = start
            longest_palindrome_substring_len = end-start+1
        return target[
            longest_palindrome_substring_start:
            longest_palindrome_substring_start+longest_palindrome_substring_len]


def check_palindrome(target):
    start = 0
    end = len(target) - 1
    while(start < end):
        if target[start] != target[end]:
            return 0
        start += 1
        end -= 1
    return 1


def longest_palindromic_substring_naive(target):
    # Time complexity: O(n^3)
    target_len = len(target)
    max_palindrome_len = 0
    max_palindrome_str = ''
    for start in xrange(target_len):
        for end in xrange(target_len, -1, -1):
            if check_palindrome(target[start:end]):
                cur_palindrome_len = (end-start + 1)
                if cur_palindrome_len > max_palindrome_len:
                    max_palindrome_len = cur_palindrome_len
                    max_palindrome_str = target[start:end]
    return max_palindrome_str

if __name__ == '__main__':
    # target = 'abccba'
    target = "aaaabaaa"
    target = "bananas"
    # target = "abracadabra"
    print longest_palindromic_substring_naive(target)
    print longest_palindromic_substring_even_odd_palindromes(target)
