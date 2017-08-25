# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def alternate_bfs(self, orig_root):
        from Queue import Queue
        import collections
        """
        only difference is usage of defaultdict, therefore less explicit
        intializations.
        """
        if orig_root is None:
            return
        node_map = collections.defaultdict(lambda: UndirectedGraphNode(-1))
        q = Queue()
        q.put(orig_root)
        while not q.empty():
            cur = q.get()
            node_map[cur].label = cur.label
            for neighbor in cur.neighbors:
                # if neighbor already exist, only add this as a neighbor to cur_node  # noqa
                if neighbor in node_map:
                    node_map[cur].neighbors.append(node_map[neighbor])
                else:
                    # else create this neighbor and add to node_map
                    # add this as a neighbor to cur_node
                    node_map[neighbor].label = neighbor.label
                    node_map[cur].neighbors.append(node_map[neighbor])
                    q.put(neighbor)
        return node_map[orig_root]

    def bfs(self, orig_root):
        if orig_root is None:
            return None
        from Queue import Queue
        q = Queue()
        q.put(orig_root)
        orig_root_copy = UndirectedGraphNode(orig_root.label)
        new_graph_map = {orig_root: orig_root_copy}
        while not q.empty():
            cur_node = q.get()
            for neighbor in cur_node.neighbors:
                if neighbor not in new_graph_map:  # neighbor not visited
                    neighbor_copy = UndirectedGraphNode(neighbor.label)
                    new_graph_map[neighbor] = neighbor_copy
                    new_graph_map[cur_node].neighbors.append(neighbor_copy)
                    q.put(neighbor)
                else:
                    new_graph_map[cur_node].neighbors.append(new_graph_map[neighbor])  # noqa

        return orig_root_copy

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, orig_root):
        return self.new_bfs(orig_root)

if __name__ == '__main__':
    a = UndirectedGraphNode('a')
    b = UndirectedGraphNode('b')
    c = UndirectedGraphNode('c')
    a.neighbors = [b]
    b.neighbors = [c]
    c.neighbors = [c]
    test_cases = [
        (a, 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().cloneGraph(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
