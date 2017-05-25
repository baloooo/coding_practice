class Solution(object):
    def backtrack(self, neighbor_dict, beginWord, word, result, path):
        if beginWord == word:
            result.append(path)
        else:
            for prev_node in neighbor_dict[word]:
                self.backtrack(neighbor_dict, beginWord, prev_node, result, [prev_node] + path)
            
            
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict, deque
        import string
        
        unvisited = set(wordList)
        if endWord not in unvisited:
            return []
        # do nothing if beginWord is not in set
        unvisited.discard(beginWord)
        
        neighbor_dict = defaultdict(list)
        queue = deque([beginWord])
        # BFS: a variation of Dijkstra's algorithm
        while len(queue):
            visited = set()
            # traverse the whole level of the same ladder length
            for i in xrange(len(queue)):
                cur = queue.popleft()
                for i in xrange(len(cur)):
                    for char in string.ascii_lowercase:
                        neighbor = cur[:i] + char + cur[i+1:]
                        if neighbor == cur:
                            continue
                        if neighbor in unvisited:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append(neighbor)
                            neighbor_dict[neighbor].append(cur)
            unvisited -= visited
        
        # DFS
        result = []
        self.backtrack(neighbor_dict, beginWord, endWord, result, [endWord])
        return result
