from Queue import Queue
n_tc = int(raw_input().strip())

class Node:
    def __init__(self, data):
        self.visited = False
        self.adjacent_nodes = set()
        self.distance_from_start = 0

def bfs(start_node):
    inp_queue = Queue()
    inp_queue.put(start_node)
    while inp_queue.qsize():
        node = inp_queue.get()
        node.visited = True
        for each in node.adjacent_nodes:
            if not each.visited:
                inp_queue.put(each)
                each.distance_from_start=node.distance_from_start+6
                each.visited = True
    

for i in xrange(n_tc):
    nodes, edges = [int(x) for x in raw_input().strip().split(' ')]
    node_map = {}
    for edge in xrange(edges):
        node1, node2 = [int(x) for x in raw_input().strip().split(' ')]
        if node_map.get(node1):
            node_a = node_map.get(node1)
        else:
            node_a = Node(node1)
            node_map[node1] = node_a
        if node_map.get(node2):
            node_b = node_map.get(node2)
        else:
            node_b = Node(node2)
            node_map[node2] = node_b
        node_a.adjacent_nodes.add(node_b)
        node_b.adjacent_nodes.add(node_a)

    start_node = int(raw_input().strip())
    bfs(node_map[start_node])
    for each in xrange(1, nodes+1):
        if each!=start_node:
            if node_map.get(each) and node_map.get(each).visited:
                print node_map[each].distance_from_start,
            else:
                print -1,
    print
