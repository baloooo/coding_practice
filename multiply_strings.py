class Solution(object):
    def multiply(self, num1, num2):
        """
        There're lot of little caveats in this one, do implement it when going over.
        :type num1: str
        :type num2: str
        :rtype: str
        Idea: https://discuss.leetcode.com/topic/20883/simple-python-solution-18-lines/8
        Idea is to reverse both the nums strings and start from there multiplying each place
        digits. Core idea is to place num1[i] * num2[i] at product[i] and then initialize
        product[i-1] += product[i]/10 where product[i] might have 36 from multiplication above.
        and in next step normalize product[i] by product[i]/10, and keep moving forward with it.
        """
        def reverse(strs):
            '''
            so reverse is not called multiple times
            '''
            return ''.join([strs[i] for i in xrange(len(strs)-1, -1, -1)])
        product = [0]*(len(num1)+len(num2))
        pos = len(product) - 1
        num1, num2 = ''.join(reversed(num1)), num2[::-1] # showing 3 different ways to reverse inc/ above one.
        for n1 in num1:
            cur_pos = pos
            for n2 in num2:
                product[cur_pos] += int(n1) * int(n2)
                product[cur_pos-1] += (product[cur_pos]/10)
                product[cur_pos] %= 10
                cur_pos -= 1
            pos -= 1
        # Remove leading zeros.
        cur_pos = 0
        while cur_pos < len(product) and product[cur_pos] == 0:
            cur_pos += 1
        return ''.join(map(str, product[cur_pos:])) or '0'

	def multiply(self, num1, num2):
        """
		Time: O(n^2), space: O(n1 + n2), where n1 is len(num1) and n2 is len(num2)
		Another way to implement the same idea, but without explicitly reversing num1 and num2,
		rather just iterating from tail to start.
		Seems cleaner this way + more efficient since we're not reversing anything
        """
        product = [0]*(len(num1)+len(num2))
        product_pos = len(product) - 1
        for i in xrange(len(num1)-1, -1, -1):
            pos = product_pos
            for j in xrange(len(num2)-1, -1, -1):
                cur_prod = int(num1[i]) * int(num2[j])
                product[pos] += cur_prod
                product[pos-1] += product[pos]/10
                product[pos] = product[pos] % 10
                pos -= 1
            product_pos -= 1
        # Remove leading zeros and stringify ints + concatenate them to make a string.
        for msb in xrange(len(product)):
            if product[msb] != 0:
                break
        return ''.join(map(str, product[msb:]))

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
