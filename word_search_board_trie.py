import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    def __str__(self):
        return "children are: %s and is_word: %r" % (self.children, self.is_word)
class Solution(object):
    def construct_trie(self, words):
        for word in words:
            cur = self.root
            for ch in word:
                cur = cur.children[ch]
            cur.is_word = True
                
    def dfs(self, board, i, j, cur_trie_node):
        if cur_trie_node.is_word and ''.join(self.cur_word) not in self.found_words:
            self.found_words.add(''.join(self.cur_word))
            return
        if not cur_trie_node.children.get(board[i][j]) or board[i][j] == '#':
            return
        self.cur_word.append(board[i][j])
        board[i][j] = '#'
        if i+1 < len(board): self.dfs(board, i+1, j, cur_trie_node.children[self.cur_word[-1]])
        if i-1 >= 0: self.dfs(board, i-1, j, cur_trie_node.children[self.cur_word[-1]])
        if j+1 < len(board): self.dfs(board, i, j+1, cur_trie_node.children[self.cur_word[-1]])
        if j-1 >=0: self.dfs(board, i, j-1, cur_trie_node.children[self.cur_word[-1]])
        board[i][j] = self.cur_word.pop()

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.root = TrieNode()
        self.construct_trie(words)
        self.found_words = set()
        self.cur_word = []
        import ipdb; ipdb.set_trace()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, self.root)
        return list(self.found_words)

if __name__ == '__main__':
    board, words = ["a"], ["a"]
    # board, words = ["oaan","etae","ihkr","iflv"], ["oath","pea","eat","rain"]
    board = [list(each) for each in board]
    words = [list(each) for each in words]
    print Solution().findWords(board, words)
