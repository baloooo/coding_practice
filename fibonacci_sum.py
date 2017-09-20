# coding: utf-8
"""
Given a number positive number n, find value of f0 + f1 + f2 + …. + fn where fi indicates i’th Fibonacci number. Remember that f0 = 0, f1 = 1, f2 = 1, f3 = 2, f4 = 3, f5 = 5, …

Input  : n = 3
Output : 4
Explanation : 0 + 1 + 1 + 2  = 4

Input  :  n = 4
Output :  7
Explanation : 0 + 1 + 1 + 2 + 3  = 7
"""

def fib_sum_basic(n):
    # Time: O(n)
    if n <= 0:
        return 0
    fibo = [0]*(n+1)
    fibo[0] = 0
    fibo[1] = 1
    cur_sum = 0
    for index in xrange(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        cur_sum += fibo[i]
    return cur_sum

def calculate_sum(n):
    f = [0]*(n+3)
    def fib(n):
        # caclulates fibonacci number for n in log(n) time
        if n == 0:
            return 0
        if n == 1 or n == 2:
            f[n] = 1
            return 1
        if f[n]:
            return f[n]
        k = (n+1)/2 if (n & 1) else n/2
        f[n] = (fib(k)*fib(k) + fib(k-1)*fib(k-1)) if (n & 1) else ((2*fib(k-1)+fib(k))*fib(k))
        return f[n]
    return fib(n+2) - 1


def calculate_sum_orig(A, B, N):
    f = [0]*(N+3)
    def fib(N):
        # caclulates fibonacci number for n in log(n) time
        if N == 0:
            f[0] = A
            return A
        if N == 1:
            f[1] = B
            return B
        if N == 2:
            f[N] = A+B
            return f[N]
        if f[N]:
            return f[N]
        k = (N+1)/2 if (N & 1) else N/2
        f[N] = ((fib(k)*fib(k)) + (fib(k-1)*fib(k-1))) if (N & 1) else ((2*fib(k-1)+fib(k))*fib(k))
        return f[N]
    # return (fib(N+2) - B) % 1000000007
    return (fib(N-1)*A + fib(N)*B) % 1000000007

if __name__ == '__main__':
    # print calculate_sum(4)
    print calculate_sum_orig(3, 4, 5)


