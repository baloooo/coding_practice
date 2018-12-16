'''
If there's a Negative cycle made out of graph formed from equations we can't use Warshalls algo.
https://cs.stackexchange.com/questions/14248/what-is-the-significance-of-negative-weight-edges-in-a-graph/14262
Floyd warshall: https://www.youtube.com/watch?v=4OQeCuLYj-4 (not the best explanation of the algo)
In our exercise it is explicitly said numbers are all positive so there can't be any
negative cycles.
Also there can't be multiple ways to reach a destination, therefore equations a/c cannot have two values
depending on which intermediate nodes you use to calculate it. As in:
    ([["a", "b"], ["b", "c"], ['a', 'd'], ['d', 'c']], [2, 3, 4, 5], [["a", "c"]], [6]),
    ([["a", "b"], ["b", "c"], ['a', 'd'], ['d', 'c']], [4, 5, 2, 3], [["a", "c"]], [6]),
'''
import collections

class Solution:
    def dfs(self, graph, src, dest, cur_cost, visited):
        if src == dest:
            visited.add(dest)
            if src in graph:
                self.results.append(cur_cost)
            else:
                self.results.append(-1)
            return
        if src in visited:
            return
        visited.add(src)
        for adj in graph[src]:
            self.dfs(graph, adj, dest, cur_cost*graph[src][adj], visited)

    def dfs_calc_equation(self, equations, values, queries):
        # https://leetcode.com/problems/evaluate-division/discuss/88196/Simple'n'Clean-DFS-solution-in-Python
        # If there're multiple ways to reach a destination, DFS will find path from
        # all of them, we can run a min query after that to get the shortest path (else use floyd warshall)
        self.results = []
        graph = self.build_graph(equations, values)
        for src, dest in queries:
                visited = set()
                self.dfs(graph, src, dest, 1, visited)
                if dest not in visited:
                    self.results.append(-1)
                # results.append(-1 if dist == 0.0 else dist)
        return self.results

    def build_graph(self, equations, values):
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / (val*1.0)
        return quot

    def floyd_warshall(self, equations, values, queries):
        '''
        Use warshall if number of queries will outweigh number of vertices since once
        table is populated all queries can be answered in O(1), whereas use DFS O(V + E) if
        no. of queries are not so large also you won't have to look out for negative edge cycle
        as in floyd warshall'l algo.
            Tushar warshal: https://www.youtube.com/watch?v=LwJdNfdLF9s
            Notice negative edge weight is fine for warshall, but negative edge cycle is a problem for warshal.
            Broad idea is dynamic programming, basically we go over all the nodes(k-> 1 to n) and check
            if for going from i to j (where i and j themselves will be all the pair of nodes possible)
            do we have a shorter distance path via k than the original direct path i to j. Where all
            paths will be updated b/w all given nodes and all the other can default to infinity.
        Time: O(V^3)
        '''
        quot = self.build_graph(equations, values)
        for k in quot:
            for i in quot[k]:
                for j in quot[k]:
                # quot[i][j] = quot[i][k] * quot[k][j]
                dist_via_k = quot[i][k] + quot[k][j]
                if quot[i][j] > dist_via_k:
                    quot[i][j] = dist_via_k
        return [quot[num].get(den, -1.0) for num, den in queries]

    def calcEquation_alternate(self, equations, values, queries):
        """
        This is the better version for repeated queries, and when graph is dense.
		simpler version of floyd warshal, rest is same

        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        equations = [ ["a", "b"], ["b", "c"] ],
        values = [2.0, 3.0],
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
        """
        import collections
        nodes = set()
        # create graph
        dist_map = {} #(a,b): 2
        for (src, dest), distance in zip(equations, values):
            dist_map[(src, dest)] = distance
            dist_map[(dest, src)] = 1/(distance*1.0)
            dist_map[(src, src)] = 0
            dist_map[(dest, dest)] = 0
            nodes.add(src)
            nodes.add(dest)

        # floyd warshal to generate min distance b/w all nodes
        for intermediate in nodes:
            for src in nodes:
                for dest in nodes:
                    if (src, intermediate) in dist_map and (intermediate, dest) in dist_map:
						# normally addition is used but the nature of operation were so that transitive relationship
						# translated to multiplication instead.
                        path_via_intermediate = dist_map[(src, intermediate)] * dist_map[(intermediate, dest)]
                        if dist_map.get((src, dest), -float('inf')) < path_via_intermediate:
                            dist_map[(src, dest)] = path_via_intermediate

        # process queries
        res = []
        for src, dest in queries:
            res.append(dist_map.get((src, dest), -1.0))
        return res 

if __name__ == '__main__':
    test_cases = [
        # ([['a', 'b'], ['b', 'c'], ['b', 'd'], ['d', 'c'], ['c', 'e'], ['c', 'b']], [2, 1, 2, -4, 3, 1], [['a', 'e']], [6]),
        # ([["a", "b"], ["b", "c"], ['a', 'd'], ['d', 'c']], [2, 3, 4, 5], [["a", "c"]], [6]),
        # ([["a", "b"], ["b", "c"], ['a', 'd'], ['d', 'c']], [4, 5, 2, 3], [["a", "c"]], [6]),
        # ([["a", "b"], ["b", "c"]], [2.0, 3.0],
        #  [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        #  [6.0, 0.5, -1.0, 1.0, -1.0]),
    ]
    for test_case in test_cases:
        res = Solution().floyd_warshall(test_case[0], test_case[1], test_case[2])
        # res = Solution().dfs_calc_equation(test_case[0], test_case[1], test_case[2])
        if res == test_case[3]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[2], res, test_case[3])
