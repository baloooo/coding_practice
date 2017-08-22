from enum import Enum
"""
TODO:
    * Assign parking spaces based on their ticket duration type:
      Maintain a sorted list of parking spaces (using a LinkedList) based on
      distance from entrance/exit.
     Now when a ticket for 1hr needs to be issued get a parking spot from the
     front of the available spots linked list and for entire day tickets get
     the parking spot from the end which would probably be on top levels of the
     building(farthest from entry/exit points) LL will have O(n) for get max
     queries and O(1) for get_min queries if the LL is further divided based on
     parking spot types too.
"""


class ParkingLot(object):
    """
    Current implementation always hands over a parking spot that is closest
    to the entrance, therefore most convenient to park and unpark that matches
    your parking vehicle type.
    Spot number are assigned as distance from entrance/exit increases and
    up the levels, so can be used as priority in the priority queue
    Todo:
        * Singleton
        * Add billing system(Assign tickets on entry and bill on exit)
        * Add floors
    """
    def __init__(self):
        from Queue import PriorityQueue
        self.parking_space_queue = PriorityQueue()
        # {vehicel_license_no: Vehicle object}
        self.vehicles_parked = {}

    def park(self, vehicle):
        # Iterate over available parking spots available, and if parking
        # spot type == vehicle trying to park, park it
        while not self.parking_space_queue.empty():
            candidate_parking_space = self.parking_space_queue.get()
            if candidate_parking_space.type == vehicle.type:
                candidate_parking_space.vehicle_parked = vehicle
                vehicle.parking_spot = candidate_parking_space
                self.vehicles_parked[vehicle.license_no] = vehicle
                return True
        print 'No parking space available for the current vehicle type'
        return False

    def unpark(self, vehicle_license_no):
        # unpark vehicle by: Generating it's bill, returning the spot back
        # to available parking spots lastly.
        try:
            vehicle_obj = self.vehicles_parked.pop(vehicle_license_no)
            self.parking_space_queue.put(vehicle_obj.parking_spot)
        except KeyError:
            print 'Vehicle doesnot exist'
            return False

    def empty_spots(self):
        """
        Todo: returns floor wise/parking space wise emtpy spots or just total
        currently return available parking spaces
        """
        return self.parking_space_queue.qsize()


class ParkingType(Enum):
    Handicapped = 1
    Large = 2
    Regular = 3
    Small = 4


class ParkingSpace(ParkingLot):
    def __init__(self, type, level, spot_number):
        self.vehicle_parked = None
        self.type = type
        self.spot_number = spot_number
        self.level = level
        super(ParkingSpace, self).__init__()
        self.parking_space_queue.put(self)

    @property
    def is_available(self):
        return self.vehicle_parked is None

    def __lt__(self, other):
        """
        First preference to floor level, second to spot number within a level
        """
        if self.level < other.level:
            return 1
        if self.spot_number < other.number:
            return 1
        return 0


class VehicleType(Enum):
    # vehicle_type: parking spots it require
    Small = 1
    Regular = 2
    Large = 5


class Vehicle(object):
    def __init__(self, vehicle_type, license_no):
        self.license_no = license_no
        self.type = vehicle_type
        self.parking_spot = None


class Motorcycle(Vehicle):
    # Vehicle types further warrant a separate class since, we've to attach
    # other info with each vehicle type like number of spots it consumes or
    # whether it fits on to a ParkingSpot etc
    def __init__(self):
        pass

if __name__ == '__main__':
    parking_lot_obj = ParkingLot()
    parking_spots = [('Regular', 1, 1), ('Regular', 1, 2)]
    for spot in parking_spots:
        p = ParkingSpace(*spot)
    incoming_vehicles = [
        ('Regular', 'TK1011'), ('Small', 'HA3511'),
        ('Large', 'HG2535')]
    for cur_vehicle in incoming_vehicles:
        parking_lot_obj.park(Vehicle(*cur_vehicle))
    import ipdb; ipdb.set_trace()
