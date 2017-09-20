"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

class Solution:
    def __init__(self):
        pass

    def swap_ll(self, head):
        pass

if __name__ == '__main__':
    test_cases = [ 
        ([], []),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2], [1, 2]),
        ([1], [1]),
    ]   
    for index, test_case in enumerate(test_cases, 1):
        head = construct_linked_list_from_array(test_case[0])
        res = Solution().swap_ll(head)
        expected_res = construct_linked_list_from_array(test_case[1])
        if compare_two_linked_lists(res, expected_res):
            print "%d: Passed" % index
        else:
            print "%d: Failed" % index
