class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        Idea: https://discuss.leetcode.com/topic/67658/simple-java-solution-with-explanation
        Time: O(n^2) n being the number of elements in "each" array.
        Space: O(2n)
        """
        two_sum_map, count = collections.defaultdict(int), 0
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
