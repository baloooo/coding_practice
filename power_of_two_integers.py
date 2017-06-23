

class Solution:
    def power_of_two_integers(self, num):
        if num == 1:
            return True
        for base in xrange(2, int(num**0.5)+1):
            for exponent in xrange(2, num+1):
                res = base ** exponent
                if res > num:
                    break
                if res == num:
                    return True
        return False

if __name__ == '__main__':
    test_cases = [
        (4, True),
    ]
    for test_case in test_cases:
        res = Solution().power_of_two_integers(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
