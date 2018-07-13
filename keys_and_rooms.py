class Solution(object):
    def dfs(self, cur_room, rooms, visited):
        for key in cur_room:
            if key not in visited:
                visited.add(key)
                self.dfs(rooms[key], rooms, visited)

    def canVisitAllRooms(self, rooms):
        """
		Time: O(n)
		Space: O(n) (visited_set)
        :type rooms: List[List[int]]
        :rtype: bool
		Idea is to get to a room and take the keys there and visit each room with the key.
		For each key in the room, make a dfs and keep going as far as you can with the key and keep adding rooms
		reachable in to visited.
		Now when you enter a room you should have already visited it using a key using any of the previous rooms, else
		there is no path to this room.
        """
        visited = set()
        visited.add(0)
        for idx, room in enumerate(rooms):
            if idx not in visited:
                return False
            self.dfs(room, rooms, visited)
        return True
