from collections import defaultdict
from bisect import bisect_left, insort

"""
Current:
    Searching working fine.
    You can add new elements by appending '#' at the end of string.
Todo:
    Also if there are duplicates in warm up data consolidate them
    Bumping existing elements freq by searching for them (not working)
"""


class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        # Sorted array to store all words in this
        # (w/ current node as root) subtree.
        self.top_hits = []


class Sentence(object):
    # Making sentences as object as bisect cannot work with tuples and doesn't
    # have a key param either
    def __init__(self, sentence, freq):
        self.sentence = sentence
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            # Here precedence is give to higher ASCII value
            return self.sentence > other.sentence

    def __str__(self):
        return '%s' % self.sentence


class AutoComplete(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        # {'string': Sentence object}
        self.existing_sentences = {}
        self.populate_trie(sentences, times)

    def _add_to_top_hits(self, cur_root, cur_sentence):
        # check if sentence already exist (B search)
        pos = bisect_left(cur_root.top_hits, cur_sentence)
        if (pos != len(cur_root.top_hits) and
                cur_root.top_hits[pos] == cur_sentence):
            cur_root.top_hits[pos].freq += 1
        else:
            insort(cur_root.top_hits, cur_sentence)

    def populate_trie(self, sentences, times):
        for sentence, time in zip(sentences, times):
            if self.existing_sentences.get(sentence):
                cur_sentence = self.existing_sentences[sentence]
            else:
                cur_sentence = Sentence(sentence, time)
                self.existing_sentences[sentence] = cur_sentence
            cur_root = self.root
            for char in sentence:
                self._add_to_top_hits(cur_root, cur_sentence)
                cur_root = cur_root.children[char]
            self._add_to_top_hits(cur_root, cur_sentence)
            cur_root.is_word = True

    def search(self):
        cur = self.root
        inp = raw_input('Search:')
        # If input ends with '#' means currrent input should be stored
        if inp[-1] == '#':
            # add sentence to trie
            self.populate_trie([inp[:-1]], [1])
            return cur.top_hits[-3:][::-1]
        for char in inp:
            if cur.children.get(char):
                cur = cur.children.get(char)
            else:
                return []
        return cur.top_hits[-3:][::-1]

if __name__ == '__main__':
    sentences, times = ([
        'i love you', 'island', 'ironman', 'i love technology', 'i love you'],
        [5, 3, 2, 2, 1])
    inp = raw_input('Press to continue:')
    atc_obj = AutoComplete(sentences, times)
    while inp != 'n':
        res = atc_obj.search()
        for each in res:
            print each.sentence, each.freq
        inp = raw_input('Do you want to continue:')
