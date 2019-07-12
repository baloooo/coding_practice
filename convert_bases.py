def convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.
    ''''
    Idea: convert from source to decimal, and then decimal to target, instead of trying to convert directly from source to target.
    # Time complexity: 2*(logn)base2
    # DAA: 13 10 10
    # (16**0)*10 + (16 ** 1) * 10 + (16 ** 2) * 13
    (102)3 =
    2 + 0 + 9
    11
    (11111111111)1.
    '''
    # convert from b1 to decimal
    if not num_as_string:
        return 0
    sign = False
    if num_as_string[0] == '-':
        sign = True
        num_as_string = num_as_string[1:]
    num_in_decimal = 0
    char_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if b1 != 10:
        multiplier = len(num_as_string) - 1
        for ch in num_as_string:
            num_in_decimal += (char_to_decimal[ch] * (b1 ** multiplier))
            multiplier -= 1
    else:
        num_in_decimal = int(num_as_string)
    # convert from decimal to b2
    target_num = []
    encoding_map = list(range(10)) + ['A', 'B', 'C', 'D', 'E', 'F']

    while num_in_decimal > 0:
        quot, rem = divmod(num_in_decimal, b2)
        target_num.append(str(encoding_map[rem]))
        num_in_decimal = quot

    if not target_num:
        target_num = ['0']
    return ''.join(reversed(target_num)) if not sign else '-' + ''.join(reversed(target_num))