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
    Code: https://discuss.leetcode.com/topic/25004/easy-concise-java-o-n-solution-with-proof-and-explanation
    Idea: https://leetcode.com/articles/container-most-water/
    The intuition behind this approach is that the area formed between the lines will
    always be limited by the height of the shorter line. Further, the farther the lines,
    the more will be the area obtained.
    We take two pointers, one at the beginning and one at the end of the array constituting the
    length of the lines. Futher, we maintain a variable maxareamaxarea to store the maximum area
    obtained till now. At every step, we find out the area formed between them, update maxarea
    and move the pointer pointing to the shorter line towards the other end by one step.
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
