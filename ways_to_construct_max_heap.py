# coding: utf-8
"""
Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes

So now the problem statement for this question is:

How many distinct Max Heap can be made from n distinct integers

In short, you have to ensure the following properties for the max heap :

Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last,
is completely filled, and all nodes are as far left as possible. )
Every node is greater than all its children
Let us take an example of 4 distinct integers. Without loss of generality let us take 1 2 3 4 as our 4 distinct integers

Following are the possible max heaps from these 4 numbers :

         4 
       /  \ 
      3   2 
     / 
    1
         4 
       /  \ 
      2   3 
     / 
    1
        4 
       /  \ 
      3   1 
     / 
    2
These are the only possible 3 distinct max heaps possible for 4 distinct elements.

Implement the below function to return the number of distinct Max Heaps that is possible from n distinct elements.

As the final answer can be very large output your answer modulo 1000000007

Input Constraints : n <= 100
"""

"""
can be done using formulae, this is a brute force implementation.
"""
class Solution:
    def __init__(self):
        self.permutations = []

    def permute(self, arr, start, end):
        if start == end:
            self.permutations.append(arr[::])
            return
        for index in xrange(start, end):
            arr[index], arr[start] = arr[start], arr[index]
            self.permute(arr, start+1, end)
            arr[index], arr[start] = arr[start], arr[index]


    def make_max_heap(self, arr):
        from math import ceil
        for index in xrange(1, len(arr)):
            parent_index = int(ceil(index/2.0))-1
            while parent_index >= 0 and arr[index] > arr[parent_index]:
                arr[index], arr[parent_index] = arr[parent_index], arr[index]
                index = parent_index
                parent_index = int(ceil(index/2.0))-1
        return arr



    def ways_max_heap(self, num_range):
        # Time: O(n!*nlogn)
        # since all the n! permutations will have different root, they will create different max heaps.
        # and nlogn for creating a heap of n nodes.
        arr = range(1, num_range+1)
        max_heap_set = set()
        self.permute(arr, 0, len(arr))
        for cur_permutation in self.permutations:
            cur_max_heap = self.make_max_heap(cur_permutation)
            max_heap_set.add(tuple(cur_max_heap))
        return len(max_heap_set) % 1000000007

if __name__ == '__main__':
    test_cases = [
        (4, 3),
        (20,  258365767),
    ]
    for test_case in test_cases:
        res = Solution().ways_max_heap(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(test_case[0], res, test_case[1])
