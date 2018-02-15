'''
Sol: https://leetcode.com/problems/employee-importance/solution/
Time: O(n)
Space: O(n)
'''

import pytest

class Solution():
    def dfs(self, graph, query_id):
        emp_id = graph[query_id]
        return (emp_id.importance + sum(self.dfs(graph, subordinate_id) for subordinate_id in emp_id.subordinates))

    def task(self, employees, query_id):
        # construct adjacency list representation of graph
        graph = {emp.id: emp for emp in employees}
        return self.dfs(graph, query_id)

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ([10, 20], 30),
        ([30, 40], 70),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.task(*args) == result
