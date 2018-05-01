import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary(object):
	'''
	Logic is same as below with the only difference that dfs now uses indices rather than slices
	of array which take more space therefore this implementation is more optimized.
	'''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_root = self.root
        for ch in word:
            cur_root = cur_root.children[ch]
        cur_root.is_word = True

    def dfs(self, cur_root, word, index):
        if len(word) == index:
            return cur_root.is_word
        if word[index] in cur_root.children:
            return self.dfs(cur_root.children[word[index]], word, index+1)
        elif word[index] == '.':
            for ch in cur_root.children:
                if self.dfs(cur_root.children[ch], word, index+1):
                    return True
        return False
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word, 0)

########################################################################################################
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
        cur.is_word = True

    def _search_from_here(self, root, word, index):
        """
        To fix, so as to use indexes rather than array copies
        """
        if index == len(word):
            return root.is_word
        for index in xrange(len(word)):
            letter = word[index]
            if letter == '.':
                for next_root in root.children.values():
                    if self._search_from_here(next_root, word, index+1):
                        return True
                return False
            else:
                root = root.children.get(letter)
                if root is None:
                    return False
        return root.is_word
    
    def dfs(self, node, word):
        """
        Idea: https://discuss.leetcode.com/topic/23695/python-easy-to-follow-solution-using-trie
        """
        if not word:
            if node.is_word:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])
            
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # return self._search_from_here(self.root, word, 0)
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

if __name__ == '__main__':
    # test_cases = [
    #     ('test1', 'sol1'),
    # ]
    word_dict = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    search_words = [["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    dict_obj = WordDictionary()
    for word in word_dict:
	dict_obj.addWord(word)
    for word in search_words:
	print dict_obj.search(word[0])
    # for test_case in test_cases:
    #     res = Solution().my_func(test_case[0])
    #     if res == test_case[1]:
    #         print "Passed"
    #     else:
    #         print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])

