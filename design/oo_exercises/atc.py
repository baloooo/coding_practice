"""
Current implementation allows you to create airplane_objects from input stream
(any source), feed these airplanes to ATC object which can then schedule
takeoffs/ from the runway based on coded priorities.
Todo:
    * Add inflight support for airplanes
    * Airplanes can enter in ATC's airspace and leave without landing therefore
      allow them to trespass your airspace, preventing any collisions
    * Allow interested airplanes to land/takeoff
"""
import Queue
import functools
from enum import Enum

plane_attribute_map = {
    'type': {1: 'Government', 2: 'Passenger', 3: 'Cargo', 4: 'Charter'},
    'size': {1: 'Large', 2: 'medium', 3: 'small'},
}
"""
Note:  The usual restrictions for pickling apply: picklable enums must be
       defined in the top level of a module, since unpickling requires them to
       be importable from that module. Note With pickle protocol version 4 it
       is possible to easily pickle enums nested in other classes.
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
        * ATC for currently in flight airplanes
        * ATC for landing/take-off permissions
    """
    def __init__(self):
        self.queue = Queue.PriorityQueue()

    def add_airplane(self, airplane):
        """
        Adds airplane to be scheduled for departure
        """
        self.queue.put(airplane)


@functools.total_ordering
class Airplane(object):
    """
    Todo:
        * Check whether only __lt__ is ok for priority queue implementation
        * Use Enum wherever required for plane types/sizes etc.
        * Use Queue with Threads:
            https://pymotw.com/2/Queue/
            https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
            Put airplane objects to queues, and threads/processes should just
            pick them and serve them accordingly.

    Place to start:
        https://stackoverflow.com/questions/28465411/priority-queue-doesnt-recognize-cmp-function-in-python?rq=1
        https://stackoverflow.com/questions/28435104/queue-with-multi-field-sorting-on-priority-and-time
    """
    def __init__(self, plane_type, plane_size, arrival_time):
        self.type = plane_type
        self.size = plane_size
        self.arrival_time = arrival_time

    def __lt__(self, other):
        """
        Compare based on plane types, if plane types are same comparison based
        on plane sizes. Lastly the plane which comes first departs first,
        if everything else is same.
        Note: Do notice that if we create a priorityQueue of this we'll get minimum priority
        plance at the top since the default priorityQueue for python Queue module is min priority,
        one can negate the values at input and negate them again at usage to replicate a max queue
        behavior though
        """
        if self.type != other.type:
            return self.type < other.type
        elif self.size != other.size:
            return self.size < other.size
        elif self.height != other.height:
            return self.height < other.height

    def __eq__(self, other):
        """
        Compare based on plane types, if plane types are same comparison based
        on plane sizes. Lastly the plane which comes first departs first,
        if everything else is same.
        """
        return (self.type == other.type and self.size == other.size and 
                self.arrival_time == other.arrival_time)

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
    stream = [(3, 3, 2), (3, 1, 1), (3, 3, 1), (1, 3, 10), (3, 3, 1)]
    for plane in stream:
        queue.put(Airplane(-plane[0], -plane[1], -plane[2]))
    while not queue.empty():
        cur_plane = queue.get()
        print cur_plane
