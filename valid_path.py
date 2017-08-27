class Solution:
    """
    Idea is to apply dfs to the board, keeping track of already visited nodes and if points to be visited
    are within the boundaries with an additional condition that each point should not be with in the self.radius distance
    from any of the centers of the given circles.
    """
    def valid(self, x1, y1):
        from math import sqrt
        # Distance b/w cur_cordinates(x,y) and any of the centers shouldn't be less than R
        for x2, y2 in zip(self.x_list, self.y_list):
            cur_distance = sqrt((abs(x2-x1))**2 + (abs(y2-y1))**2)
            if cur_distance < self.radius:
                return False
        return True

    def move(self, x, y):
        print x,y
	if (x,y) in self.already_visited:
	    return False
        self.already_visited.add((x, y))
        if x == self.final_x and y == self.final_y:
            return True
        if x+1 <= self.final_x and self.valid(x+1, y):
            if self.move(x+1, y):
                return True
        if y+1 <= self.final_y and self.valid(x, y+1):
            if self.move(x, y+1):
                return True
        if x-1 >= 0 and self.valid(x-1, y):
            if self.move(x-1, y):
                return True
        if y-1 >= 0 and self.valid(x, y-1):
            if self.move(x, y-1):
                return True
        if x+1 <= self.final_x and y+1 <= self.final_y and self.valid(x+1, y+1):
            if self.move(x+1, y+1):
                return True
        if x+1 <= self.final_x and y-1 >= 0 and self.valid(x+1, y-1):
            if self.move(x+1, y-1):
                return True
        if x-1 >= 0 and y+1 <= self.final_y and self.valid(x-1, y+1):
            if self.move(x-1, y+1):
                return True
        if x-1 >= 0 and y-1 >= 0 and self.valid(x-1, y-1):
            if self.move(x-1, y-1):
                return True
        self.already_visited.remove((x, y))
        return False
        
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, x, y, N, r, x_list, y_list):
        self.final_x, self.final_y, self.radius, self.x_list, self.y_list = x, y, r, x_list, y_list
        self.already_visited = set()
        return 'YES' if self.move(0, 0) else 'NO'

if __name__ == '__main__':
    # print Solution().solve(2, 3, 1, 1, [1, 2], [1, 3])  # expected ans: NO
    # print Solution().solve(41, 67, 5, 0, [17, 16, 12, 0, 40], [52, 61, 61, 25, 31])  # expected ans: YES
    print Solution().solve(61, 88, 2, 9, [3, 55], [18, 83])  # expected ans: NO
