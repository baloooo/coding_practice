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
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        pass
