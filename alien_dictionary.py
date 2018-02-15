"""
Topological Sorting: A topological sort or topological ordering of a directed Acyclic graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another.
Problem understanding: https://discuss.leetcode.com/topic/22395/the-description-is-wrong
Idea is Topological sorting using DFS: https://discuss.leetcode.com/topic/22395/the-description-is-wrong
"""

import collections

class DirectedGraphNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = set() # These are the neighbors this node has directed link towards.
        self.visited = False

    def __str__(self):
        return self.val

    def __eq__(self, other):
        if self.val == other.val:
            return True
        else:
            return False

class Solution(object):
    def _create_nodes(self, graph, word):
        for ch in word:
            if ch not in graph:
                node = DirectedGraphNode(ch)
                graph[ch] = node

    def create_graph(self, words):
        """
        creates an adjacency list graph reprsentation of words.
        """
        graph = collections.defaultdict(DirectedGraphNode)
        
        for i in xrange(len(words)):
            self._create_nodes(graph, words[i])
            for j in xrange(i+1, len(words)):
                self._create_nodes(graph, words[j])
                for parent_ch, child_ch in zip(words[i], words[j]):
                    # Make a directed edge parent_ch -> child_ch
                    if parent_ch != child_ch:
                        graph[parent_ch].neighbors.add(graph[child_ch])
                        if graph[parent_ch] in graph[child_ch].neighbors:
							# there's a loop so invalid graph.
                            return False
                        break
        return graph
        
    def toposort_util(self, node, stack):
        if node.visited is True:
            return
        else:
            node.visited = True
        for neighbor in node.neighbors:
            if neighbor.visited is False:
                self.toposort_util(neighbor, stack)
        stack.append(node) # This is imp. we're pushing the node afterwards unlike regular DFS.

    def toposort(self, graph):
        """
        returns a toposort of the given graph.
        """
        stack = []
        for node_key, node_object in graph.items():
            if node_object.visited is False:
                self.toposort_util(node_object, stack)
        return ''.join([node.val for node in reversed(stack)]) # Note that we're printing in reverse as this is stack.

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = self.create_graph(words)
        if not graph:
            return "" # Invalid graph
        return self.toposort(graph)

if __name__ == '__main__':
    words = [ "wrt", "wrf", "er", "ett", "rftt" ]
    words = ["z", "x", "z"]
    words = ["z", "z"]
    words = ["ab", "adc"]
    words = ["wlbn"]
    print "Got o/p: %s" % Solution().alienOrder(words)
