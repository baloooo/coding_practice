class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total_res = []
        # multiplication stage
        for index, top_num in enumerate(num2):
            carry, res = 0, []
            for bot_num in num1:
                mul = int(top_num) * int(bot_num) + carry
                if len(str(mul)) > 1:
                    carry = int(str(mul)[:-1])
                import ipdb; ipdb.set_trace()
                res.append(str(mul)[-1])
            res = [res.append('0') for _ in xrange(index)]
            total_res.append(res)
        # Addition stage
        import ipdb; ipdb.set_trace()

if __name__ == '__main__':
    test_cases = [
        (('22', '22'), '484'),
    ]
    for test_case in test_cases:
        res = Solution().multiply(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
