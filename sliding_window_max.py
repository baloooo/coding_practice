# -*- coding: utf-8 -*-

def sliding_window_max(arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    Idea: http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
    We create a Dequeue, Qi of capacity k, that stores only useful elements of current window of k elements. An element is useful if it is in current window and is greater than all other elements on left side of it in current window. We process all array elements one by one and maintain Qi to contain useful elements of current window and these useful elements are maintained in sorted order. The element at front of the Qi is the largest and element at rear of Qi is the smallest of current window
    There're two kind of pops here, one is to remove all elements smaller than element to be added from the rear of the queue.
    Second is while adding each element after the first k elements pop all elements from the front of the queue that went
    outside the k window size.
    """
    from collections import deque
    if not arr:
        return []
    q = deque() # q = [Front ........ Rear]
    res = []
    # Parse starting window size elements
    for index in range(k):
        # For very element, the previous smaller elements are useless so remove them from Qi
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
        while len(q) and arr[index] > arr[q[-1]]:
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
