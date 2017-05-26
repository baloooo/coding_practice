class Solution(object):
    def backtrack(self, neighbor_dict, beginWord, word, result, path):
        if beginWord == word:
            result.append(path)
        else:
            for prev_node in neighbor_dict[word]:
                self.backtrack(neighbor_dict, beginWord, prev_node, result,
                               [prev_node] + path)

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
            print 'univisited', unvisited
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
                            # nodes which have not been dealt as keys for
                            # neighbor_dict
                            if neighbor not in visited:
                                # nodes which have not been marked as visited for
                                # cur_node (key in neighbor_dict), just so that
                                # we don't add a value multiple times to queue.
                                visited.add(neighbor)
                                queue.append(neighbor)
                            neighbor_dict[neighbor].append(cur)
            print 'visited', visited
            unvisited -= visited
        # DFS
        result = []
        print 'neighbor dict', neighbor_dict
        self.backtrack(neighbor_dict, beginWord, endWord, result, [endWord])
        return result

if __name__ == '__main__':
    print Solution().findLadders(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
