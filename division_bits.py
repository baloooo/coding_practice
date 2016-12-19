def divide(dividend, divisor):
    quotient = 0
    negative = False
    if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
        negative = True
    if divisor == 0:
        return sys.maxint
    elif abs(divisor) == 1:
        import ipdb; ipdb.set_trace()
        if negative:
            return -dividend
        return dividend
    while(dividend>=divisor):
        dividend-=divisor
        quotient+=1
    return quotient

if __name__ == '__main__':
    print divide(-1, 1)
    print divide(2147483647, 1)
