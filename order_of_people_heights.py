# coding: utf-8
"""
You are given the following :

A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the
number of persons who are taller than P and standing in front of P
You need to return list of actual order of persons’s height

Consider that heights will be unique

Example

Input :
Heights:  5 3 2 6 1 4
InFronts: 0 1 2 0 3 2
Output :
actual order is: 5 3 2 1 6 4
So, you can see that for the person with height 5, there is no one taller than
him who is in front of him, and hence Infronts has 0 for him.

For person with height 3, there is 1 person ( Height : 5 ) in front of him who
is taller than him.

You can do similar inference for other people in the list.
"""


class Solution:
    def reconstructQueue_BST(self, people):
        '''
        This
         has a O(nlogn) average time complexity
        algorithm using BST
        '''
        pass

    def reconstructQueue(self, people):
        """
	    from leetcode
        :type people: List[List[int]]
        :rtype: List[List[int]]
        Idea: https://discuss.leetcode.com/topic/60981/explanation-of-the-neat-sort-insert-solution
        Time: O(n^2) due to insert on lists
        The idea is to sort items based on their height in descending order and then just place them in
        an array based on their k value, similar to selection sort. As k-defines the number of items that 
        can be in front of a item and as we're picking items in height sorted order (largest first) the last
        item will be the smallest item and will tell us the exact location where it should be placed,
        we can't ignore any positions ahead of it b'coz everyone is bigger than him so he definitely
        counted accurately everyone in front of him.Whereas on the other hand the larger guys we
        placed initially had the liberty of counting only the persons taller than them so their
        count was not so accurate, so we delibarately placed them before and the smaller persons had
        more control over their location since "they had to be more accurate since they didn't
        skip anyone".
        """
        arr = []
        for candidate in sorted(people, key=lambda (h,k): (-h,k)):
            arr.insert(candidate[1], candidate)
        return arr 

    def construct_queue(self, heights, in_fronts):
        people = [[height, in_front] for height, in_front in zip(heights, in_fronts)]  # noqa
        queue = []
        people.sort(key=lambda (height, in_front): (-height, in_front))
        for person in people:
            queue.insert(person[1], person)
        return [each[0] for each in queue]

if __name__ == '__main__':
    heights, in_fronts = [5,3,2,6,1,4], [0,1,2,0,3,2]
    print Solution().construct_queue(heights, in_fronts)
    print "5 3 2 1 6 4"
