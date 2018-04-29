class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        Idea is to convert 4 sum to 2 sum with hash map type solution
        Make hasmap with every possible combinations of A and B
        and for every possible sum of C and D perform 2 sum with hash map technique
        Idea: https://discuss.leetcode.com/topic/67658/simple-java-solution-with-explanation
        http://www.geeksforgeeks.org/find-four-elements-sum-given-value-set-3-hashmap/
        Time: O(n^2) n being the number of elements in "each" array.
        Space: O(n^2)

        https://www.geeksforgeeks.org/count-quadruples-four-sorted-arrays-whose-sum-equal-given-value-x/
        """
        from collections import defaultdict
        two_sum_map, count = defaultdict(int), 0
        for ele1 in A:
            for ele2 in B:
                cur_sum = ele1 + ele2
                two_sum_map[cur_sum] += 1
        for ele3 in C:
            for ele4 in D:
                cur_sum = -(ele3+ele4)
                if cur_sum in two_sum_map:
                    count += two_sum_map[cur_sum]
        return count
