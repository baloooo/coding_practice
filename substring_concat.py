"""
Substring Concatenation
You are given a string, S, and a list of words, L, that are all of the same
length.

Find all starting indices of substring(s) in S that is a concatenation of each
word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
"""


def substring_concat(base_str, word_list):
    word_len = len(word_list[0])
    word_list_len = word_len*len(word_list)
    start_indices = []
    for i in xrange(len(base_str)-word_list_len-1):
        sub_str_map = {}
        # defaulting dict to word_list, b'coz we only care about these
        for word in word_list:
            if sub_str_map.get(word) is None:
                sub_str_map[word] = 1
            else:
                sub_str_map[word] += 1
        for j in xrange(i, (i+word_list_len), word_len):
            try:
                sub_str_map[base_str[j:j+word_len]] -= 1
            except KeyError:
                # break if tried to enter a string not in word_list
                break
        else:
            for word_count in sub_str_map.values():
                if word_count != 0:
                    break
            else:
                start_indices.append(i)
    return start_indices

if __name__ == '__main__':
    base_str, word_list = "barfoothefoobarman", ["foo", "bar"]
    base_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_list = ["aaa", "aaa", "aaa", "aaa", "aaa"]
    print substring_concat(base_str, word_list)
