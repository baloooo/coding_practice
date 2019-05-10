'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''

import pytest

class Solution(object):
    def shortestDistance(self, city_map):
        """
        Naive:
            For each building, traverse the matrix, use BFS to compute the shortest distance from each '0' to
            this building. After we do this for all the buildings, we can get the sum of shortest distance
            from every '0' to all reachable buildings. This value is stored
            in 'distance[][]'. For example, if grid[2][2] == 0, distance[2][2] is the sum of shortest distance from this block to all reachable buildings.
            Time complexity: O(number of 1)O(number of 0) ~ O(m^2n^2)

        Optimized:
            we just run BFS at each '0', summing up the distance to each '1'.
            Once we've hit every node, we can return this distance only if we were able to go to all the 1's on the board.
            Time:  O(K*(mn))

        :type grid: List[List[int]]
        :rtype: int
        """
        num_of_target_houses = 0
        for row in xrange(len(city_map)):
            for col in xrange(len(city_map[0])):
                if city_map[row][col] == 1:
                    num_of_target_houses += 1
        min_distance_to_all_targets = float('inf')
        for row in xrange(len(city_map)):
            for col in xrange(len(city_map[0])):
                if city_map[row][col] == 0:
                    min_distance_to_all_targets = min(min_distance_to_all_targets, self.bft(city_map, row, col, num_of_target_houses))

        return min_distance_to_all_targets if min_distance_to_all_targets != float('inf') else -1

    def bft(self, city_map, origin_row, origin_col, num_of_target_houses):
        visited = set()
        visited.add((origin_row, origin_col))
        visited_houses = 0
        total_distance_travelled = 0
        cur_distance_from_origin = 0
        # Implement Level order bfs
        cur_level = [(origin_row, origin_col)]
        while cur_level:
            next_level = []
            for house_pos_x, house_pos_y in cur_level:
                for adjacent_house_x, adjacent_house_y in [(house_pos_x+1, house_pos_y), (house_pos_x-1, house_pos_y), (house_pos_x, house_pos_y+1),(house_pos_x, house_pos_y-1)]:
                    if (not (0 <= adjacent_house_x < len(city_map) and 0 <= adjacent_house_y < len(city_map[0])) or
                            city_map[adjacent_house_x][adjacent_house_y] == 2 or
                            (adjacent_house_x, adjacent_house_y) in visited):
                        continue
                    else:
                        visited.add((adjacent_house_x, adjacent_house_y))

                    if city_map[adjacent_house_x][adjacent_house_y] == 1:
                        total_distance_travelled += cur_distance_from_origin + 1
                        visited_houses += 1
                    else:
                        next_level.append((adjacent_house_x, adjacent_house_y))

            cur_level = next_level
            cur_distance_from_origin += 1

        return total_distance_travelled if visited_houses == num_of_target_houses else float('inf')

class TestShortestDistance(object):
    def setUp(self):
        #self.test_object = Solution()
        pass

    @pytest.mark.parametrize("input, expected_output", [
        ([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]], 7),
        ([[1]], -1),
        ([[1, 0]], 1),
    ])
    def test_shortest_distance(self, input, expected_output):
        #assert self.test_object.shortestDistance(**input) == expected_output
        sol = Solution()
        assert sol.shortestDistance(input) == expected_output

    def tearDown(self):
        pass
'''
if __name__ == '__main__':
    city_map, expected_distance = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]], 7
    city_map, expected_distance = [[1]], -1
    city_map, expected_distance = [[1, 0]], 1

    print Solution().shortestDistance(city_map)
'''
# Latest solution where logic is called on the basis if number of ones are less or number of zeroes.
# Time complexity is same for both logics but time can vary a lot on big test cases with disproportianate zeroes over ones or vice versa

class Solution(object):
    def shortestDistance(self, matrix):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return Sol().test_bf_2(matrix)

class Sol(object):
    def get_min_distance_house_location(self, matrix):
        min_distance = float('inf')
        for row in xrange(len(matrix)):
            for col in xrange(len(matrix[0])):
                if matrix[row][col] == 0:
                    min_distance = min(min_distance, self.get_distance_to_all_ones(matrix, row, col))

        return min_distance


    def get_distance_to_all_ones(self, matrix, row, col):
        cur_bfs_q = []
        cur_bfs_q.append((row, col))
        cur_distance = 0
        distance = 0
        no_of_houses_visited = 0
        visited = set()
        visited.add((row, col))
        while cur_bfs_q:
            next_bfs_queue = []
            for row, col in cur_bfs_q:
                for adj_row, adj_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0 <= adj_row < len(matrix) and 0 <= adj_col < len(matrix[0]) and (adj_row, adj_col) not in visited:
                        if matrix[adj_row][adj_col] == 1:
                            distance += cur_distance + 1
                            no_of_houses_visited += 1
                        elif matrix[adj_row][adj_col] == 0:
                            next_bfs_queue.append((adj_row, adj_col))

                        visited.add((adj_row, adj_col))
            cur_bfs_q = next_bfs_queue
            cur_distance += 1
        return distance if no_of_houses_visited == self.number_of_ones else float('inf')

    def test_bf_2(self, matrix):
        """
        Time: O(o * (m*n)), o being number of ones
        start from ones and try to reach all other zeroes and mark the distance it travelled to reach it, at the same time
        keep recording the number of ones visited. If at any point we cannot reach all ones quit and return -1
        """
        self.distance_matrix = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        self.number_of_ones = 0
        self.number_of_zeroes = 0

        # get total no of ones and zeroes, to decide which algo to use and also to check if all ones are reachable from a zero.
        for row in xrange(len(matrix)):
            for col in xrange(len(matrix[0])):
                if matrix[row][col] == 1:
                    self.number_of_ones += 1
                elif matrix[row][col] == 0:
                    self.number_of_zeroes += 1
        if self.number_of_ones > self.number_of_zeroes:
            min_distance = self.get_min_distance_house_location(matrix)
            return min_distance if min_distance != float('inf') else -1
        else:
            return self.get_min_distance_house_location2(matrix)

    def get_min_distance_house_location2(self, orig_matrix):
        distance_matrix = [[0 for _ in xrange(len(orig_matrix[0]))] for _ in xrange(len(orig_matrix))]
        houses_reachable_from_loc_matrix = [[0 for _ in xrange(len(orig_matrix[0]))] for _ in xrange(len(orig_matrix))]
        for row in xrange(len(orig_matrix)):
            for col in xrange(len(orig_matrix[0])):
                if orig_matrix[row][col] == 1:
                    if self.populate_distance_matrix_for2(row, col, orig_matrix, distance_matrix, houses_reachable_from_loc_matrix) == -1:
                        return -1

        return self.get_min_distance2(distance_matrix, houses_reachable_from_loc_matrix)

    def get_min_distance2(self, distance_matrix, houses_reachable_from_loc_matrix):
        min_distance = float('inf')
        for row in xrange(len(distance_matrix)):
            for col in xrange(len(distance_matrix[0])):
                # Ignores position with obstacles( represented by 2 in exercise)
                if distance_matrix[row][col] != 0 and houses_reachable_from_loc_matrix[row][col] == self.number_of_ones:
                    min_distance = min(min_distance, distance_matrix[row][col])

        return min_distance if min_distance != float('inf') else -1

    def populate_distance_matrix_for2(self, row, col, orig_matrix, distance_matrix, houses_reachable_from_loc_matrix):
        cur_bfs_q = []
        cur_bfs_q.append((row, col))
        cur_distance = 0
        distance = 0
        no_of_houses_visited = 0
        visited = set()
        visited.add((row, col))
        while cur_bfs_q:
            next_bfs_queue = []
            for row, col in cur_bfs_q:
                for adj_row, adj_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0 <= adj_row < len(orig_matrix) and 0 <= adj_col < len(orig_matrix[0]) and (adj_row, adj_col) not in visited:
                        if orig_matrix[adj_row][adj_col] == 1:
                            no_of_houses_visited += 1
                        elif orig_matrix[adj_row][adj_col] == 0:
                            distance_matrix[adj_row][adj_col] += (cur_distance + 1)
                            next_bfs_queue.append((adj_row, adj_col))
                            houses_reachable_from_loc_matrix[adj_row][adj_col] += 1

                        visited.add((adj_row, adj_col))
            cur_bfs_q = next_bfs_queue
            cur_distance += 1
        return distance if (no_of_houses_visited + 1) == self.number_of_ones else -1