from Queue import Queue
n_tc = int(raw_input().strip())

class Node:
    def __init__(self, data):
        self.visited = False
        self.adjacent_nodes = set()
        self.distance_from_start = 0

def bfs(start_node):
    start_node.visited = True
    inp_queue = Queue()
    [inp_queue.put(each) for each in start_node.adjacent_nodes if not each.visited]
    while inp_queue.qsize():
        node = inp_queue.get()
        node.visited = True
        node.distance_from_start+=6
        for each in node.adjacent_nodes:
            if not each.visited:
                inp_queue.put(each)
                each.distance_from_root+=node.distance_from_start
    

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
            if node_map.get(each):
                print node_map[each].distance_from_start,
            else:
                print -1,


