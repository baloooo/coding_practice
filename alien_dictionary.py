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
    def create_graph(self, words):
        """
        creates an adjacency list graph reprsentation of words.
        """
        graph = collections.defaultdict(DirectedGraphNode)
        
        for i in xrange(len(words)):
        	for j in xrange(i+1, len(words)):
        		for parent_ch, child_ch in zip(words[i], words[j]):
        			# Make a directed edge parent_ch -> child_ch
        			if parent_ch != child_ch:
        				if parent_ch in graph:
        					parent_node = graph[parent_ch]
        				else:
        					parent_node = DirectedGraphNode(parent_ch)
        					graph[parent_ch] = parent_node
        				if child_ch in graph:
        					child_node = graph[child_ch]
        				else:
        					child_node = DirectedGraphNode(child_ch)
        					graph[child_ch] = child_node
        				parent_node.neighbors.add(child_node)
        				break
        return graph
        
    def toposort_util(self, node, stack):
        for neighbor in node.neighbors:
            if neighbor.visited is False:
                neighbor.visited = True
                self.toposort_util(neighbor, stack)
        stack.append(node)

    def toposort(self, graph):
        """
        returns a toposort of the given graph.
        """
        stack = []
        for node_key, node_object in graph.items():
            if node_object.visited is False:
                self.toposort_util(node_object, stack)
        return ''.join([node.val for node in reversed(stack)])

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # import ipdb; ipdb.set_trace()
        graph = self.create_graph(words)
        #import ipdb; ipdb.set_trace()
        if not graph:
        	return "" # Invalid graph
        return self.toposort(graph)

if __name__ == '__main__':
	words = [
	  "wrt",
	  "wrf",
	  "er",
	  "ett",
	  "rftt"
	]
	print "Expected o/p: wertf"
	print "Got o/p: %s" % Solution().alienOrder(words)
