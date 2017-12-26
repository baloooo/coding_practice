import collections

class Solution:
    def word_break_latest(self, target, word_list):
        '''
        This is seems to be more optimized than all the other solutions for word_break1. Also this
        solution is more intutive than other solutions. On top of that this logic is very similar to
        the one we use in word_break2 so that's also a plus point.
        '''
        if not target:
            return True
        if not word_list:
            return not target
        # Note: dp[i] is True if target[0, i-1] can be segmented into dictionary words
        dp = [False] * (len(target)+1)
        dp[0] = True # We can always get empty string from word_list by not taking any word at all, so always True.
        word_len_to_set_map = collections.defaultdict(set)
        for word in word_list:
            word_len_to_set_map[len(word)].add(word)
        for start in xrange(len(target)):
            if dp[start] is False:
                continue
            for length, word_set in word_len_to_set_map.iteritems():
                if target[start: start+length] in word_set:
                    dp[start+length] = True
                if dp[-1] is True:
                    return True
        return dp[-1]


    def dfs(self, index_to_words, target, word_set, start, word_len_set):
        if start not in index_to_words:  # word_break for cur_len has not been calculated
            res = []
            # as we only want to get chunks of lens we've words of.
            for candidate_len in word_len_set:
                prefix = target[start:start+candidate_len]
                if prefix in word_set:
                    for word in self.dfs(index_to_words, target, word_set,
                                         start+candidate_len, word_len_set):
        #https://stackoverflow.com/questions/19213535/using-and-and-or-operator-with-python-strings
                        # res.append(prefix + (word and ' '+word))
                        res.append(prefix + ((' '+word if word else word)))
            index_to_words[start] = res
        return index_to_words[start]

    def word_break2(self, target, word_list):
        '''
        solution from top solutions submitted dashboard (not discuss)
        Time:
        Space:
        https://github.com/kamyu104/LeetCode/blob/master/Python/word-break-ii.py
        '''
        word_set = set()
        word_len_set = set()
        for word in word_list:
            word_len_set.add(len(word))
            word_set.add(word)
        '''This is a start index in text to possible words we can find that 
        exist in the word_list
        {0: ['i like sam sung', 'i like samsung'],
         1: ['like sam sung', 'like samsung'],
         5: ['sam sung', 'samsung'],
         8: ['sung'],
         12: [''],
         14: [],
         15: []}
        '''
        index_to_words = {len(target): ['']}
        word_breaks = self.dfs(index_to_words, target, word_set, 0, word_len_set)
        import ipdb; ipdb.set_trace()
        return sorted(word_breaks)
        # return sorted(self.dfs(dp, target, word_set, 0, word_len_set))



#################################################################################################
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
        https://stackoverflow.com/questions/31370674/time-complexity-of-the-word-break-recursive-solution
        time: O(2^n)
        Since in each step we're passing down target with one less char to parse in worst case.
        T(n) = T(n-1) + T(n-2) + T(n-3) + ... which is equal to 2^n.
        '''
        word_set = set(word_list)
        return self.word_break(0, word_set, target)

    def word_break_dp(self, target, word_list):
        '''
        Time: O(n^2) but can be coded as O(n*k) where n = len(target) and k = len(word_list)
        Todo: check O(n*k) version for usecases where len(word_list) is small and target string too big.
        IB strictly required n*k version w/ optimizations.
        https://discuss.leetcode.com/topic/6156/java-implementation-using-dp-in-two-ways/44
        https://github.com/kamyu104/LeetCode/blob/master/Python/word-break.py O(n*k)

        Below link has commented explanation of below code.
        https://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
        '''
        word_set = set(word_list)
        # Note: dp[i] is True if target[0, i-1] can be segmented into dictionary words
        dp = [False] * (len(target)+1) # since we need result from 0 to i
        for i in xrange(1, len(target)+1):
            if dp[i] is False and target[:i] in word_set:
                dp[i] = True
            if dp[i]:
                for j in xrange(i+1, len(target)+1):
                    if dp[j] is False and target[i:j] in word_set:
                        dp[j] = True
                if dp[len(target)]: return True
        return dp[len(target)]

    def word_break_dp_another(self, target, word_list):
        # https://github.com/kamyu104/LeetCode/blob/master/Python/word-break.py
        # Time: 
        word_set = set(word_list)
        max_len = 0
        for word in word_set:
            max_len = max(max_len, len(word))
        can_break = [False] * (len(target)+1)
        can_break[0] = True # since target[0: 0-1] that is null string will always be true
        '''
        i is the forward pointer, and j is the back pointer that travels all the way
        up untill i
        Todo:
        1. why j starts from 1, why not zero
        2. why break at # 68
        '''
        for i in xrange(1, len(target)+1):
            for j in xrange(1, min(max_len, i) + 1):
                '''
                can_break[i-j] ensures target[0:i-j] is in word set, and we'll therefore
                check remaining target up untill i, i.e target[i-j: i] in word_set
                '''
                if can_break[i-j] and target[i-j: i] in word_set:
                    # since target[0:i-j] is in set already and target[i-j:i] is now also
                    # set can_break[i] saying target[0:i] is in word_set
                    can_break[i] = True
                    break
        return can_break[len(target)]

    



if __name__ == '__main__':
    test_cases = [
        # (('leetcode', ['leet', 'code']), True),
        # (('ilikegoogle', ['i', 'li', 'like', 'g', 'goo', 'oo', 'gle']), True),
        (('ilikesamsung', ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice']), True),
        # (('abcd', ['a', 'abc', 'b', 'cd']), True),
        # (('myinterviewtrainer', ["interview", "my", "trainer"]), True),
        # (('aabbbabaaabbbabaabaab', ["bababbbb", "bbbabaa", "abbb", "a", "aabbaab", "b", "babaabbbb", "aa", "bb" ]), "abcde")
    ]
    for test_case in test_cases:
        res = Solution().word_break2(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
