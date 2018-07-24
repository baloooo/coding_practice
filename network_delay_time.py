'''There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

https://cs.stackexchange.com/questions/33136/is-single-source-single-destination-shortest-path-problem-easier-than-its-single
It turns out, this is one of the weird things about shortest paths, according to the-state of-the-art we know today, it seems to be the best algorithm for solving the A to B problem (given s, given t, go from s to t) is no easier than this problem (going from s to all vertices).

The best way we know how to solve going from A to B is to solve how to go from A to everywhere else.

Therefore:
  single source single dest: Dijkistra/Bellman ford
  single source all other nodes: Dijkistra/Bellman ford
  All pairs shortest path: Floyd warshall
'''


class Solution(object):
    def networkDelayTime_optimized(self, times, N, orig_src):
        import collections
        from Queue import PriorityQueue
        graph = collections.defaultdict(list)
        edges = {}
        for src, dest, w in times:
            graph[src].append(dest)
            edges[(src, dest)] = w

        visited = set()
        cost_from_src = collections.defaultdict(lambda: float('inf'))
        cost_from_src[orig_src] = 0
        frontier = PriorityQueue()
        frontier.put((0, orig_src))
        while not frontier.empty():
            closest = frontier.get()[1]
            if closest in visited:
                continue
            visited.add(closest)
            for adj in graph[closest]:
                new_cost_src_to_adj = cost_from_src[closest] + edges[(closest, adj)]
                if new_cost_src_to_adj < cost_from_src[adj]:
                    cost_from_src[adj] = new_cost_src_to_adj
                    frontier.put((new_cost_src_to_adj, adj))

        return max(cost_from_src.values()) if len(visited) == N else -1
        

if __name__ == '__main__':
    # times, N, K = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    # times, N, K = [[1,2,1],[2,1,3]], 2, 2
    # times, N, K = [[1,2,1],[2,3,2],[1,3,4]], 3, 1
    # times, N, K = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 3, 1
    times, N, K = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5
    times, N, K = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    print Solution().networkDelayTime_optimized(times, N, K)
