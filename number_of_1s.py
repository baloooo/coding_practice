def hamming_weight(n):
    # https://leetcode.com/articles/number-1-bits/
    count = 0
    while n != 0:
        count += 1
        n = n & (n - 1)
    return count

def number_of_1s(num):
    count = 0
    while(num):
        if num % 2 != 0:
            count += 1
        num = num/2
    print count


def hamming_weight(num):
    # the reason above code works is here
    # https://discuss.leetcode.com/topic/11385/simple-java-solution-bit-shifting
    ones = 0
    while num:
        ones += (num & 1)
        num = num >> 1
    return ones

if __name__ == '__main__':
    number_of_1s(162545345)
    print hamming_weight(162545345)
