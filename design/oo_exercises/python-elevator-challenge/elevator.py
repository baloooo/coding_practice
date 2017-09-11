from Queue import PriorityQueue
from elevator_base import UP, DOWN


class ElevatorLogic(object):
    """
    Todo: Don't ignore requests for opposite direction

    Fix the methods below to implement the correct logic for elevators.
    The tests are integrated into `README.md`. To run the tests:
    $ python -m doctest -v README.md

    To learn when each method is called, read its docstring.
    To interact with the world, you can get the current floor from the
    `current_floor` property of the `callbacks` object, and you can move the
    elevator by setting the `motor_direction` property.
    See below for how this is done.
    """

    def __init__(self):
        # Feel free to add any instance variables you want.
        self.destination_floor = None
        self.callbacks = None
        self.direction = None
        """
         1:  PQ for requests while going upward direction that lie ahead of the
             current floor
        -1:  PQ for requests while going downward direction that lie ahead of
             the current floor.  This should be a max priority queue, while
             travelling from top of building to basement
         0:  PQ for requests while going upward/downward direction that lie in
             the opposite direction of the current movement.
        """
        self.destinations = {1: PriorityQueue(), -1: PriorityQueue(),
                             0: PriorityQueue()}

    def on_called(self, floor, direction):
        """
        This is called when somebody presses the up or down button to call the
        elevator. This could happen at any time, whether or not the elevator
        is moving. The elevator could be requested at any floor at any time,
        going in either direction.
        floor: the floor that the elevator is being called to
        direction: the direction the caller wants to go, up or down
        """
        # requested_movement is floor*direction
        # cur_position = self.callbacks.current_floor
        # if self.callbacks.direction is not None:
        #  cur_position = self.callbacks.direction*self.callbacks.current_floor
        self.destinations[direction].put(direction*floor)
        # If request is for a floor to come ahead
        # if requested_movement < cur_position:
        #     self.destinations[direction].put(direction*floor)
        # else:
        #     self.destinations[0].put(direction*floor)
        # else:
        #     self.destinations[direction].put(direction*floor)
        self.on_ready()

    def on_floor_selected(self, floor):
        """
        -> called from select_floor
        This is called when somebody on the elevator chooses a floor.
        This could happen at any time, whether or not the elevator is moving.
        Any floor could be requested at any time.

        floor: the floor that was requested
        """
        # Request is in the same direction as current movement
        # if (self.direction*floor <= self.direction*self.callbacks.current_floor or  # noqa
        #     self.direction*floor >= self.direction*self.callbacks.current_floor):  # noqa
        #         return
        # If request is for a floor to come ahead
        if self.direction*self.callbacks.current_floor < self.direction*floor:
            self.destinations[self.direction].put(self.direction*floor)
        else:
            self.destinations[self.direction].put(self.direction*floor)

    def on_floor_changed(self):
        """
        This lets you know that the elevator has moved one floor up or down.
        You should decide whether or not you want to stop the elevator.
        """
        if self.destination_floor == self.callbacks.current_floor:
            self.callbacks.motor_direction = None

    def on_ready(self):
        """
        This is called when the elevator is ready to go.
        Maybe passengers have embarked and disembarked. The doors are closed,
        time to actually move, if necessary.
        """
        # if elevator is idle move it
        # Todo: currently checks requests for moving up first, but can be made
        # based on timestamp of request
        # import ipdb; ipdb.set_trace()
        self.destination_floor = None
        if self.callbacks.motor_direction is None:
            """
            if the elevator is idle
                See if there are any pending requests for going up(first)
                    Yes: service them
                    NO: See if there are any requests for going down
                        Yes: service them
                        NO: set motor_direction and direction to NONE
            """
            if not self.destinations[UP].empty():
                pass
            elif not self.destinations[DOWN].empty():
                self.destination_floor = self.destinations[DOWN].get()
                self.direction = (
                    UP if self.destination_floor > self.callbacks.current_floor
                    else DOWN)
                self.destination_floor = abs(self.destination_floor)
                self.callbacks.motor_direction = (
                    UP if self.destination_floor > self.callbacks.current_floor
                    else DOWN)
            else:
                self.callbacks.motor_direction = self.direction = None
        elif self.callbacks.motor_direction == UP:
            """
            If the elevator is going up:
                See if there are any pending requests ahead
                    if yes: service them
                    no: check if going down has some requests to be serviced
                        yes: service them
                        no: set motor direction and direction to None
            """
            if not self.destinations[UP].empty():
                pass
            else:
                # No more pending requests in upward direction
                if not self.destinations[DOWN].empty():
                    self.callbacks.motor_direction = self.direction = None
                else:
                    self.callbacks.motor_direction = DOWN
                    self.destination_floor = abs(self.destinations[DOWN].get())
        else:
            # Elevator going down
            print 'wants go down, add logic for it.'
        # if there's any pending requests in the direction of current movement
        # if self.destination_floor > self.callbacks.current_floor:
        #     self.callbacks.motor_direction = UP
        # elif self.destination_floor < self.callbacks.current_floor:
        #     self.callbacks.motor_direction = DOWN
