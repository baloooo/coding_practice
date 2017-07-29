# -*- coding: utf-8 -*-

"""

A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position.

Example :

    The array is [1 3 -1 -3 5 3 6 7], and w is 3.

    Window positionMax   
    [1 3 -1] -3 5 3 6 73
    1 [3 -1 -3] 5 3 6 7331 3 [-1 -3 5] 3 6 733151 3 -1 [-3 5 3] 6 73315151 3 -1 -3 [5 3 6] 7331515161 3 -1 -3 5 [3 6 7]73315151617Input: A long array A[], and a window width w
    Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
    Requirement: Find a good optimal way to get B[i]

     Note: If w > length of the array, return 1 element with the max of the array. 
"""


def sliding_window_max(arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    Idea: http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
    """
    from collections import deque
    if not arr:
        return []
    q = deque()
    res = []
    # Parse starting window size elements
    for index in range(k):
        while len(q) and arr[index] > arr[q[-1]]:
            q.pop()
        q.append(index)
    for index in xrange(k, len(arr)):
        """
        The element at the front of the queue is the largest element of
        previous window, so print it
        """
        res.append(arr[q[0]])
        # Remove all elements from front that went out of the window
        while len(q) and index - k + 1 > q[0]:
            q.popleft()  # Remove from front of Queue
        """
        Remove all elements smaller than the currently
        being added element (remove useless elements)
        """
        while len(q) and arr[index] >= arr[q[-1]]:
            q.pop()
        # Add current element to the rear
        q.append(index)
    # Add maximum element of the last window
    res.append(arr[q[0]])
    return res

# def sliding_window_max(stream, window_size):
#     from collections import deque
#     window_max_list = []
#     # q has the index elements
#     asc_q = deque()
#     # Add first k useful elements
#     for index, ele in enumerate(stream[:window_size]):
#         while(asc_q and stream[asc_q[0]] <= ele):
#             asc_q.popleft()
#         asc_q.appendleft(index)
#     for index, cur_ele in enumerate(stream[window_size:], start=window_size):
#         # add asc_q front element to window_max_list
#         window_max_list.append(stream[asc_q[-1]])
# 
#         # Remove front element if this went out of window.
#         # Todo: see if there can be multiple instance of this
#         while (asc_q and (asc_q[-1] < (index-window_size+1))):
#             asc_q.pop()
# 
#         while(asc_q and (cur_ele >= stream[asc_q[0]])):
#             # Pop elements until cur_ele is the biggest element
#             asc_q.popleft()
#         asc_q.appendleft(index)
#     window_max_list.append(stream[asc_q[-1]])
#     return window_max_list


if __name__ == '__main__':
    # stream = [4, 4, 4, 4, 4, 4, 4, 4, 4]
    # stream, window_size= [1, 3, -1, -3, 5, 3, 6, 7], 3
    # stream = [12, 1, 78, 90, 57, 89, 56]
    # stream, window_size = [1], 1
    # stream, window_size = [4, -2], 2
    # stream, window_size = [1, -1], 1
    # stream, window_size = [1], 1
    stream, window_size = [7, 2, 4], 2
    print sliding_window_max(stream, window_size)
