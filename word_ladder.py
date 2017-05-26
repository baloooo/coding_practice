"""
Given two words (start and end), and a dictionary, find the length of shortest
transformation sequence from start to end, such that:

You must change exactly one character in every transformation
Each intermediate word must exist in the dictionary
Example :

Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note that we account for the length of the transformation path instead of the
number of transformation itself.

 Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""


class Solution:
    """
    Time: O(n^2*m) where n is the number of entries in word_list
    and m is the size of goal_word (sizes of all words are same though)
    We'll be iterating over word_list for a max of n^2 times, worst case
    being when for every iteration only one word is added to queue and
    we iterated the entire list so put all elements from word_list to
    queue we'll require n^2 iterations (putting one element per iteration)
    word_list size-> n -> n-1 -> n-2 -> ... and each iteration requires full
    iteration over word list.
    Now for each iteration we call is_adjacent which takes O(m) time which
    essentially is just one pass over cur_word and target_word, so in total
    overall time complexity: O(n^2*m)
    """
    def __init__(self):
        pass

    def is_adjacent(self, test_word, cur_word):
        # to store count of differences
        count = 0
        # iterate thru all chars and return false if
        # more than one mismatching characters.
        # Note: length of all words in list is same
        for index in xrange(len(test_word)):
            if test_word[index] != cur_word[index]:
                count += 1
            if count > 1:
                return False
        """
        To ignore count == 0 which would mean strings same as cur_word should
        be ignored and only test_word at exact 1 edit distance should be passed
        """
        return True if count == 1 else False

    def word_ladder_naive(self, word_list, source_word, goal_word):
        from Queue import Queue
        q = Queue()
        q.put((source_word, 0))
        # word_list.append(goal_word)
        # This can  be improved by O(n) by using set instead of list.
        try:
            word_list.remove(source_word)
        except ValueError:
            pass
        while not q.empty():
            cur_word, cur_distance = q.get()
            if cur_word == goal_word:
                return cur_distance+1
            for test_word in word_list[:]:
                if self.is_adjacent(test_word, cur_word):
                    q.put((test_word, cur_distance+1))
                    word_list.remove(test_word)
        return -1

    def word_ladder_optimized(self, word_list, source_word, goal_word):
        """
        Problem statement:
         Given two words (beginWord and endWord), and a dictionary's word list,
        find the length of shortest transformation sequence from beginWord to
        endWord, such that:

        Only one letter can be changed at a time.
        Each transformed word must exist in the word list.
        Note that beginWord is not a transformed word.

        For example,

        Given:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]

        As one shortest transformation is
            "hit" -> "hot" -> "dot" -> "dog" -> "cog",
        return its length 5.

        Note:

            Return 0 if there is no such transformation sequence.
            All words have the same length.
            All words contain only lowercase alphabetic characters.
            You may assume no duplicates in the word list.
            You may assume beginWord and endWord are non-empty and are not the
            same.

        The trick (different from naive method above) here is to make use of
        the datastructures (set in this case)
        For every word in word_set we change it one bit and then check if
        this one bit changed word is in word_set and since this word_set is
        as set() we can do so in O(1). So for each_word in word_set (n) we
        iterate thru its size (w) and for each iteration try to fix 26
        alphabet chars and see which one works. Therefore in total:
        Time complexity: O(n*w*26)
        Space: O(n)
        """
        from string import ascii_lowercase
        word_set = set(word_list)
        cur_word_list, visited_set = [source_word], set([source_word])
        cur_distance = 0
        while cur_word_list:
            next_word_list = []
            print cur_word_list
            for cur_word in cur_word_list:
                if cur_word == goal_word:
                    return cur_distance + 1
                for index in xrange(len(cur_word)):
                    for ch in ascii_lowercase:
                        candidate_word = cur_word[:index] + ch + cur_word[index+1:]  # noqa
                        if (candidate_word in word_set and
                                candidate_word not in visited_set):
                            visited_set.add(candidate_word)
                            next_word_list.append(candidate_word)
            cur_word_list = next_word_list
            cur_distance += 1
        return cur_distance

    def word_ladder_2(self, word_list, source_word, goal_word):
        """
        Given two words (beginWord and endWord), and a dictionary's word list,
        find all shortest transformation sequence(s) from beginWord to endWord
         such that:

        Only one letter can be changed at a time
        Each transformed word must exist in the word list.
        Note that beginWord is not a transformed word.
        For example,

        Given:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        Return
          [
            ["hit","hot","dot","dog","cog"],
            ["hit","hot","lot","log","cog"]
          ]
        Note:
        Return an empty list if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same
        """
        from string import ascii_lowercase
        from collections import defaultdict
        from Queue import Queue
        """
        BFS for constructing graph.(BFS ends up making neighbor_dict)
        This graph is realized using neighbor_dict which is just a mapping
        of a word to (:) all words that are in one edit distance of this
        word.
        neighbor_dict = {'cog': ['dog', 'log'],
                     'dog': ['dot'],
                     'dot': ['hot'],
                     'hot': ['hit'],
                     'log': ['lot'],
                     'lot': ['hot']}
        """
        word_set = set(word_list)
        neighbor_dict = defaultdict(list)
        visited_values = set()
        visited_keys.add(source_word)
        while unvisited_keys:
            


if __name__ == '__main__':
    # source_word, goal_word, word_dict = "hit", "cog", ["hot", "dot", "dog",
    #                                                    "lot", "log", "cog"]
    # source_word, goal_word, word_dict = "a", "c", ["a", "b", "c"]
    # print Solution().word_ladder(word_dict, source_word, goal_word)
    # source_word, goal_word, word_dict = "a", "c", ["a", "b", "c"]
    source_word, goal_word, word_dict = "hit", "cog", ["hot", "dot", "dog",
                                                       "lot", "log"]
    print Solution().word_ladder_optimized(word_dict, source_word, goal_word)
