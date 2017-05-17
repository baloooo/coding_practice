from Queue import Queue


class Solution:
    def __init__(self):
        pass

    def knight_shortest_path_bfs(self, board_x, board_y, start_x, start_y,
                                 goal_x, goal_y):
        board = [[False for _ in xrange(board_y)] for _ in xrange(board_x)]
        q = Queue()
        q.put((start_x, start_y))
        visited = set()
        moves = 0
        while not q.empty():
            cur_x, cur_y = q.get()
            visited.add((cur_x, cur_y))
            # if (cur_x < 0 or cur_y < 0 or cur_x >= len(board) or
            #         cur_y >= len(board[0])):
            #     continue
            if cur_x == goal_x and cur_y == goal_y:
                print "moves: ", moves
                return True
            if not (cur_x-1 < 0 or cur_y+2 < 0 or cur_x-1 >= len(board) or
                    cur_y+2 >= len(board[0]) or (cur_x-1, cur_y+2) in visited):
                q.put((cur_x-1, cur_y+2))
                moves += 1
            if not (cur_x-1 < 0 or cur_y-2 < 0 or cur_x-1 >= len(board) or
                    cur_y-2 >= len(board[0]) or (cur_x-1, cur_y-2) in visited):
                q.put((cur_x-1, cur_y-2))
                moves += 1
            if not (cur_x-2 < 0 or cur_y+1 < 0 or cur_x-2 >= len(board) or
                    cur_y+1 >= len(board[0]) or (cur_x-2, cur_y+1) in visited):
                q.put((cur_x-2, cur_y+1))
                moves += 1
            if not (cur_x-2 < 0 or cur_y-1 < 0 or cur_x-2 >= len(board) or
                    cur_y-1 >= len(board[0]) or (cur_x-2, cur_y-1) in visited):
                q.put((cur_x-2, cur_y-1))
                moves += 1
            if not (cur_x+1 < 0 or cur_y+2 < 0 or cur_x+1 >= len(board) or
                    cur_y+2 >= len(board[0]) or (cur_x+1, cur_y+2) in visited):
                q.put((cur_x+1, cur_y+2))
                moves += 1
            if not (cur_x+1 < 0 or cur_y-2 < 0 or cur_x+1 >= len(board) or
                    cur_y-2 >= len(board[0]) or (cur_x+1, cur_y-2) in visited):
                q.put((cur_x+1, cur_y-2))
                moves += 1
            if not (cur_x+2 < 0 or cur_y+1 < 0 or cur_x+2 >= len(board) or
                    cur_y+1 >= len(board[0]) or (cur_x+2, cur_y+1) in visited):
                q.put((cur_x+2, cur_y+1))
                moves += 1
            if not (cur_x+2 < 0 or cur_y-1 < 0 or cur_x+2 >= len(board) or
                    cur_y-1 >= len(board[0]) or (cur_x+2, cur_y-1) in visited):
                q.put((cur_x+2, cur_y-1))
                moves += 1


if __name__ == '__main__':
    board_x, board_y, start_x, start_y, goal_x, goal_y = 9, 9, 1, 1, 8, 8 # 8, 8, 0, 0, 1, 4
    print Solution().knight_shortest_path_bfs(
        board_x, board_y, start_x, start_y, goal_x, goal_y)
