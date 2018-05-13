class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
	https://leetcode.com/problems/sentence-similarity/solution/
        Don't use a hashmap here since there can be duplicate mappings as
	'good': 'awesome' and 'good': 'satisfactory'.
        In case of hash_map one of these entries will override the other.
	So if one has to use hash map with values as list or set()
        """
        if len(words1) != len(words2):
            return False
        if len(words1) == 0: return True
        word_set = set()
        for w1, w2 in pairs:
            word_set.add((w1, w2))
            word_set.add((w2, w1))
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2:
                if (w1, w2) not in word_set:
                    return False
        return True

class DisjointNode(object):
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = None
        
class DJSGraph(object):
    def __init__(self):
        self.node_graph = {}
        
    def add_node(self, data):
        if data in self.node_graph:
            return self.node_graph[data]
        node = DisjointNode(data)
        node.parent = node
        self.node_graph[data] = node
        return node
    
    def find_parent(self, node):
        if node.parent == node:
            return node
        else:
            node.parent = self.find_parent(node.parent)
        return node.parent
    
    def merge_forest(self, node1, node2):
        node1_parent = self.find_parent(node1)
        node2_parent = self.find_parent(node2)
        
        if node1_parent == node2_parent: return
        
        if node1_parent.rank >= node2_parent.rank:
            if node1_parent.rank == node2_parent.rank:
                node1_parent.rank += 1
            node2_parent.parent = node1_parent
        else:
            node1_parent.parent = node2_parent
    
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        https://leetcode.com/problems/sentence-similarity-ii/solution/
	Here transitive property is allowed which inturn means:
		if A can reach B and B can reach C, A can reach C.
	Not only this but now,
		if X can reach Y and Y can reach A.
		X can reach B, and C by using the same transitive property.
	and the cycle can continue.
	Therefore the idea is to make nodes out of all words in the pairs and connect them
	as they are encountered in paris.
	Now for words1 and words2 we can just check if for each w1, w2 they both have the same
	parent_node or not meaning whether they belong to the same group or not.
        """
        if len(words1) != len(words2): return False
        if len(words1) == 0: return True
        dsu = DJSGraph()
        for w1, w2 in pairs:
            node1 = dsu.add_node(w1)
            node2 = dsu.add_node(w2)
            dsu.merge_forest(node1, node2)
            
        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            try:
                node1 = dsu.node_graph[w1]
                node2 = dsu.node_graph[w2]
            except KeyError:
                return False
            node1_parent = dsu.find_parent(node1)
            node2_parent = dsu.find_parent(node2)
            if node1_parent != node2_parent:
                return False
        
        return True
