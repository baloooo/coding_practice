"""
Longest Substring Without Repeat
Given a string, 
find the length of the longest substring without repeating characters.

Example:

    The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

    For "bbbbb" the longest substring is "b", with the length of 1
"""

def longest_substring_without_rep(s):
    '''
    Template: https://discuss.leetcode.com/topic/68976/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem
    There're multiple exercises that run on the same idea where we maintain a window and a hash table :
    
    https://leetcode.com/problems/minimum-window-substring/
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    https://leetcode.com/problems/substring-with-concatenation-of-all-words/
    https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
    https://leetcode.com/problems/find-all-anagrams-in-a-string/
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
    https://leetcode.com/problems/longest-repeating-character-replacement


    Idea: https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
    '''
    char_to_index_map, start, max_window_size = {}, 0, 0
    for (index, char) in enumerate(s):
    	if char in char_to_index_map:
    	    '''
            Why max() and not just char_to_index_map[char]+1.
            ->There can be situations where char_to_index_map[char] points to a char far behind than cur start
            For those edge cases we use max
            Ex: New start will be max of older start and one character ahead of this repeating char
    	    s='abca' and index = 3 which will force start to be 1 and
            skip the initial a and later char_to_index_map will also
    	    be updated to add the correct index of 'a' 
            This is the most important step'''
    	    start = max(start, char_to_index_map[char]+1)
    	max_window_size = max(max_window_size, index-start+1)
    	char_to_index_map[char] = index
    return max_window_size

if __name__ == '__main__':
    target = "abcabcbb"
    # target = "bbbbbbbb"
    # target = ""
    # target = "abc"
    print longest_substring_without_rep(target)
