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
    def shortestDistance2(self, city_map):
        self.UNREACHABLE = float('inf')
        city_distance_matrix = [[self.UNREACHABLE for _ in xrange(len(city_map[0]))] for _ in xrange(len(city_map))]
        self.number_of_buildings = self.get_number_of_buildings(city_map)

        for row in xrange(len(city_map)):
            for col in xrange(len(city_map[0])):
                if city_map[row][col] == 1:
                    if not self.reach_all_other_buildings_bft(city_map, city_distance_matrix, row, col):
                        return -1
        shortest_distance = self.get_shortest_distance_to_all_other_buildings(city_distance_matrix)
        return shortest_distance if shortest_distance != self.UNREACHABLE else -1

    def get_number_of_buildings(self, city_map):
        number_of_buildings = 0
        for row in xrange(len(city_map)):
            for col in xrange(len(city_map[0])):
                if city_map[row][col] == 1:
                    number_of_buildings += 1

        return number_of_buildings

    def reach_all_other_buildings_bft(self, city_map, city_distance_matrix, origin_row, origin_col):
        from Queue import Queue
        visited = set()
        bfs_queue = Queue()
        bfs_queue.put((origin_row, origin_col))
        visited.add((origin_row, origin_col))
        cur_hop = 0
        adj_coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited_buildings = set() # since we always start from a building and try to visit all other cells of 0 and 1.
        visited_buildings.add((origin_row, origin_col))
        while not bfs_queue.empty():
            cur_hop += 1
            for _ in xrange(len(bfs_queue.queue)):
                row, col = bfs_queue.get()
                for d_row, d_col in adj_coordinates:
                    adj_row, adj_col = row+d_row, col+d_col
                    if not(0 <= adj_row < len(city_map) and 0 <= adj_col < len(city_map[0])):
                        continue
                    if city_map[adj_row][adj_col] == 0 and (adj_row, adj_col) not in visited:
                        if city_distance_matrix[adj_row][adj_col] == self.UNREACHABLE:
                            city_distance_matrix[adj_row][adj_col] = cur_hop
                        else:
                            city_distance_matrix[adj_row][adj_col] += cur_hop
                        bfs_queue.put((adj_row, adj_col))
                        visited.add((adj_row, adj_col))
                    elif city_map[adj_row][adj_col] == 1:
                        visited_buildings.add((adj_row, adj_col))
        return len(visited_buildings) == self.number_of_buildings

    def get_shortest_distance_to_all_other_buildings(self, city_distance_matrix):
        closest_pos_to_all_buildings = self.UNREACHABLE
        for row in xrange(len(city_distance_matrix)):
            for col in xrange(len(city_distance_matrix[0])):
                closest_pos_to_all_buildings = min(closest_pos_to_all_buildings, city_distance_matrix[row][col])

        return closest_pos_to_all_buildings


    def shortestDistance1(self, city_map):
        """
        Naive:
            For each building, traverse the matrix, use BFS to compute the shortest distance from each '0' to
            this building. After we do this for all the buildings, we can get the sum of shortest distance
            from every '0' to all reachable buildings. This value is stored
            in 'distance[][]'. For example, if grid[2][2] == 0, distance[2][2] is the sum of shortest distance from this block to all reachable buildings.
            Time complexity: O(number of 1)O(number of 0) ~ O(m^2n^2)

        Optimized for less zeros:
            we just run BFS at each '0', summing up the distance to each '1'.
            Once we've hit every node, we can return this distance only if we were able to go to all the 1's on the board.
            Time:  O(K*(mn)), where K is the number of zeroes in the city_map.
            Notice that this strategy is more favorable when number of zeros are less in test cases.

        Optimized for less ones:
            Start from a building (a ONE), traverse the entire city map in BFT, and update the distance to each zero on the city map grid.
                As a side note see that you can reach all other buildings, if not return immediately since every building should be reachable from every other for the
                new position to reach all existing buildings.
                Edge case: [[1, 1], [0, 1]] This should return -1 not 2 since [1][1] cannot reach the valid new house location.

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
                    min_distance_to_all_targets = min(min_distance_to_all_targets, self.bft_1(city_map, row, col, num_of_target_houses))

        return min_distance_to_all_targets if min_distance_to_all_targets != float('inf') else -1

    def bft_1(self, city_map, origin_row, origin_col, num_of_target_houses):
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
        ([[1, 1], [0, 1]], -1),
    ])
    def test_shortest_distance(self, input, expected_output):
        #assert self.test_object.shortestDistance(**input) == expected_output
        sol = Solution()
        assert sol.shortestDistance2(input) == expected_output
        #assert sol.shortestDistance1(input) == expected_output

    def tearDown(self):
        pass

'''
if __name__ == '__main__':
    city_map, expected_distance = [[1]], -1
    city_map, expected_distance = [[1, 0]], 1
    city_map, expected_distance = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 7

    print Solution().shortestDistance2(city_map)
'''