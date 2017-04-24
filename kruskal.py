"""
Kruskal's algo for min spanning tree, for a given connected, undirected and
weighted graph.
"""


from disjoint_set_datastructure import DisjointSet


class Graph:
    def __init__(self, num_of_vertices):
        # List of (u, v, w) node1, node2 and weight on edge b/w node1 and node2
        self.vertices = num_of_vertices
        self.graph = []
        self.dj_set = DisjointSet()
        self.mst = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal_mst(self):
        """
        We can achieve this bound as follows: first sort the edges by weight
        using a comparison sort in O(E log E) time; this allows the step
        "remove an edge with minimum weight from S" to operate in constant
        time. Next, we use a disjoint-set data structure (Union&Find) to keep
        track of which vertices are in which components. We need to perform
        O(V) operations, as in each iteration we connect a vertex to the
        spanning tree, two 'find' operations and possibly one union for each
        edge. Even a simple disjoint-set data structure such as disjoint-set
        forests with union by rank can perform O(V) operations in O(V log V)
        time. Thus the total time is O(E log E) = O(E log V).
        """
        for node in range(self.vertices):
            self.dj_set.make_set(node)
        # Loop untill v-1 edges are selected.
        # Step 1: Sort all edges based on non-decreasing weights.
        # Sorts inplaces but can easily be done off of separate copy
        self.graph.sort(key=lambda (u, v, w): w)
        vertices_count = 0
        index = 0
        # Step 2: Pick the smallest edge and increment the index for next iteration  # noqa
        while index < len(self.graph) and vertices_count <= (self.vertices - 1):  # noqa
            u, v, w = self.graph[index]
            u_parent = self.dj_set.find_parent_value(u)
            v_parent = self.dj_set.find_parent_value(v)
            if u_parent != v_parent:
                self.dj_set.union(u, v)
                vertices_count += 1
                self.mst.append([u, v, w])
            index += 1
        print 'Cost of MST is ', sum([edge[2] for edge in self.mst])


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.kruskal_mst()
