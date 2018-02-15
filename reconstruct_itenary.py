'''
Run as:
    python -m pytest -s reconstruct_itenary.py    
'''
import pytest
import collections

class Solution():
    '''
    As every path in the itineary needs to be included(w/ added requirement of correct order)
    this models the Eulerian path exercise.
    '''

    def visit(self, graph, route, airport):
        # https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
        while not graph[airport].empty():
            self.visit(graph, route, graph[airport].get())
        route.append(airport)

    def task(self, tickets):
        from Queue import PriorityQueue
        route = []
        graph = collections.defaultdict(PriorityQueue) # PQ due to lexicographically sorted requirement.

        # Construct adjacency graph
        for src, dest in tickets:
            graph[src].put(dest)

        airport = "JFK" # can be set from user
        self.visit(graph, route, airport)
        return route[::-1]

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
        ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"])
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.task(args) == result
