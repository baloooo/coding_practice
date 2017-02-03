"""
Given an array of strings, return all groups of strings that are anagrams.
Represent a group by a list of integers representing the index in the
original list. Look at the sample case for clarification.

Anagram : a word, phrase, or name formed by rearranging the letters of another,
such as 'spar', formed from 'rasp'
  Note: All inputs will be in lower-case.
  Example :

  Input : cat dog god tca
  Output : [[1, 4], [2, 3]]
  cat and tca are anagrams which correspond to index 1 and 4.
  dog and god are another set of anagrams which correspond to index 2 and 3.
  The indices are 1 based ( the first element has index 1 instead of index 0).

   Ordering of the result : You should not change
"""


def group_anagrams(inp_list):
    from collections import defaultdict
    anagram_map = defaultdict(list)
    for index, cur_str in enumerate(inp_list, start=1):
        anagram_map[''.join(sorted(cur_str))].append(index)
    return sorted(anagram_map.values(), key=lambda x: x[0])


if __name__ == '__main__':
    inp_list = ['caa', 'tab', 'cca', 'bat']
    # inp_list = ['cat', 'dog', 'god', 'tca']
    print group_anagrams(inp_list)
