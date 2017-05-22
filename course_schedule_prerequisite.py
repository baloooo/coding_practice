"""
PS:
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Algo:
    This problem is equivalent to detecting a cycle in the graph represented by
    prerequisites
    BFS uses the indegrees of each node. We will first try to find a node with
    0 indegree. If we fail to do so, there must be a cycle in the graph and we
    return false. Otherwise we have found one. We set its indegree to be -1 to
    prevent from visiting it again and reduce the indegrees of all its
    neighbors by 1. This process will be repeated for n (number of nodes)
    times. If we have not returned false, we will return true.
"""


class Solution:
    def __init__(self):
        pass

    def make_graph(self, num_courses, prerequisite_list):
        """
        1. makes adjacency list as edge list (prerequisite_list) is not
        the best representation of graph to do operations we want to
        perform like who is adjacent to who.
        2. Makes indegree list
        Time: O(V+E)
        Space: O(E) in a complete graph
        """
        from collections import defaultdict
        # self.adjacency_list = {node_num: [adjacent_node1, adjacent_node2,]}
        self.adjacency_list = defaultdict(list)
        # self.indegree_list = [0, 1, 5, 0, ...] where index depicts node_num
        # and value at index depicts
        # Indegree of node_num
        self.indegree_list = [0]*num_courses
        for destination, source in prerequisite_list:
            self.adjacency_list[source].append(destination)
            self.indegree_list[destination] += 1

    def can_finish(self, num_courses, prerequisite_list):
        # prerequisite_list[destination, source]
        self.make_graph(num_courses, prerequisite_list)
        # populate zero_indegree_q
        from Queue import Queue
        zero_indegree_q = Queue()
        for node_num, indegree in enumerate(self.indegree_list):
            if indegree == 0:
                zero_indegree_q.put(node_num)
        visited_count = 0
        topo_sort = []
        while not zero_indegree_q.empty():
            cur_node = zero_indegree_q.get()
            """
            extension of can_finish where if course schedule can be finished,
            one of the possible paths are returned else empty list is returned.
            """
            topo_sort.append(cur_node)
            visited_count += 1
            for neighbor in self.adjacency_list[cur_node]:
                self.indegree_list[neighbor] -= 1
                if self.indegree_list[neighbor] == 0:
                    zero_indegree_q.put(neighbor)
        return True if visited_count == num_courses else False
        # if topo sort needs to be returned
        # return topo_sort if visited_count == num_courses else False


if __name__ == '__main__':
    test_cases = [
        ((2, [[1, 0], [0, 1]]), False),
        ((2, [[0, 1]]), True),
        ((4, [[1, 0], [2, 1], [3, 2], [1, 3]]), False),
    ]
    for test_case in test_cases:
        res = Solution().can_finish(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
