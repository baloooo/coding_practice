"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at
(i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the
container contains the most water.

Your program should return an integer which corresponds to the maximum area
of water that can be contained ( Yes, we know maximum area instead of maximum
volume sounds weird. But this is 2D plane we are working with for simplicity ).

 Note: You may not slant the container.
Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2.
Height of container = min(5, 3) = 3.
So total area = 3 * 2 = 6
"""


def max_container_area(arr):
    '''
    Idea:https://discuss.leetcode.com/topic/25004/easy-concise-java-o-n-solution-with-proof-and-explanation
    Also https://leetcode.com/articles/container-most-water/
    Crux of the idea is that we've to find the area which depends on x-distance and y-distance
    b/w two walls of the container in 2D plane. Now x-distance is governed by the distance
    b/w walls of the container and y-distance is governed by the minimum height b/w two walls.
    So the whole idea is to use two pointer tech. to have two pointers and scan thru the 
    arr to see how width*height value changes and since we want difference b/w heights of the
    wall to be as min as possible always move the wall with less height. Meanwhile keep
    recording the max_area seen so far.
    '''
    start, end = 0, len(arr)-1
    max_area = 0
    while(start < end):
        max_area = max(max_area, (end-start) * min(arr[start], arr[end]))
        if arr[start] < arr[end]:
            start += 1
        else:
            end -= 1
    return max_area

if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1]
    # arr = [1, 5, 4, 3]
    print max_container_area(arr)
