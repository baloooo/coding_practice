from enum import Enum
import abc
"""
* Good video source: https://www.youtube.com/watch?v=DSGsa0pu8-k
Current implementation creates a parking lot object and adds some parking
spaces of certain types in it. Further some vehicles are created using a
VehicleFactory class. Now parking lot object is used to park these vehicles,
with the prime motivation of parking a vehicle as close to the entrance/exit so
as to allow them to leave the parking lot asap. Notice that since parking
spaces have different types (regular, handicapped) we still would park a car on
a parking space that can fit the type of vehicle, iff the number of spots
needed for parking are available.

TODO:
    * Make a class LEVEL and use this in parking lot class to get available
      spots on each level. This abstraction can help us to have more fine
      grain control over our spots on levels instead of iterating over all
      available slots on all levels. Similar can be done for Building which
      can hose multiple levels and so on.
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


class ParkingType(Enum):
    HANDICAPPED = 1
    REGULAR = 2


class ParkingSpace(object):
    def __init__(self, type, level, spot_number):
        self.vehicle_parked = None
        self.type = type
        # Can also include parking space UUID or just a (area_code+building_no+level+spot_no)
        self.spot_number = spot_number
        self.level = level  # Can help in making decision based on duration of park or if user wants to supply

    @property
    def is_available(self):
        return self.vehicle_parked is None

    def __lt__(self, other):
        """
        First preference to floor level, second to spot number within a level
        """
        if self.level < other.level:
            return 1
        if self.spot_number < other.spot_number:
            return 1
        return 0


class ParkingLot(object):
    """
    Idea: Not using Inheritance(IS-A),
        http://www.python-course.eu/inheritance_example.php
    but composition as it gives more flexibility (HAS-A).
    https://en.wikipedia.org/wiki/Composition_over_inheritance
    Current implementation always hands over a parking spot that is closest
    to the entrance, therefore most convenient to park and unpark that matches
    your parking vehicle type.
    Spot number are assigned as distance from entrance/exit increases and
    up the levels, so can be used as priority in the priority queue
    Todo:
        * Add billing system(Assign tickets on entry and bill on exit)
        * Also it might be a good idea to have separate priority queues for each type
          of parking spaces instead of popping and putting back loops also this would
          break it to constant time task as number of parking types is very small constant.
    """
    def __init__(self):
        from Queue import PriorityQueue
        self.parking_space_queue = PriorityQueue()
        # {vehicel_license_no: Vehicle object}
        self.vehicles_parked = {}

    def add_parking_space(self, parking_type, floor_no, spot_no):
        self.parking_space_queue.put(
            ParkingSpace(parking_type, floor_no, spot_no))

    def park(self, vehicle):
        """
        Iterate over available parking spots available, and if parking
        available for the vehicle type and number of spots are available
        for vehicle to park, park it else return message
        Handicaps can park in their spot or regular
        """
        # To alleviate push backs we can maintain separate PQs for Physicall challenged and regular type vehicles.
        parking_spaces_push_back = []
        while not self.parking_space_queue.empty():
            index = 0
            cur_parking_spots = []
            while (not self.parking_space_queue.empty() and
                   index < vehicle.type.value):
                candidate_parking_space = self.parking_space_queue.get()
                if (vehicle.parking_type == 'Handicap' or
                        candidate_parking_space.type == vehicle.parking_type):
                    cur_parking_spots.append(candidate_parking_space)
                    index += 1
                else:
                    # Place all unused parking spots back
                    parking_spaces_push_back.extend(cur_parking_spots)
                    parking_spaces_push_back.append(candidate_parking_space)
                    break
            else:
                vehicle.parking_spot = cur_parking_spots
                self.vehicles_parked[vehicle.license_no] = vehicle
                for parking_spot in cur_parking_spots:
                    parking_spot.vehicle_parked = vehicle
            parking_spaces_push_back.append(candidate_parking_space)
        # Puts back unused parking spaces
        for parking_space in parking_spaces_push_back:
            self.parking_space_queue.put(parking_space)
        return index == vehicle.type.value

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


class VehicleType(Enum):
    # vehicle_type: parking spots it require
    Small = 1
    Regular = 2
    Large = 3


class Vehicle(object):
    __metaclass__ = abc.ABCMeta

    # Forces derived classes to implement this
    @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError("You need to implement get_type")


class Small(Vehicle):
    def __str__(self):
        return '''Vehicle: License_no: %s, type: %s, parking_spot: %s,
            parking_type: %s''' % (self.license_no, self.type,
                                   self.parking_spot, self.parking_type)

    # Vehicle types further warrant a separate class since, we've to attach
    # other info with each vehicle type like number of spots it consumes or
    # whether it fits on to a ParkingSpot etc
    def __init__(self, license_no, parking_type='Regular'):
        self.license_no = license_no
        self.type = VehicleType.Small
        self.parking_spot = None
        self.parking_type = parking_type

    def get_type(self):
        return self.type.name


class Regular(Vehicle):
    # Vehicle types further warrant a separate class since, we've to attach
    # other info with each vehicle type like number of spots it consumes or
    # whether it fits on to a ParkingSpot etc
    def __init__(self, license_no, parking_type='Regular'):
        self.license_no = license_no
        self.type = VehicleType.Regular
        self.parking_spot = None
        self.parking_type = parking_type

    def get_type(self):
        return self.type.name


class Large(Vehicle):
    # Vehicle types further warrant a separate class since, we've to attach
    # other info with each vehicle type like number of spots it consumes or
    # whether it fits on to a ParkingSpot etc
    def __init__(self, license_no, parking_type='Regular'):
        self.license_no = license_no
        self.type = VehicleType.Large
        self.parking_spot = None
        self.parking_type = parking_type

    def get_type(self):
        return self.type.name

class VehicleFactory(object):

    # Factory(creational) design pattern
    def get_vehicle(self, vehicle_type, license_no, *args, **kwargs):
        if vehicle_type == 'Small':
            return Small(license_no, *args, **kwargs)
        elif vehicle_type == 'Regular':
            return Regular(license_no, *args, **kwargs)
        elif vehicle_type == 'Large':
            return Large(license_no, *args, **kwargs)

if __name__ == '__main__':
    parking_lot_obj = ParkingLot()
    # Parking_spot (type, level/floor, spot_number)
    parking_spots = [('Regular', 1, 1), ('Regular', 1, 2)]
    for spot in parking_spots:
        parking_lot_obj.add_parking_space(*spot)
    incoming_vehicles = [
        ('Regular', 'TK1011', 'Handicap'), ('Small', 'HA3511'),
        ('Large', 'HG2535'), ('Regular', 'TK1011')]
    for cur_vehicle in incoming_vehicles:
        vehicle_obj = VehicleFactory().get_vehicle(*cur_vehicle)
        if parking_lot_obj.park(vehicle_obj):
            print 'Vehicle parked %s' % vehicle_obj
        else:
            print '''No parking space available for the current vehicle %s
                ''' % (vehicle_obj)
