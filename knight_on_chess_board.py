from Queue import Queue


class Solution:
    def __init__(self):
        pass

    def backtrace(self, cur, goal, path):
        # https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
        if cur == goal:
            return len(path)
        else:
            try:
                return self.backtrace(self.parent[cur], goal, [cur] + path)
            except KeyError:
                # when goal is not reachable
                return -1

    def knight_shortest_path_bfs(self, board_x, board_y, start_x, start_y,
                                 goal_x, goal_y):
        self.parent = {}
        board = [[False for _ in xrange(board_y)] for _ in xrange(board_x)]
        # start/goal coordinates are passed as 1 indexed instead of zero
        start_x -= 1
        start_y -= 1
        goal_x -= 1
        goal_y -= 1
        q = Queue()
        q.put((start_x, start_y))
        visited = set()
        while not q.empty():
            cur_x, cur_y = q.get()
            visited.add((cur_x, cur_y))
            if cur_x == goal_x and cur_y == goal_y:
                break
            if not (cur_x-1 < 0 or cur_y+2 < 0 or cur_x-1 >= len(board) or
                    cur_y+2 >= len(board[0]) or (cur_x-1, cur_y+2) in visited):
                q.put((cur_x-1, cur_y+2))
                self.parent[(cur_x-1, cur_y+2)] = (cur_x, cur_y)
            if not (cur_x-1 < 0 or cur_y-2 < 0 or cur_x-1 >= len(board) or
                    cur_y-2 >= len(board[0]) or (cur_x-1, cur_y-2) in visited):
                q.put((cur_x-1, cur_y-2))
                self.parent[(cur_x-1, cur_y-2)] = (cur_x, cur_y)
            if not (cur_x-2 < 0 or cur_y+1 < 0 or cur_x-2 >= len(board) or
                    cur_y+1 >= len(board[0]) or (cur_x-2, cur_y+1) in visited):
                q.put((cur_x-2, cur_y+1))
                self.parent[(cur_x-2, cur_y+1)] = (cur_x, cur_y)
            if not (cur_x-2 < 0 or cur_y-1 < 0 or cur_x-2 >= len(board) or
                    cur_y-1 >= len(board[0]) or (cur_x-2, cur_y-1) in visited):
                q.put((cur_x-2, cur_y-1))
                self.parent[(cur_x-2, cur_y-1)] = (cur_x, cur_y)
            if not (cur_x+1 < 0 or cur_y+2 < 0 or cur_x+1 >= len(board) or
                    cur_y+2 >= len(board[0]) or (cur_x+1, cur_y+2) in visited):
                q.put((cur_x+1, cur_y+2))
                self.parent[(cur_x+1, cur_y+2)] = (cur_x, cur_y)
            if not (cur_x+1 < 0 or cur_y-2 < 0 or cur_x+1 >= len(board) or
                    cur_y-2 >= len(board[0]) or (cur_x+1, cur_y-2) in visited):
                q.put((cur_x+1, cur_y-2))
                self.parent[(cur_x+1, cur_y-2)] = (cur_x, cur_y)
            if not (cur_x+2 < 0 or cur_y+1 < 0 or cur_x+2 >= len(board) or
                    cur_y+1 >= len(board[0]) or (cur_x+2, cur_y+1) in visited):
                q.put((cur_x+2, cur_y+1))
                self.parent[(cur_x+2, cur_y+1)] = (cur_x, cur_y)
            if not (cur_x+2 < 0 or cur_y-1 < 0 or cur_x+2 >= len(board) or
                    cur_y-1 >= len(board[0]) or (cur_x+2, cur_y-1) in visited):
                q.put((cur_x+2, cur_y-1))
                self.parent[(cur_x+2, cur_y-1)] = (cur_x, cur_y)
        return self.backtrace((goal_x, goal_y), (start_x, start_y), [])


if __name__ == '__main__':
    board_x, board_y, start_x, start_y, goal_x, goal_y = 9, 9, 1, 1, 8, 8 # 8, 8, 0, 0, 1, 4
    board_x, board_y, start_x, start_y, goal_x, goal_y = 8, 8, 1, 1, 8, 8
    print Solution().knight_shortest_path_bfs(
        board_x, board_y, start_x, start_y, goal_x, goal_y)
