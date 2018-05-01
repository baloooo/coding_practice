"""
https://leetcode.com/articles/implement-trie-prefix-tree/


Idea: https://discuss.leetcode.com/topic/14202/ac-python-solution/7
Also contains info on time complexity for insert and search
http://www.geeksforgeeks.org/trie-insert-and-search/
Time: O(n) where n is the length of word to be searched.
Space: O(mnk) where m is the total number of words each of lenght n, and k is the size of character set
since at each node this character set resides pointing to nodes in it's children
"""
import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            cur = cur.children.get(ch)
            if cur is None:
                return False
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if cur is None:
                return False
        return True

    # def _inorder(self, root):
    #     if root is None:
    #         return
    #     # All children smaller than root
    #     # self._inorder(root.left)
    #     sorted_keys =
    #     for child in [
#         left_child for child in sorted(root.children) if child < root.val]:
    #         self._inorder(child)
    #     print root.val
    #     # All children greater than root
    #     self._inorder(root.right)

    # def sorted_values(self):
    #     self._inorder(self.root)


class CompactTrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}
        self.is_word = False


class CompactTrie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cur = None
        self.root = CompactTrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        cur[word[0]] = ?
        for index, ch in enumerate(word):
            if cur.children.get(ch):
                cur = cur.children[ch]
            else:
                cur.word = word[index:]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            cur = cur.children.get(ch)
            if cur is None:
                return False
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if cur is None:
                return False
        return True

    def all_prefixes(self, prefix):
        """
        returns all strings in datastructure that have this prefix
        """
        pass


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# words = ['romane', 'romanus', 'romulus', 'rubens', 'ruber', 'rubicon',
#          'rubicundus']
# for word in words:
#     obj.insert(word)
# param_2 = obj.search('rubicon')
# param_3 = obj.startsWith('rubi')
obj = CompactTrie()
words = ['romane', 'romanus', 'romulus', 'rubens', 'ruber', 'rubicon',
         'rubicundus']
for word in words:
    obj.insert(word)
param_2 = obj.search('rubicon')
param_3 = obj.startsWith('rubi')
import ipdb; ipdb.set_trace()
