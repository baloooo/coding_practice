'''
We can not simply apply the code from REDUNDANT CONNECTION I, and add codes checking duplicated-parent only.
Here are 2 sample failed test cases:
[[4,2],[1,5],[5,2],[5,3],[2,4]]
got [5,2] but [4,2] expected
and
[[2,1],[3,1],[4,2],[1,4]]
got [3,1] but [2,1] expected
(Thanks @niwota and @wzypangpang )
The problem is we can not consider the two conditions separately, I mean the duplicated-parents and cycle.
This problem should be discussed and solved by checking 3 different situations:

No-Cycle, but 2 parents pointed to one same child
No dup parents but with Cycle
Possessing Cycle and dup-parents
Those 2 failed test cases are all in situation 3), where we can not return immediately current edge when we found something against the tree's requirements.
The correct solution is detecting and recording the whole cycle, then check edges in that cycle by reverse order to find the one with the same child as the duplicated one we found.
A more clear explanation and code have been posted by @niwota
https://discuss.leetcode.com/topic/105087/share-my-solution-c


https://leetcode.com/problems/redundant-connection-ii/discuss/108046/most-posted-answers-are-wrong
https://leetcode.com/problems/redundant-connection-ii/discuss/108073/share-my-solution-c
https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases

'''

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        parent = {}
        candidates = [] # List of all vertex pairs having multiple parents.
        for u, v in edges:
            if v in parent: 
                # Notice that we only add the first parent connection for all the remaining parent relationships,
                # we add them to candidates. 
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u
        # Notice that we're using parent map here and not children map
        def orbit(node): # runs a dfs to find if there is a cycle and return visited set and last node.
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen # returns the node which points to the node with multiple parents(if they exist)

        root = orbit(1)[0]

        if not candidates: # if no node has multiple parents, cycle will decide the redundant edge
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        # create children dict for dfs style traversing.
        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N # as nodes start from 1 put zero as dummy(True)
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])
        '''If cycle exists/DFS is able to see all nodes remove last edge(in occurence) for multiple parents since now
        all nodes are accessible therefore last edge added to cause a child have multiple parents is redundant, else
        there is a cycle and some nodes are not accessible therefore remove the first parent edge
        '''
        return candidates[all(seen)] 

if __name__ == '__main__':
    # edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
    # Output = [4,1]
    # edges =  [[1,2], [1,3], [2,3]]
    # Output = [2,3]
    edges = [[3,1], [2,1], [4,2], [1,4]]
    Output = [2,1]

    # print Solution().findRedundantConnection(edges)
    print Solution().findRedundantDirectedConnection(edges)
