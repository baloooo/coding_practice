'''
Adds drivers to Uber service.
Take requests from customers and serve them.
    Find nearby drivers (R-data structure)
    Send notifications to drivers
    Send routing info to driver to reach customer, and then to their destination
    Generate bill for the trip, charge the customer and pay the driver.
'''


class Person(object):
    def __init__(self, name):
        self.cur_rating = 0
        self.name = name

    def get_device_location(self): pass # Gets person location from CoreLocationFramework(iOS)


class Driver(Person):
    def __init__(self, name, car):
        super(Customer, self).__init__(name)
        self.car = car

    def serve_request(self, request): pass
    def _provide_routing_info(self, destination): pass # Called once request is accepted.


class Customer(Person):
    def __init__(self, name):
        super(Customer, self).__init__(name)

    def get_ride(self, source, destination): pass # Use https://en.wikipedia.org/wiki/R-tree for nearest drivers around and send them push notifications.
    def get_past_bookings(self): pass


class Vehicle(object):
    def __init__(self, model_no, license_no):
        self.model_no = model_no
        self.license_no = license_no


class UberX(Vehicle):
    def __init__(self, model_no, license_no):
        super(UberX, self).__init__(model_no, license_no)
        self.base_fares = 10


class UberBlack(Vehicle):
    def __init__(self, model_no, license_no):
        super(UberBlack, self).__init__(model_no, license_no)
        self.base_fares = 20

class VehicleFactory:
    '''
    Returns the appropriate vehicle object depending on the type of vehicle.
    '''
    def create_vehicle(self, service_type, vehicle_model, vehicle_name):
        vehicle = None

        if service_type == 'UberX':
            vehicle = UberX(vehicle_model, vehicle_name)
        elif service_type == 'UberBlack':
            vehicle = UberBlack(vehicle_model, vehicle_name)
        return vehicle


class Uber:
    def __init__(self):
        # These drivers would be stored in a R-tree in actual practice so as to be served
        # in O(logn) time to nearby Customers
        self.drivers = set()

    def register_driver(self, name, car, service_type):
        # drivers gives in details of his car and service he wants to subscribe into.
        vehicle_obj = VehicleFactory(car, service_type)
        driver = Driver(name, vehicle_obj)
        self.drivers.add(driver)
    def find_ride(self, customer, source, destination):
        drivers = self.find_nearby_drivers(self, customer.location)
        for driver in drivers:
            if self.send_notification(driver):
                # driver accepted notification
                break
        else:
            return 'Cannot find any nearby driver'
        self.provide_routing_info(driver.location, source)
        self.provide_routing_info(source, destination)
        self.bill_customer(customer, driver, source, destination)

    def find_nearby_drivers(self, location): pass

if __name__ == '__main__':
    uber = Uber()
    driver_details = {'name': 'Bob', 'car': 'Prius', 'service_type': 'UberX'}
    uber.register_driver(**driver_details)
