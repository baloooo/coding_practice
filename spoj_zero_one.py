"""
PS: Smallest Multiple With 0 and 1
You are given an integer N. You have to find smallest multiple of N which
consists of digits 0 and 1 only. Since this multiple could be large, return
it in form of a string.

Note:
- Returned string should not contain leading zeroes.

For example,

For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.

Algo:

You need to search for the smallest number to multiply N by.

I would construct the number incrementally, starting from the least significant
digit.

Supposing N=7. What are the possible least significant digits of the
multiplying number? It will be a number which, when you multiply by 7, will
have a result with the least significant digit of 0 or 1.
If you try the numbers from 0-9, it can only be '0' or 3'.

+-------+--------+------+
| Digit | Result | Pass |
+-------+--------+------+
| 0     |  0     | Yes  |
| 1     |  7     | No   |
| 2     | 14     | No   |
| 3     | 21     | Yes  |
| 4     | 28     | No   |
| 5     | 35     | No   |
| 6     | 42     | No   |
| 7     | 49     | No   |
| 8     | 56     | No   |
| 9     | 63     | No   |
*-------*--------*------*

Then you try the second least significant digit. You will now try 00, 10, 20,
30, 40, 50, 60, 70, 80, 90 and 03,13,23,43,53,63,73,83,93.
The successful candidates will be the ones when, multiplied by 7, produce a
number in which the two least significant digits are 0 or 1.
You are left with '43', '30', '00', and '01'.

Repeat this process with the 3rd digit, finding the number which produces a
multiple with 3 least significant digits meeting the qualities.

During the process you will find a number in which ALL of the digits meet the
qualities, and that's your answer. In the case of N=7, you've found it by the
3rd digit. (7 * 143 == 1001).

"""


class Solution:
    def __init__(self):
        pass

    def all_zero_one(self, result):
        for digit in result:
            if digit not in ['0', '1']:
                return False
        return True

    def zero_one_multiple_new(self, multiplicand):
        for k_size in xrange(1, 100):
            candidate = '0'*k_size
            for index in xrange(len(candidate)-1, -1, -1):
                candidate[index] = 1
                if int(candidate) % multiplicand == 0:
                    return candidate

    def zero_one_multiple(self, multiplicand):
        multiplier_list = ['']
        iteration_index = 1
        while multiplier_list:
            new_multiplier_list = []
            for num in multiplier_list:
                for unit_place in xrange(10):
                    new_multiplier_list.append(
                        str(unit_place) + str(num))
            multiplier_list = new_multiplier_list
            new_multiplier_list = []
            for multiplier in multiplier_list:
                result = str(int(multiplier) * multiplicand)
                if int(result) and self.all_zero_one(result):
                    return result
                try:
                    if result[-iteration_index] in ['0', '1']:
                        new_multiplier_list.append(multiplier)
                        # print multiplier
                except:
                    new_multiplier_list.append(multiplier)
                    # print multiplier
            multiplier_list = new_multiplier_list
            iteration_index += 1

n = int(raw_input())
for _ in xrange(n):
    m = int(raw_input())
    print Solution().zero_one_multiple(m)

#     print Solution().zero_one_multiple(3456)  # 11011111110000000
# if __name__ == '__main__':
#     # print Solution().zero_one_multiple(479)  # 100111
#     print Solution().zero_one_multiple(3456)  # 11011111110000000
#     # print Solution().zero_one_multiple(325)  # 100100
