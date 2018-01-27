'''
https://discuss.leetcode.com/topic/20681/20ms-c-solution-with-explanations/9

This is a nice trick used here: sum(vec2d, [])[::-1]
sum method uses + operator which here can be used to add or join in this case two lists.
Notice default value needs to be [] and not 0 which would result in trying to add int and list error
In [1]: vec = [[1,2],[3],[4,5,6]]

In [2]: sum(vec, [])[::-1]
Out[2]: [6, 5, 4, 3, 2, 1]
Unfortunately this approach take O(n) space so not very efficient
'''

class Vector2D(object):
    '''
    Convert a 2D array to 1D array is basically the exercise.
    Time: O(elements in the 2D vector array)
    Space: O(1) As we're just maintaining two pointers row and col and iterating over the array once.
    '''

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.arr = vec2d
        self.adjust_iter() # As arrays can have empty arrays within, so need to skip those before.
        

    def next(self):
        """
        :rtype: int
        """
        cur = self.arr[self.row][self.col]
        self.col += 1
        self.adjust_iter()
        return cur

        

    def hasNext(self):
        """
        :rtype: bool
        """
        # Essentially saying row and col pointers are not on the end of the array.
        return self.row != len(self.arr) and self.col != len(self.arr[self.row])

    def adjust_iter(self):
        '''
        To keep next method clean
        '''
        # As there can be multiple empty arrays with in outer array, skip all zero len arrays for which
        while self.row != len(self.arr) and self.col == len(self.arr[self.row]):
        	self.row += 1
        	self.col = 0
        
if __name__ == '__main__':
	#Your Vector2D object will be instantiated and called as such:
	vec2d = [[], [3]]
	i, v = Vector2D(vec2d), []
	while i.hasNext(): v.append(i.next())
	print v