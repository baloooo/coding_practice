"""
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""


def my_reverse(self, x):
    ans = 0
    if x >= 0:
        while x:
            # ans*10, since one unit place was added with this iteration.
            # x%10 to get the current tail of x
            ans = ans * 10 + x % 10
            x /= 10
        return ans if ans <= 2147483647 else 0  # Handle overflow.
    else:
        return -self.my_reverse(-x)


def reverse_integer(num):
    sign = False
    if num<0:
        sign = True
        num = abs(num)
    reversed_num = 0
    num_len = len(str(num)) - 1
    index = 0
    while(index<=num_len):
        rem = num%10
        reversed_num += (10**(num_len-index))*rem
        num /= 10
        index += 1
    return -reversed_num if sign else reversed_num


if __name__ == '__main__':
    num = -123
    print reverse_integer(num)



