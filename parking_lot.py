from enum import Enum


class ParkingType(Enum):
    Handicapped = 1
    Regular = 2
    Compact = 3


class ParkingSpace(object):
    def __init__(self, parking_type):
        self.is_vacant = True
        self.vehicle_parked = None
        self.parking_type = parking_type


class ParkingLot(object):
    """
    Todo:
        * Singleton
        * Add billing system(Assign tickets on entry and bill on exit)
        * Add floors
    """
    def __init__(self):
        pass

    def park(self, vehicle):
        pass

    def unpark(self, vehicle):
        pass

    def empty_spots(self):
        """
        returns floor wise/parking space wise emtpy spots or just total
        """
        pass


class VehicleType(Enum):
    Special = 1
    Regular = 2
    Mini = 3
    Bike = 4


class Vehicle(object):
    def __init__(self, license_no, type):
        self.license_no = license_no
        self.type = type
