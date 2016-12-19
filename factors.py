from math import sqrt


def calc_factors(A):
    small_factors = [1]
    large_factors = []
    for num in xrange(2, int(sqrt(A))+1):
        if A % num == 0:
            small_factors.append(num)
            large_factors.append(A/num)
    large_factors = large_factors[::-1]
    large_factors.append(A)
    return small_factors+large_factors

if __name__ == '__main__':
    print calc_factors(82944)
