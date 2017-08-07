class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0]*(len(num1)+len(num2))
        for i in xrange(len(num1)-1, -1, -1):
            for j in xrange(len(num2)-1, -1, -1):
                product[i+j] += int(num1[i])*int(num2[j])
                product[i+j-1] += product[i+j] / 10
                product[i+j] %= 10
        return ''.join([str(each) for each in product])


if __name__ == '__main__':
    test_cases = [
        # (('22', '22'), '484'),
        (('12', '12'), '144'),
        (('99', '99'), '9801'),
    ]
    for test_case in test_cases:
        res = Solution().multiply(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
