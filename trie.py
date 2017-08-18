"""
Idea: https://discuss.leetcode.com/topic/14202/ac-python-solution/7
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
    #     for child in [left_child for child in sorted(root.children) if child < root.val]:
    #         self._inorder(child)
    #     print root.val
    #     # All children greater than root
    #     self._inorder(root.right)

    # def sorted_values(self):
    #     self._inorder(self.root)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
