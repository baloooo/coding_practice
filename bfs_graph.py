from collections import deque

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

    def bfs(self, source, destination):
        frontier = deque()
        frontier.append(source)
        came_from = {}
        came_from[source] = None
        while len(frontier):
            cur_node = frontier.popleft()
            # print 'visitin: %s' % (cur_node)
            if cur_node == destination:
                break
            for neighbor in self.neighbors(cur_node):
                if neighbor not in came_from:
                    came_from[neighbor] = cur_node
                    frontier.append(neighbor)
        if cur_node == destination:
            path = []
            # tracing back path
            while(cur_node != source):
                path.append(cur_node)
                cur_node = came_from[cur_node]
            path.append(source)
            return path[::-1]
        else:
            # target not found
            return None

if __name__ == '__main__':
    graph_object = SimpleGraph()
    graph_object.edges = {
	'A': ['B'],
	'B': ['A', 'C', 'D'],
	'C': ['A'],
	'D': ['E', 'A'],
	'E': ['B']
    }
    print graph_object.bfs('C', 'E')



