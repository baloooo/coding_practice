# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
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
        return self.bfs(orig_root)

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
