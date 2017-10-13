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
        Uses separate lists instead of one queue
        Note:

            Return 0 if there is no such transformation sequence.
            All words have the same length.
            All words contain only lowercase alphabetic characters.
            You may assume no duplicates in the word list.
            You may assume beginWord and endWord are non-empty and are not the
            same.

        tldr: Standard BFS with visited_set = set()
        Time complexity: O(n*w*26)
        Space: O(n)
        
        The trick (different from naive method above) here is to make use of
        the datastructures (set in this case)
        For every word in word_set we change it one bit and then check if
        this one bit changed word is in word_set and since this word_set is
        as set() we can do so in O(1). So for each_word in word_set (n) we
        iterate thru its size (w) and for each iteration try to fix 26
        alphabet chars and see which one works. Therefore in total:

        Another key idea here is to use word_list and next_word_list to measure,
        when one level of BFS has completed and therefore cur_distance can be incremented.
        if we use a queue instead, we have no(yet I can think of) way of measuring the
        end of current level and beginning of next and therefore increment of cur_distance.
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
                        if (candidate_word in word_set and candidate_word not in visited_set):
                            visited_set.add(candidate_word)
                            next_word_list.append(candidate_word)
            cur_word_list = next_word_list
            cur_distance += 1
        return cur_distance

    def word_ladder_optimized_queue(self, beginWord, endWord, wordList):
        """
        Same as above, but uses regular queue instead of two lists for marking
        different levels.
        Appends None after every level therefore whenever queue front has None we can be 
        sure that one level has completed, and when consecutive None are encountered BFS
        has ended.
        """
        from Queue import Queue
        from string import ascii_lowercase
        word_set = set(wordList)
        cur_word_q, visited_set = Queue(), set(beginWord)
        cur_word_q.put(beginWord)
        cur_word_q.put(None)
        cur_distance = 0
        while not cur_word_q.empty():
            cur_word = cur_word_q.get()
            if cur_word is None:
                # end of level
                cur_distance += 1
                cur_word_q.put(None)
                cur_word = cur_word_q.get()
                if cur_word is None: break
            if cur_word == endWord: return cur_distance + 1
            for index in xrange(len(cur_word)):
                for ch in ascii_lowercase:
                    candidate_word = ''.join([cur_word[:index], ch, cur_word[index+1:]])
                    if candidate_word in word_set and candidate_word not in visited_set:
                        #if candidate_word == endWord: return cur_distance + 1
                        cur_word_q.put(candidate_word)
                        visited_set.add(candidate_word)
            #cur_distance += 1
        return 0

    def word_ladder_2(self, word_list, source_word, goal_word):
        from string import ascii_lowercase
        from collections import defaultdict
        from Queue import Queue
        """
        BFS for constructing graph.(BFS ends up making neighbor_dict)
        This graph is realized using neighbor_dict which is just a mapping
        of a word to (:) all words that are in one edit distance of this
        word.
        neighbor_dict = 
            {'dog': ['cog'],
			 'dot': ['dog'],
			 'hit': ['hot'],
			 'hot': ['dot', 'lot'],
			 'log': ['cog'],
			 'lot': ['log']}
        """
        word_set = set(word_list)
        neighbor_dict = defaultdict(list)
        # set to store nodes that have their neighbors explored for current node
        visited = set()
        bfs_q = Queue()
        # set to store nodes that have not been explored for their neighbors
        unvisited = set(word_list)
        # since we will begin to explore with source_word
        unvisited.discard(source_word)
        bfs_q.put(source_word)
        self.result = []
        while not bfs_q.empty():
            visited = set()
            # traverse the whole level of the same ladder length
            # run for current queue length, since we'll be adding
            # new items to queue this would prevent us from processing
            # all of them and only let us process queue items that
            # are there on current level.
            for _ in xrange(len(bfs_q.queue)):
                cur_word = bfs_q.get()
                for index in xrange(len(cur_word)):
                    for ch in ascii_lowercase:
                        candidate_word = cur_word[:index] + ch + cur_word[index+1:]
                        if candidate_word == cur_word:
                            continue
                        if candidate_word in unvisited:
                            # nodes which have not been dealt as keys for
                            # neighbor_dict
                            if candidate_word not in visited:
                                # nodes which have not been marked as visited for
                                # cur_node (key in neighbor_dict), just so that
                                # we don't add a value multiple times to queue.
                                bfs_q.put(candidate_word)
                                visited.add(candidate_word)
                            neighbor_dict[cur_word].append(candidate_word)
                            # neighbor_dict[candidate_word].append(cur_word)
                            # This can be neighbor_dict[candidate_word].append(cur_word)
                            # but then dfs algo would change, as key: value mappings changed
            unvisited -= visited
        # DFS for each possible paths
        # here we start from the goal word and try to reach source_word
        # and record all shortest possible paths we can do it from.
	print neighbor_dict
        self.dfs(source_word, goal_word, neighbor_dict, [source_word])
        return self.result

    def dfs(self, cur_word, goal_word, neighbor_dict, goal_path):
        if cur_word == goal_word:
            self.result.append(goal_path)
        else:
            for candidate_word in neighbor_dict[cur_word]:
                self.dfs(candidate_word, goal_word, neighbor_dict, goal_path + [candidate_word])

    def backtrack(self, neighbor_dict, beginWord, word, result, path):
	"""
	To be used when dict is made like so neighbor_dict[candidate_word].append(cur_word)
	"""
        if beginWord == word:
            result.append(path)
        else:
            for prev_node in neighbor_dict[word]:
                self.backtrack(neighbor_dict, beginWord, prev_node, result,
                               [prev_node] + path)


if __name__ == '__main__':
    source_word, goal_word, word_dict = "hit", "cog", ["hot", "dot", "dog",
                                                       "lot", "log", "cog"]
    # source_word, goal_word, word_dict = "a", "c", ["a", "b", "c"]
    # print Solution().word_ladder(word_dict, source_word, goal_word)
    # source_word, goal_word, word_dict = "a", "c", ["a", "b", "c"]
    # source_word, goal_word, word_dict = "hit", "cog", ["hot", "dot", "dog",
    #                                                    "lot", "log", "cog"]
    # source_word, goal_word, word_dict = "red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]
    print Solution().word_ladder_2(word_dict, source_word, goal_word)
