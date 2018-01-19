class MovingAverage(object):
    '''
    https://discuss.leetcode.com/topic/44108/java-o-1-time-solution
    The idea is to have a pointer 'ins_at' in the array and have it on the location
    that contains the most stale value.
    When a new value comes in subtract the value at that pointer from the cur_sum and add the
    new value in to the array, add value to cur_sum and move the pointer.
    This way we won't have to calculate cur_sum again and again and can have a running updated
    sum of the array.
    Notice we'll have to have a variable n to keep the lenght of array as for initial values
    n will be less than lenght of arr so we'll have to use n and not len of self.arr
    '''

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.arr = [0]*size
	    # Location where new element can be stored, also the location of most
		# stale element that will go out of window.
        self.ins_at = 0
        self.cur_sum = 0
        self.n = 0

    def next(self, val):
        """
        returns cur average after adding passed in value.
        :type val: int
        :rtype: float
        """
        if self.n < self.arr: self.n += 1
        self.cur_sum -= self.arr[self.ins_at]
        self.arr[self.ins_at] = val
        self.cur_sum += val
        self.ins_at = (self.ins_at + 1 ) % len(self.arr)
        return self.cur_sum / float(self.n*1.0)
        

if __name__ == '__main__':

    # Your MovingAverage object will be instantiated and called as such:
    obj = MovingAverage(3)
    print obj.next(1)
    print obj.next(10)
    print obj.next(3)
    print obj.next(5)
    # param_1 = obj.next(val)
