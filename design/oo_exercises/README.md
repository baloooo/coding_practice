Design patterns skim: design_patterns/

https://github.com/donnemartin/system-design-primer#object-oriented-design-interview-questions-with-solutions

ParkingLot
FoodDeliveryApp
    UberBackend
    GarbageCollector
    in_memory_file_system
    air traffic control
    python-elevator-challenge
    elevator_control_system

Design patterns:

    Creational:
        - pool: This pattern is used when creating an object is costly (and they are created frequently) but only a few are used at a time. With a Pool we can manage those instances we have as of now by caching them. Now it is possible to skip the costly creation of an object if one is available in the pool.  A pool allows to 'check out' an inactive object and then to return it.  If none are available the pool creates one to provide without wait.  - Singleton: The Borg pattern (also known as the Monostate pattern) is a way to implement singleton behavior, but instead of having only one instance of a class, there are multiple instances that share the same state. In other words, the focus is on sharing state instead of sharing instance identity. Can be used for logging.
        - Factory: Base method for creating objects from base classes.

    Structural:
        - Adapter: Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.
        - decorator: Add a feature/functionality dynamically.
        - facade: Simpler unified interface to complex systems
        - mvc:
    Behavioral:
        - Publisher/subscriber: Get Notifications on events.
		- observer: Maintain a list of observers and notify them of changes
        - Strategy: ?
        - memento: Provides the ability to restore an object to its previous state. This can be for rolling back a transaction or such.
        - catalog: A class that uses different static function depending of a parameter passed in
init. Note the use of a single dictionary instead of multiple conditions
        - Command: Encapsulate all info needed to perform an operation in to object.
