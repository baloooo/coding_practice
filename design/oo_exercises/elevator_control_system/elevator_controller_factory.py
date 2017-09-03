class ElevatorControllerFactory(object):
    """
    ABC for generating elevator classes
    """
    MAX_ELEVATORS = 16

    def __init__(self):
        # initialize elevators
        pass

    def get_elevators(self):
        pass

    def pick_up(self, pick_up_floor):
        pass

    def destination(self, elevator_id, destination_floor):
        pass

    def scheduling_request_to_elevator(self):
        pass
