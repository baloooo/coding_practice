'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

import pytest
import collections

def cmp_persons(person1, person2):
    '''
    return
        -1 if person1 < person2
        0 if person1 == person2
        +1 if person1 > person2
    '''
    if person1.height < person2.height:
        return 1
    elif person1.height > person2.height:
        return -1
    elif person1.height == person2.height and person1.in_front != person2.in_front:
        if person1.in_front <= person2.in_front:
            return 1
        else:
            return -1
    else:
        return 0

class Person(object):
    def __init__(self, height, in_front):
        self.height = height
        self.in_front = in_front

class PersonNode(object):
    def __init__(self, height, in_front):
        self.height = height
        self.in_front = in_front
        self.left = None
        self.right = None

class Solution(object):
    def reconstructQueue(self, person_info_list):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        person_object_list = self.get_people_object_list(person_info_list)
        root = PersonNode(person_info_list[0].height, person_info_list[1].in_front)
        self.create_persons_height_tree(root, 1, person_object_list)
        self.reconstructed_queue = []
        self.inorder(root)
        return self.reconstructed_queue

    def inorder(self, root):
        pass

    def create_persons_height_tree(self, root, person_object_list_idx, person_object_list):
        if person_object_list_idx == len(person_object_list):
            return
        cur_person = person_object_list[person_object_list_idx]
        if cur_person.in_front > root.in_front: # go left
            if root.left is None:
                cur_person_tree_node_obj = PersonNode(cur_person.height, cur_person.in_front)
                root.left = cur_person_tree_node_obj
            else:
                self.create_persons_height_tree(root.left, person_object_list_idx, person_object_list)
            root.in_front += 1
        else: # go right
            if root.right is None:
                cur_person_tree_node_obj = PersonNode(cur_person.height, cur_person.in_front)
                root.right = cur_person_tree_node_obj
            else:
                self.create_persons_height_tree(root.right, person_object_list_idx, person_object_list)


    def get_people_object_list(self, people_info_list):
        persons_list = []
        for height, in_front in people_info_list:
            person = Person(height, in_front)
            persons_list.append(person)
        # Add sorting on second attribute also.
        persons_list.sort(cmp=cmp_persons)
        return persons_list

if __name__ == '__main__':
    input_str, expected_output = ["ab", "ba"], 1
    input_str, expected_output = ["abc", "bca"], 2
    input_str, expected_output = ["aabc", "abca"], 2
    input_str, expected_output = ["aaaabbbbccccddddeeee","abcdeabcdeabcdeabcde"], 8
    res = Solution().test_code(*input_str)
    print "Input {0}".format(input_str)
    print "Output   {0}".format(res)
    if not res == expected_output:
        print "expected {0}".format(expected_output)



'''
class TestShortestDistance(object):
    def setUp(self):
        #self.test_object = Solution()
        pass

    @pytest.mark.parametrize("input, expected_output", [
        ([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]], 7),
        ([[1]], -1),
        ([[1, 0]], 1),
        ([[1, 1], [0, 1]], -1),
    ])
    def test_shortest_distance(self, input, expected_output):
        #assert self.test_object.shortestDistance(**input) == expected_output
        sol = Solution()
        assert sol.shortestDistance2(input) == expected_output
        #assert sol.shortestDistance1(input) == expected_output

    def tearDown(self):
        pass

'''