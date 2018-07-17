'''There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

https://cs.stackexchange.com/questions/33136/is-single-source-single-destination-shortest-path-problem-easier-than-its-single
It turns out, this is one of the wired things about shortest paths, according to the-state of-the-art we know today, it seems to be the best algorithm for solving the A to B problem (given s, given t, go from s to t) is no easier than this problem (going from s to all vertices).

The best way we know how to solve going from A to B is to solve how to go from A to everywhere else.

Therefore:
  single source single dest: Dijkistra/Bellman ford
  single source all other nodes: Dijkistra/Bellman ford
  All pairs shortest path: Floyd warshall
'''


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
		'''
		Make  a separate map for indirect costs only from start node. We cannot use cost_map since values in there
		can be not the ones we use for reaching each node, and therefore max of them is not the max delay.
		'''
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import collections
        from heapq import heappush, heappop
        graph = collections.defaultdict(list)
        cost_map = {}
        cost_from_start = {}
        for source, dest, weight in times:
            graph[source].append((weight, dest))
            cost_map[(source, dest)] = weight
            cost_map[(source, source)] = 0
            cost_map[(dest, dest)] = 0

        frontier = [(0, start)] # (Priority, item)
        visited = set()
        while frontier:
            _, cur_node = heappop(frontier)
            visited.add(cur_node)
            for adj in graph[cur_node]:
                if adj[1] in visited:
                    continue
                heappush(frontier, adj)
                cost_from_start[adj[1]] = min(
                    cost_map.get((start, adj[1]), float('inf')), 
                    cost_map.get((start, cur_node), float('inf')) + cost_map.get((cur_node, adj[1]), float('inf')))

        return max(cost_from_start.values()) if len(visited) == N else -1

if __name__ == '__main__':
    # times, N, K = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    # times, N, K = [[1,2,1],[2,1,3]], 2, 2
    # times, N, K = [[1,2,1],[2,3,2],[1,3,4]], 3, 1
    # times, N, K = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 3, 1
    times, N, K = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5
    print Solution().networkDelayTime(times, N, K)
