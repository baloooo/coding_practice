class Solution(object):
    def _neighbors(self, candidate, target):
        # find all neighbors of candidate that can lead to target
        i = 0
        while candidate[i] == target[i]:
            i += 1
        neighbor = list(candidate)
        for j in xrange(i+1, len(neighbor)):
            if neighbor[j] == target[i]:
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                yield ''.join(neighbor)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

    def kSimilarity(self, start, target):
        """
        :type A: str
        :type B: str
        :rtype: int
		https://github.com/kamyu104/LeetCode/blob/master/Python/k-similar-strings.py
		https://leetcode.com/problems/k-similar-strings/discuss/140099/JAVA-BFS-32-ms-cleanconciseexplanationwhatever
        Todo: time and space complexity from https://leetcode.com/problems/k-similar-strings/solution/
        """
        if start == target:
            return 0
        bfs_q = collections.deque([start])
        steps = 0
        visited = set()
        while bfs_q:
            for _ in xrange(len(bfs_q)):
                cand = bfs_q.popleft()
                if cand == target:
                    return steps
                for neighbor in self._neighbors(cand, target):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        bfs_q.append(neighbor)
            steps += 1
        return steps
