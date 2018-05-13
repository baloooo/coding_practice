class Solution(object):
    def bfs(self, grid, gates):
        '''
        Scans from all gates parallely to fill all empty rooms.
        '''
        from Queue import Queue
        EMPTY = 2147483647
        bfs_q = Queue()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for gate in gates:
            bfs_q.put(gate)
        while not bfs_q.empty():
            row, col = bfs_q.get()
            for direction in directions:
                cur_row = row + direction[0]
                cur_col = col + direction[1]
                
                if not (0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0])) or grid[cur_row][cur_col] != EMPTY:
                    continue
                # This is the first time (cur_row, cur_col) is being visited so add the min distance to the room.
                grid[cur_row][cur_col] = grid[row][col] + 1
                
                bfs_q.put((cur_row, cur_col))
                
                
    def wallsAndGates(self, rooms):
        """
	https://leetcode.com/problems/walls-and-gates/solution/
	Idea is that it is more profitable to start from gates rather than empty rooms since when
	you start from empty room once you find your way to nearest gate, all you get to know or write
	is one box(empty room) you started from thereby taking O(mn*mn) time as for each box you'll
	have to do a BFS which can scan the entire grid.
	On the other hand if we start from gates, any and all the empty rooms we encounter can be filled
	there and then since if the room has still INF value no one has visited it yet, therefore this
	is the first time they're being visited.We can be sure about this since we added all the gates
	to the queue first and the way BFS works is that it travels a distance of d from all the gates
	first and then moves to 2d distance for all the neighboring positions and so on.So once you
	touch a room that has never been seen before you can be sure you're the first one or the minimum
	distance from any gate to this room, also you can be now neglect this room for further traversals
	too since any traversal to this room from any other gate will result in a distance greater than
	this one as, we said before BFS fills all nodes with distance d before filling the node with 
	distance 2d so any later encounters to a room with already filled in value will have to be
	greater than this scan value.
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        gates = []
        for row in xrange(len(rooms)):
            for col in xrange(len(rooms[0])):
                if rooms[row][col] == 0:
                    gates.append((row, col))
        
        self.bfs(rooms, gates)

########################################################################################################
'''
Similar question is 01 matrix , we can just change the 1 to INF and rest is same.
Currently we're getting TLE 36/38 test case pass though, I don't think it's due to suboptimal 
algorithm may be just a tight test case.
'''
class Solution2(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from Queue import Queue
        bfs_q = Queue()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for row in xrange(len(matrix)):
            for col in xrange(len(matrix[0])):
                if matrix[row][col] == 0:
                    bfs_q.put((row, col))
        
        while not bfs_q.empty():
            row, col = bfs_q.get()
            
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0])) or matrix[new_row][new_col] != 1:
                    continue
                matrix[new_row][new_col] = matrix[row][col] + 1
                bfs_q.put((new_row, new_col))
        
        return matrix

if __name__ == '__main__':
    matrix = [[0,0,0],[0,1,0],[1,1,1]]
    print Solution2().updateMatrix(matrix)
