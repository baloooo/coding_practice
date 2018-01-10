import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def __str__(self):
        return "children are: %s and is_word: %r" % (self.children, self.is_word)

class Solution(object):
    def construct_trie(self, root, words):
        for word in words:
            cur = root
            for ch in word:
                cur = cur.children[ch]
            cur.is_word = True
        
    def dfs(self, root, board, row, col, cur, found_words):
        if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or
            root.children.get(board[row][col]) is None or board[row][col]=='#'):
                return False
        root = root.children[board[row][col]]
        cur.append(board[row][col])
        cur_word = ''.join(cur)
        if root.is_word and cur_word not in found_words:
            found_words.add(cur_word)
            # return # Here just for reminder: Don't return here so as to catch words like pea and peas
        board[row][col] = '#'    
        self.dfs(root, board, row+1, col, cur, found_words)   
        self.dfs(root, board, row-1, col, cur, found_words)   
        self.dfs(root, board, row, col+1, cur, found_words)   
        self.dfs(root, board, row, col-1, cur, found_words)   
        board[row][col] = cur.pop()
        
    def findWords(self, board, words):
        """
	Time: O(m * n * l) where m*n is the dimension of board and l is the max size of word
        Idea: In standard DFS (used in word_search_board 1) we can only chech for one word at
        a time. For example if word_list = [peaty, pea, bob, peas, zorro, peat] in Trie based solution
        when for 'peaty' we will check out all prefixes of pea so peaty, pea, peas, peat all will be
        added to found_words in one shot, as we're comparing all words with common prefix together.
        http://www.geeksforgeeks.org/boggle-set-2-using-trie/
        """
        root = TrieNode()
        self.construct_trie(root, words)
        found_words = set()
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                # Try finding prefixes from each [row][col] position
                self.dfs(root, board, row, col, [], found_words)
        return list(found_words)

if __name__ == '__main__':
    # board, words = ["a"], ["a"]
    board, words = ["oaan","etae","ihkr","iflv"], ["oath","pea","eat","rain"]
    board = [list(each) for each in board]
    words = [list(each) for each in words]
    print Solution2().findWords(board, words)
