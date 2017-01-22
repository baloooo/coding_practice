"""
Longest Substring Without Repeat
Given a string, 
find the length of the longest substring without repeating characters.

Example:

    The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

    For "bbbbb" the longest substring is "b", with the length of 1
"""

def longest_substring_without_rep(target_str):
    target_len = len(target_str)
    substr_set = set()
    base_index = 0
    max_uniq_substr_len = 0
    while(base_index < target_len):
        index = base_index
        while(index<target_len):
            if target_str[index] not in substr_set:
                substr_set.add(target_str[index])
                index += 1
            else:
                cur_substr_len = len(substr_set)
                if cur_substr_len > max_uniq_substr_len:
                    max_uniq_substr_len = cur_substr_len
                substr_set = set()
                break
        else:
            break
        base_index += 1
    cur_substr_set = len(substr_set)
    if cur_substr_set > max_uniq_substr_len:
        return cur_substr_set
    else:
        return max_uniq_substr_len


if __name__ == '__main__':
    target = "abcabcbb"
    # target = "bbbbbbbb"
    # target = ""
    # target = "abc"
    print longest_substring_without_rep(target)
