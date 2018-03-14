import pytest
import random

class Solution():
    def partition(self, arr, lo, hi):
        # lo will have our partition element, which will land in its original position by the end of this method.
        # pivot is the current probable location of arr[lo] which is our target
        pivot = random.randint(lo, hi)  # To prevent worst case for quicksort T(n) = T(n-1) + n
        # bring our target pivot to arr[0]
        arr[pivot], arr[lo] = arr[lo], arr[pivot]
        pivot = lo
        for i in xrange(lo + 1, hi + 1):
            if arr[i] < arr[lo]:
                pivot += 1
                arr[i], arr[pivot] = arr[pivot], arr[i]
        arr[lo], arr[pivot] = arr[pivot], arr[lo]
        return pivot

    def kth_largest_partitioning(self, arr, k):
        """
        Time, space along with strategy explained in:
        https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60309/4-C++-Solutions-using-Partition-Max-Heap-priority_queue-and-multiset-respectively
        """
        iteration = len(arr)
        lo, hi = 0, len(arr)-1
        k = len(arr) - k # This converts largest index to absolute index which can be easily compared with returned indices.
        while iteration: # can use while True also but seems un-necessary.
            iteration -= 1
            pos = self.partition(arr, lo, hi)
            if pos == k:
                return arr[pos]
            if pos < k:
                lo = pos + 1
            else:
                hi = pos - 1

    def kth_largest_heap(self, arr, k):
        '''
        Time: O(k) + O((n-k)logk), k for building the heap and then insert operation on the heap for n-k items.
        Space: O(k), size of the min heap
        Idea is to generate a min heap, and remove top of the heap or min elements whenever size gets equal to k.
        This makes sure of two things:
            1. Heap has always k elements. with kth max on min in k being on top.
            2. Poppping on heap will always prune min elements therefore in the end, we'll get
            a heap with k max elements of the array having n elements. Now since these are top k elements
            minimum of these would be the kth max in the sorted order.
        '''
        import heapq
        if not(1 <= k <= len(arr)):
            return -1
        heap = []
        for ele in arr:
            heap
        for index in xrange(k): # O(k)
            heap.append(arr[index])
        heapq.heapify(heap) # O(k)
        for index in xrange(k, len(arr)):
            heap.append(arr[index])
            heapq.heapify(heap)
            heapq.heappop(heap)
        return heap[0]

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (([3, 2, 1, 5, 6, 4], 2), 5),
        ])
    def test_task(self, args, result):
        sol = Solution()
        # assert sol.kth_largest_heap(*args) == result
        assert sol.kth_largest_partitioning(*args) == result
if __name__ == '__main__':
    arr, k = [3, 2, 1, 5, 6, 4], 2
    sol = Solution().kth_largest_partitioning(arr, k)
    print 'result is', sol
