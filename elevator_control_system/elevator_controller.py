"""
1. Ask
How many elevators are there?
2. General optimal critiera
provide even service to each floor
minimize how long passengers wait for an elevator to arrive
minimize how long passengers spend to get to their destination floor
"""
import ElevatorControllerFactory

import heapq


class ElevatorController(ElevatorControllerFactory):
    """
    Controller for an elevator
    """

    def __init__(self):
        # All elevators start from lobby at first floor.
        self.currrent_floor = 1
        # Requests from floors will be added by Central Elevator controller
        # also. This is heapq as we need sorted min from current floor as
        # we are moving in one direction and new tasks are being added.
        self.request_queue = []

    def next_destination(self):
        return heapq.heappop(self.request_queue)

    def add_destination(self):
        """
        adds destination to request queue
        """
        pass

    def on_called(self, floor, direction):
        """
        floor: the floor that the elevator is being called to
        direction: the direction the caller wants to go, up or down
        """
        pass



class Elevator:
    def __init__(self, ele_id, cur_floor):
        self.ele_id = ele_id
        self.cur_floor = cur_floor
        self.direction = 0  # 0: Idle, +1: Up, -1: Down

    def on_floor_selected(self, floor):
        """
        floor: the floor that was requested from the elevator
        """
        pass

    def open(self):
        print "Doors opening on elevator %s for floor %s" % (self.ele_id, self.cur_floor)


    def close(self):
        print "Doors closing on elevator %s for floor %s" % (self.ele_id, self.cur_floor)

    def move(self, from_floor, to_floor):
        pass
