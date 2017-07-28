

class Solution:
    def power_of_two(self, n):
        """
        Notice this idea would also take care of negative numbers than using a mask and traversing over bits of the number
        The number will be of the binary form 1000...000. When you -1 it, it will be of the form 0111...111. Thus, the two number's binary and would result is 000000. This wouldn't happen for non-power-of-twos, since 1010100 for example would become 1010011, resulting in an Resulting in a 1010000 after the binary and. The only false positive would be 0, which is why I would use: return (x != 0) && ((x & (x - 1)) == 0)
        """
        return bool(n!=0 and not (n&(n-1)) )

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
