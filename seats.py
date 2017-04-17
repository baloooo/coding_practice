"""
There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

Return minimum value % MOD where MOD = 10000003

Example

Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -

              . . . . x . . x x . . . x . .

Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .

Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -  
    Number of jumps by him =   (6 - 4) = 2

2 - Bring the person sitting at 12th index to 9th index - 
    Number of jumps by him = (12 - 9) = 3

So now the total number of jumps made = 
    ( 2 + 3 ) % MOD = 
    5 which is the minimum possible jumps to make them seat together.

There are also other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.

For example bring them all towards the starting of the row i.e. start placing them from index 0. 
In that case the total number of jumps will be 
    ( 4 + 6 + 6 + 9 )%MOD 
    = 25 which is very costly and not an optimized way to do this movement

"""


class Solution:
    def __init__(self):
        pass

    def seats(self, inp):
        MOD = 10000003
        # str_arr = inp.split('')
        arr = [index for index, ele in enumerate(inp) if ele == 'x']
        if not arr:
            return 0
        median = len(arr)/2
        cur_index = median - 1
        moves = 0
        left_boundary = arr[median]
        while(cur_index >= 0):
            moves += left_boundary - arr[cur_index] - 1
            left_boundary -= 1
            cur_index -= 1
        cur_index = median + 1
        right_boundary = arr[median]
        while(cur_index < len(arr)):
            moves += arr[cur_index] - right_boundary - 1
            right_boundary += 1
            cur_index += 1
        return moves % MOD

if __name__ == '__main__':
    test_cases = [
        ('....x..xx...x..', 5)
        # ('. . . . x . . x x . . . x . .', 5),
        # ('. . . . x x x x x x . .', 0),
        # ('x x x x x x', 0),
        # ('x', 0),
    ]
    for test_case in test_cases:
        res = Solution().seats(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
