import pytest
import collections

class Solution():
    def visit(self, graph, route, airport):
        route.append(airport)
        for next_airport in graph[airport]:
             pass

    def task(self, tickets):
        route = []
        graph = collections.defaultdict(list)

        for src, dest in tickets:
            graph[src].append(dest)

        for src, dest in graph.items():
            dest.sort(reverse=True)

        airport = "JFK" # can be set from user
        self.visit(graph, route, airport)
        return route

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
        assert sol.task(*args) == result
