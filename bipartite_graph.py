class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
		Idea: https://en.wikipedia.org/wiki/Bipartite_graph#Algorithms
		Basic idea is to start from any node and paint cur node by a color(red) and all adjacent nodes with
		a different color(blue), if we encounter an adjacent that is already visited and has the same color
		as cur node graph is not bi-partite.
		This idea can be realized using DFS or BFS, below is the implementation using BFS(largely b'coz
		input kind of facilitated using BFS)
        """
        import collections
        from Queue import Queue
        if not graph:
            return
        color = collections.defaultdict(int) # 0-> uncolored, 1->(Red), -1->(Blue)
        # BFS
        visited = set()
        bfs_q = Queue()
        # Note since disconnected graph satisfy bi-partite requirements, we have to scan thru all nodes
        for node in xrange(len(graph)):
            if node in visited:
                continue

            
            bfs_q.put((node, 1))
            color[node] = 1 # we start painting nodes by red(random choice, can select anything.)
            while not bfs_q.empty():
                cur_node, cur_color = bfs_q.get()
                if cur_node not in visited:
                    visited.add(cur_node)
                else:
                    continue
                for adj in graph[cur_node]:
                    if color[adj] == 0:
                        color[adj] = cur_color * -1
                    elif color[adj] == cur_color:
                        return False
                    bfs_q.put((adj, color[adj]))
        return True

if __name__ == '__main__':
    # graph = [[1,3],[0,2],[1,3],[0,2]]
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    print Solution().isBipartite(graph)
