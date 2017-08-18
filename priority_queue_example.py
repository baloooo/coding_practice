import Queue
from enum import Enum

plane_attribute_map = {
    'type': {1: 'Government', 2: 'Passenger', 3: 'Cargo', 4: 'Charter'},
    'size': {1: 'Large', 2: 'medium', 3: 'small'},
}
"""
Note:  The usual restrictions for pickling apply: picklable enums must be defined in the top level of a module, since unpickling requires them to be importable from that module.
Note With pickle protocol version 4 it is possible to easily pickle enums nested in other classes.
"""
class PlaneType(Enum):
    GOV = 1
    PASSENGER = 2
    CARGO = 3
    CHARTER = 4

class PlaneSize(Enum):
    Large = 1
    Medium = 2
    Small = 3

class ATC(object):
    """
    Todo:
        * ATC for inflight airplanes
        * ATC for landing/take-off permissions
    """
    def __init__(self):
        self.queue = Queue.PriorityQueue()

    def add_airplane(self, airplane):
        """
        Adds airplane to be scheduled for departure
        """
        self.queue.put(airplane)

class Airplane(object):
    """
    Todo:
        * Check whether only __lt__ is ok for priority queue implementation
        * Use Enum wherever required for plane types/sizes etc.
        * Use Queue with Threads: https://pymotw.com/2/Queue/

    Place to start: https://stackoverflow.com/questions/28465411/priority-queue-doesnt-recognize-cmp-function-in-python?rq=1
    https://stackoverflow.com/questions/28435104/queue-with-multi-field-sorting-on-priority-and-time
    """
    def __init__(self, plane_type, plane_size, arrival_time):
        self.type = plane_type
        self.size = plane_size
        self.arrival_time = arrival_time

    def __lt__(self, other):
        # Compare based on plane types
        # if plane types are same comparison based on plane sizes
        # Lastly the plane which comes first departs first, if everything else is same
        if (self.type < other.type or self.size < other.size or
                self.arrival_time < other.arrival_time):
            return True
        else:
            return False

    # def __eq__(self, other):
    #     # if (self.type == other.type and self.size == other.size and
    #     #         self.arrival_time == other.arrival_time):
    #     #     return True
    #     if self.type != other.type:
    #         return False
    #     elif self.size != other.size:
    #         return False
    #     elif self.arrival_time != other.arrival_time:
    #         return False
    #     else:
    #         return True

    def __str__(self):
        return "Airplane with type: %s, size: %s, and arrival_time: %s" % (
            plane_attribute_map['type'][self.type],
            plane_attribute_map['size'][self.size],
            self.arrival_time)

if __name__ == '__main__':
    queue = Queue.PriorityQueue()
    """
    Higher the priority, lower the number
    types: [4: charted, 3: cargo, 2:passenger, 1: Government]
    sizes: [3: small, 2: medium, 1: large]
    arrival_times: These are just time stamps
    """
    # stream = [('cargo', 'small', 2), ('cargo', 'large', 1), ('cargo', 'small', 1)]
    stream = [(3, 3, 2), (3, 1, 1), (3, 3, 1), (1, 3, 10), (3, 3, 1)]
    for plane in stream:
        queue.put(Airplane(plane[0], plane[1], plane[2]))
    while not queue.empty():
        cur_plane = queue.get()
        print cur_plane
