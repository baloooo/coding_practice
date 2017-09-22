"""
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.
"""


def binary_add(x, y):
    # {(x, y, Carry_in): (sum, Carry_out)}
    binary_add_map = {
        ('0', '0', '0'): ('0', '0'),
        ('0', '0', '1'): ('1', '0'),
        ('0', '1', '0'): ('1', '0'),
        ('0', '1', '1'): ('0', '1'),
        ('1', '0', '0'): ('1', '0'),
        ('1', '0', '1'): ('0', '1'),
        ('1', '1', '0'): ('0', '1'),
        ('1', '1', '1'): ('1', '1')
    }
    carry = '0'
    x_len = len(x)
    y_len = len(y)
    max_len = x_len
    if x_len != y_len:
        # Match lengths so we don't have to any extra vodoo
        if x_len > y_len:
            y = '0'*(x_len-y_len) + y
        else:
            x = '0'*(y_len-x_len) + x
            max_len = y_len
    net_sum = [0]*max_len
    for index in xrange(max_len-1, -1, -1):
        binary_sum, carry = binary_add_map[(x[index], y[index], carry)]
        net_sum[index] = binary_sum
    if carry == '1':
        return '1' + ''.join(net_sum)
    return ''.join(net_sum)

if __name__ == '__main__':
    a = '1001'
    b = '10'
    a = '011111'
    b = '1'
    print binary_add(a, b)
