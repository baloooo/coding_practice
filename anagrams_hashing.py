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
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        This runs under the idea that strs will have only english alphabets.
	    Idea: https://leetcode.com/articles/group-anagrams/
	    Time: O(n*k) (Most efficient of all)
        """
        str_map = collections.defaultdict(list)
        for cur_str in strs:
	        str_signature = [0]*26
            for ch in cur_str:
                str_signature[ord(ch)-ord('a')] += 1
            str_map[tuple(str_signature)].append(cur_str)
        return str_map.values()

    def group_anagrams2(strs):
        '''
        This is a more generic version of the above
        '''
        ana_dict = collections.defaultdict(list)
        for cur_str in strs:
            str_map = {}
            for ch in cur_str:
                str_map[ch] = str_map.get(ch, 0) + 1
            # notice the 'items' here
            cur_set = frozenset(str_map.items())
            anagram_map[cur_set].append(string)
            # counter = collections.Counter(cur_str)
            # cur_dict = counter.items()
            # cur_set = frozenset(cur_dict)
            # ana_dict[cur_set].append(cur_str)
        return [each for each in ana_dict.values()]

    def group_anagrams(inp_list):
        """
        Time: O(nmlogm) #of strs is n and length of each str is m
        """
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for index, cur_str in enumerate(inp_list, start=1):
            anagram_map[''.join(sorted(cur_str))].append(index)
        return sorted(anagram_map.values(), key=lambda x: x[0])



if __name__ == '__main__':
    # inp_list = ['caa', 'tab', 'cca', 'bat']
    # inp_list = ['cat', 'dog', 'god', 'tca']
    # print group_anagrams2(inp_list)
    # inp_list = ["eat","tea","tan","ate","nat","bat"]
    inp_list = ["boo", "bob"]
    # inp_list = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
    print Solution().groupAnagrams2(inp_list)
