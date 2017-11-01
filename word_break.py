

class Solution:
    def word_break(self, start, word_set, target):
        if start == len(target):
            return True
        for i in xrange(start, len(target)):
            prefix = ''.join(target[start:i+1])
            # print prefix
            if prefix in word_set and self.word_break(i+1, word_set, target):
                return True
        return False

    def word_break_recursion(self, target, word_list):
        '''
        http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
        time: O(2^n) n = len(target)
        '''
        word_set = set(word_list)
        return self.word_break(0, word_set, target)

    def word_break_dp(self, target, word_list):
        '''
        Time: O(n^2) but can be coded as O(n*k) where n = len(target) and k = len(word_list)
        Todo: check O(n*k) version for usecases where len(word_list) is small and target string too big.
        https://discuss.leetcode.com/topic/6156/java-implementation-using-dp-in-two-ways/44
        https://github.com/kamyu104/LeetCode/blob/master/Python/word-break.py O(n*k)
        '''
        word_set = set(word_list)
        # dp[i] is True if target[0, i-1] can be segmented into dictionary words
        dp = [False] * (len(target)+1)
        for i in xrange(1, len(target)+1):
            if dp[i] is False and target[:i] in word_set:
                dp[i] = True
            if dp[i]:
                for j in xrange(i+1, len(target)+1):
                    if dp[j] is False and target[i:i+j] in word_set:
                        dp[j] = True
                if dp[len(target)]: return True
        return dp[len(target)]

    def word_break2(self, word_list, target):
        pass

if __name__ == '__main__':
    test_cases = [
        (('leetcode', ['leet', 'code']), True),
        (('ilikegoogle', ['i', 'li', 'like', 'g', 'goo', 'oo', 'gle']), True),
        (('ilikesamsung', ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice']), True),
        (('abcd', ['a', 'abc', 'b', 'cd']), True),
    ]
    for test_case in test_cases:
        res = Solution().word_break_dp(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
