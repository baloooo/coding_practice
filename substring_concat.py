"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
"""
import collections


def findSubstring2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        More efficient, uses min string window technique.
        Todo: why start only goes until w_len and not untill s_len-w_len_total
        https://discuss.leetcode.com/topic/35676/accepted-java-solution-12ms-with-explanation

        """
        s_len, w_len = len(s), len(words[0])
        w_len_total = len(words) * w_len
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        curr = {}
        res = []
        for start in range(w_len):
            curr = {}
            end = start
            while start + w_len_total <= s_len:
                sub = s[end:end+w_len]
                end += w_len
                if sub not in counter:
                    curr = {}
                    start = end
                else:
                    curr[sub] = curr.get(sub, 0) + 1
                    while curr[sub] > counter[sub]:
                        curr[s[start: start+w_len]] -= 1
                        start += w_len
                    if start + w_len_total == end:
                        res.append(start)
        return res


def substring_concat_basic(base_str, word_list):
    '''
    Idea is to make a frequency map of word_list(which would serve two purposes:
        a. Look up in O(1) time.
        b. can deal with duplicates, which can't be done in set)
    and traverse base_str and from each index there try to run thru word_list distance
    and populating a cur_word_freq_map, and see if after running till word_list distance
    if cur_word_freq_map == base_word_list_freq_map, if so, store the base_str index, and repeat
    the same process for next index in word_list.

    Time: O(len(base_str) * len(word_list) * word_len)
    Space: O(2 * len(word_list) * len(word_list[0])) # Two dictionaries

    Idea:https://discuss.leetcode.com/topic/17943/naive-c-solution-using-two-unordered_map-about-20-lines/20?page=1
    check Two pointer sol.n: https://github.com/kamyu104/LeetCode/blob/master/Python/substring-with-concatenation-of-all-words.py#L31
    '''
    if not base_word or not word_list:
        return []
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
