"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
"""
import collections


def substring_concat_orig(base_str, word_list):
    '''
    Time: O(len(base_str) * len(word_list) * word_len)
    Space: O(2 * len(word_list) * len(word_list[0]))
    Idea:https://discuss.leetcode.com/topic/17943/naive-c-solution-using-two-unordered_map-about-20-lines/20?page=1
    check Two pointer sol.n: https://github.com/kamyu104/LeetCode/blob/master/Python/substring-with-concatenation-of-all-words.py#L31
    '''
    word_len, word_freq_map = len(word_list[0]), collections.defaultdict(int)
    word_list_len = word_len*len(word_list)
    start_indices = []
    for word in word_list:
        word_freq_map[word] += 1
    for i in xrange(len(base_str)-word_list_len+1): # O(len(base_string))
        cur_word_freq_map, word_count = collections.defaultdict(int), 0
        for j in xrange(i, (i+word_list_len), word_len): # O(len(word_list)
            word = base_str[j:j+word_len] # O(word_len)
            if word not in word_freq_map:
                # break if tried to enter a string not in word_list
                break
            cur_word_freq_map[word] += 1
            # If had a valid string but freq more than in original
            if cur_word_freq_map[word] > word_freq_map[word]:
                break
            word_count += 1
        if word_count == len(word_list):
            start_indices.append(i)
    return start_indices



if __name__ == '__main__':
    # base_str, word_list = "barfoothefoobarman", ["foo", "bar"]
    # base_str = "aaaaaaaaaaaaaaaaaaa"
    # word_list = ["aaa", "aaa", "aaa", "aaa", "aaa"]
    base_str, word_list = "wordgoodgoodgoodbestword", ["word","good","best","good"]
    print substring_concat_orig(base_str, word_list)
