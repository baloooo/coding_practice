from collections import defaultdict
from bisect import bisect_left, insort

"""
graph or tree

https://leetcode.com/articles/design-search-autocomplete-system/
Performance Analysis

AutocompleteSystem() takes O(k*l)O(k∗l) time. We need to iterate over ll sentences each of average length kk, to create the trie for the given set of sentencessentences.

p = number of nodes up untill here i.e len(cur_prefix)
q = total nodes in the subtree with cur_root as the root node, where cur_root
is the end of cur_prefix
m is the total_words in this subtree of q nodes(i.e nodes which have is_word = True)

input() takes O\big(p+q+mlog(m)\big)O(p+q+mlog(m)) time. Here, pp refers to the length of the sentence formed till now, cur_sencur
​s
​​ en. qq refers to the number of nodes in the trie considering the sentence formed till now as the root node. Again, we need to sort the listlist of length mm indicating the options available for the hot sentences, which takes O\big(mlog(m)\big)O(mlog(m)) time.

Current:
    Searching working fine.
    You can add new elements by appending '#' at the end of string.
Todo:
    Trying to implement dynamic population of top hits at the end of cur_prefix.
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
        # Can be used by strategy when you search for top hits on the fly.
        self.freq = 0


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
            # Prevents adding same sentence again.
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
            cur_root.freq = time

    def bfs(self, cur_node, edit_distance):
        from Queue import Queue
        q = Queue()
        q.put(cur_node)
        """
        Todo: Add a strategy to cache words from cur_node to min1 index
        for each min and return that.
        we can use constant elements right now, but this can be extended
        for arbitrary k by usin a min heap and for bfs and running pop k times
        in the end.
        """
        # (sentence_obj, freq)
        min1 = Sentence('dummy', 0)
        min2 = Sentence('dummy', 0)
        min3 = Sentence('dummy', 0)
        while not q.empty() and edit_distance != 0:
            if edit_distance is not None:
                edit_distance -= 1
            cur = q.get()
            if cur.is_word:
                if cur.freq < min1:
                    min3 = min2
                    min2 = min1
                    min1 = cur
                elif cur.freq < min2[1]:
                    min3 = min2
                    min2 = cur
                elif cur.freq < min3[1]:
                    min3 = cur
            for each in cur.children.values():
                q.put(each)
        import ipdb; ipdb.set_trace()
        return [min1, min2, min3]

    def get_top_hits(self, cur_node, edit_distance=None):
        # edit distance would govern,till how much can the top hit be different
        # from our prefix
        return self.bfs(cur_node, edit_distance)

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
        # use this when you want to search for top hits on the fly using end
        # of cur_prefix as the root node.
        return self.get_top_hits(cur)
        # use this when you want to store results on each intermediate node
        # return cur.top_hits[-3:][::-1]

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
