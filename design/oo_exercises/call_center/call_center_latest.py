from abc import ABCMeta, abstractmethod
from collections import deque
from enum import Enum


class Rank(Enum):

    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class Employee(object):
    __metaclass__ = ABCMeta

    def __init__(self, employee_id, name, rank, call_center):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.on_call = None
        self.call_center = call_center

    def take_call(self, call):
        """Assume the employee will always successfully take the call."""
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS

    def complete_call(self):
        self.call.state = CallState.COMPLETE
        self.call_center.notify_call_completed(self.call)

    @abstractmethod
    def escalate_call(self):
        pass

    def _escalate_call(self):
        self.call.state = CallState.READY
        call = self.call
        self.call = None
        self.call_center.notify_call_escalated(call)


class Operator(Employee):

    def __init__(self, employee_id, name):
        super(Operator, self).__init__(employee_id, name, Rank.OPERATOR)

    def escalate_call(self):
        '''
        State change (State Design Pattern)
        '''
        self.call.level = Rank.SUPERVISOR
        self._escalate_call()


class Supervisor(Employee):

    def __init__(self, employee_id, name):
        super(Supervisor, self).__init__(employee_id, name, Rank.SUPERVISOR)

    def escalate_call(self):
        self.call.level = Rank.DIRECTOR
        self._escalate_call()


class Director(Employee):

    def __init__(self, employee_id, name):
        super(Director, self).__init__(employee_id, name, Rank.DIRECTOR)

    def escalate_call(self):
        raise NotImplemented('Directors must be able to handle any call')


class CallState(Enum):

    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class Call(object):

    # Default all calls go to operator, if not present they'll be escalated.
    def __init__(self, rank=Rank.OPERATOR):
        self.state = CallState.READY
        self.rank = rank
        self.employee = None


class CallCenter(object):

    def __init__(self, operators, supervisors, directors):
        self.operators = operators
        self.supervisors = supervisors
        self.directors = directors
        self.queued_calls = deque()
        # when calls complete shove them over to completed calls list, so as to have
        # them for Internal quality check log or similar.
        self.completed_calls = []

    def dispatch_call(self, call):
        if call.rank not in (Rank.OPERATOR, Rank.SUPERVISOR, Rank.DIRECTOR):
            raise ValueError('Invalid call rank: {}'.format(call.rank))
        employee = None
        if call.rank == Rank.OPERATOR:
            employee = self._dispatch_call(call, self.operators)
            # Makes sure, if there is no Operator FREE Supervisor should take the call
            # This is the Chain of responsibility design pattern where
            # The derived classes know how to satisfy Client requests.
            # If the "current" object is not available or sufficient, then it
            # delegates to the base class, which delegates to the "next" object,
            # and the circle of life continues.
            # https://sourcemaking.com/design_patterns/chain_of_responsibility
            if employee is None:
                call.rank = Rank.SUPERVISOR
        if call.rank == Rank.SUPERVISOR or employee is None:
            employee = self._dispatch_call(call, self.supervisors)
            if employee is None:
                call.rank = Rank.DIRECTOR
        if call.rank == Rank.DIRECTOR or employee is None:
            employee = self._dispatch_call(call, self.directors)
        if employee is None: # Calls are queued if there's no one to attend
            self.queued_calls.append(call)

    def _dispatch_call(self, call, employees):
        '''
        Goes over list of Employees class(Operator, Supervisors, etc)
        and selects first available employee and assigns him the call
        This employee list can be made in to a LinkedList where available will
        have list of all available employees
        When a busy employee is freed, we can just de-attach him from busy linked list
        and attach him to available linked list. This would enable O(1) time for 
        getting an available employee for the new call instead of O(n) we've right now.
        '''
        for employee in employees:
            if employee.call is None:
                employee.take_call(call)
                return employee
        return None

    def notify_call_escalated(self, call):
        """
        Returns 'call escalated' message, and returns back the employee to list.
        Call is put in to front of the queue to be handled by the appropriate
        employee if all of them are busy at the moment.
        """
        pass

    def notify_call_completed(self, call):
        """
        sets the call status to complete, and puts back the employee in to his list.
        """
        pass

    def periodic_in_queue_calls_check(self):
        """
        Periodically checks for pending/queued calls waiting to be serviced
        """
        for call in self.queued_calls:
            self.dispatch_call(call)

if __name__ == '__main__':
    # These should preferably be LinkedLists so we can remove and add operators easily
    # as they complete their call.
    operators, supervisors, directors = [], [], []
    for employee_id in xrange(1, 6):
        operators.append(Operator(employee_id))
    for employee_id in xrange(6, 8):
        supervisors.append(Operator(employee_id))
    for employee_id in xrange(8, 9):
        directors.append(Operator(employee_id))
    call_center = CallCenter(operators, supervisors, directors)
    for _ in xrange(5):
        call_center.dispatch_call(Call())

    '''
    Start small and expand gradually.
    Create Abstract class employee, and child classes (Operator, Superivisor, Director) with their respective
    ranks.
    Create a call center and create queued_calls and completed calls queue. All incoming calls go to
    queued_calls queue and a periodic method should try to go over all queued calls and assign it to
    requested employees. Employees themselves can have two separate lists (available, busy) so that we can get an     available employee with O(1).Calls themselves will hold the state of the call, operators
    assigned(possibly as as list) and other relevant info.
    Each employee can define their own escalate call methods which would put the call back in queue with desired
    employee rank as one higher than the current or as requested by the call.
    Things like call states, Employee ranks should be made Enums.
    Employee base class should be a metaclass and define some abstract methods like escalate_call, receive_call
    etc.
    '''
