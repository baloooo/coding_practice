class Solution(object):
    def add_edges(self, seqs, graph, indegree):
        # You can add mapping between non-existent nodes but since they will have indegree 0 so ultimately will return False
        # We're allowing this non-existent node mapping to prevent polluting the code with too many if-else blocks
        for seq in seqs:
            if seq: # Add nodes and indegree to graph for ex like: [[1], [1], [1]]
                graph[seq[0]]
                indegree[seq[0]]
            for i in xrange(1, len(seq)):
                source, dest = seq[i-1], seq[i]
                if dest not in graph[source]:
                    graph[source].add(dest)
                    indegree[dest] += 1
                    
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        from Queue import Queue
        if not org or not seqs: return False
        
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        
        self.add_edges(seqs, graph, indegree)
        bfs_q = Queue()
        topo = []
        
        for node, indegree_count in indegree.items():
            if indegree_count == 0:
                bfs_q.put(node)
        # toposort using BFS
        #print bfs_q.queue
        #print graph
        #print indegree
        while not bfs_q.empty():
            if len(bfs_q.queue) > 1:
                return False
            cur = bfs_q.get()
            topo.append(cur)
            
            for adj in graph[cur]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    bfs_q.put(adj)
	''' You can either do this to check for cases like
		[1]
		[[1],[2,3],[3,2]]
	or have a check uptop about having any node in sequence list which is not in 
	org_set.'''
        for node, indegree_val in indegree.items():
            if indegree_val != 0:
                return False
        return topo == org
