'''
Run as:
    python -m pytest -s reconstruct_itenary.py    
'''
import pytest
import collections

class Solution():
    '''
    As every path in the itineary needs to be included(exactly once w/ added requirement of correct order)
    this models the Eulerian path exercise.
        https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
    Also for checking whether Euler path/cycle exists:
        https://math.stackexchange.com/questions/1871065/euler-path-for-directed-graph
    '''

    def visit(self, graph, route, airport):
        # https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
        # PQ blocks if get() is called on empty queue untill something is put in so don't loop directly
        # on PQ get() call
        while not graph[airport].empty():
            self.visit(graph, route, graph[airport].get())
        route.append(airport) # The placement of this line is the most important step in the algo.

    def findItinerary(self, tickets):
        '''
        Greedy DFS to find the Eulerian path.(Every edge is visited exactly once)
        '''
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
        assert sol.findItinerary(args) == result
