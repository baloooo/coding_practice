'''
https://www.youtube.com/watch?v=GSBLe8cKu0s
Edge cases:
    https://youtu.be/GSBLe8cKu0s?t=10m18s

Key points are the start coordinates of horizontal lines(roofs) of the buildings.
Exception being last point which will be the x-axis coordinate of the last buildings vertical wall
or whenever there is a gap in x-axis in positions of buildings or otherwise put when
there is a gap b/w set of buildings on x-axis.
Steps:
    1. Break given building co-ordinates (left, right, height) to (left, height, start) and (right, height, end)
    2. Sort this list on x-coordinate
    3. Maintain a max PQ, and insert elements to final skyline whenever max of PQ changes.
    4. For each start point encountered, add it to PQ if it changes cur max add it to final skyline.
    5. For each end point encountered, remove it from PQ, now if this changes cur max add new max to final skyline.
    Caveats:
        1. 
        2. 
Remove on heap can be brought down to O(logn):
    https://stackoverflow.com/questions/10162679/python-delete-element-from-heap
    https://stackoverflow.com/questions/12719066/priority-queue-remove-complexity-time
Alternate implementations:
    https://discuss.leetcode.com/topic/14987/108-ms-17-lines-body-explained
    
'''


# class Point(object):
#     def __init__(self, x, y, is_start):
#         self.x = x
#         self.y = y
#         self.is_start = is_start
# 
#     def __cmp__(self, other):
#         '''
#         If x coordinate are not same, do regular comparison, else:
#         If two starts are compared: then higher height should be picked first
#         If two ends are compared: lower height should be picked first
#         If one start and one end are compared: start should appear before end
#         '''
#         if self.x != other.x:
#             return self.x - other.x
#         else:
#             return (
#                     (-self.height if self.is_start else self.height) -
#                     (-other.height if other.is_start else other.height))
# 
#     def __repr__(self):
#         return 'x: %s, y: %s, is_start: %s ' % (self.x, self.y, self.is_start)

class Solution(object):
    def get_skyline(self, LRH):
	from heapq import *
	skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
	    import ipdb; ipdb.set_trace()
https://stackoverflow.com/questions/39080416/x-and-y-or-z-ternary-operator
https://stackoverflow.com/questions/18195322/pythons-logical-operator-and
https://stackoverflow.com/questions/36550588/assigning-string-with-boolean-expression/36551857#36551857
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
		print 'here'
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
		print 'there'
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline

    # def get_skyline(self, city):
    #     import heapq
    #     structures, skyline = [], []
    #     for structure in city:
    #         x1, x2, height = structure
    #         structures.append(Point(x1, height, True))
    #         structures.append(Point(x2, height, False))
    #     structures.sort()
    #     pq = []
    #     pq.append(0) # Reason: To have some default value to let compare existing strucutures with
    #     cur_max = 0
    #     for point in structures:
    #         if point.is_start:
    #             if point.y > cur_max:
    #                 # This building is taller than every other building at this start point
    #                 cur_max = point.y
    #                 heapq.heappush(pq, -point.y) # since it's a max PQ
    #                 skyline.append((point.x, point.y))
    #         else:
    #             try:
    #                 pq.remove(-point.y)
    #             except ValueError as err:
    #                 import ipdb; ipdb.set_trace()
    #             heapq.heapify(pq)
    #             # These two steps can be combined in O(logn)
    #             # https://stackoverflow.com/questions/10162679/python-delete-element-from-heap
    #             if -pq[0] != cur_max: # If PQ's max changed b'coz of remove
    #                 cur_max = -pq[0]
    #                 skyline.append([point.x, -pq[0]])
    #     return skyline

if __name__ == '__main__':
    test_cases = [
        # ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
	([[1,3,3],[2,4,4],[5,8,2],[6,7,4],[8,9,4]], []),
    ]
    for test_case in test_cases:
        res = Solution().get_skyline(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
