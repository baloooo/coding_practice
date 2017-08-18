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

    def move_up(self):
        self.current_floor += 1

    def move_down(self):
        self.current_floor -= 1

    def get_elevator_direction(self):
        pass

    def get_elevator_status(self):
        pass
