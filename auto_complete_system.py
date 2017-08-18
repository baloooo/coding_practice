from collections import defaultdict
import queue


class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        self.top_hits = queue.PriorityQueue()


class AutoComplete(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.populate_trie(sentences, times)

    def populate_trie(self, sentences, times):
        pass

    def search(self):
        cur = self.root
        char = None
        while char != '#':
            char = raw_input('Search:')
            if len(char) > 1:
                # hit trie multiple times
                pass
            else:
                pass

