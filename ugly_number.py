class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        Time: Max of (log2(n), log3(n), log5(n)) therefore log2(n)
        """
        if num in [0, 1]: return bool(num)
        while num % 2 == 0: num = num/2
        while num % 3 == 0: num = num/3
        while num % 5 == 0: num = num/5
        return num == 1
