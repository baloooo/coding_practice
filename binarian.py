# coding: utf-8
"""
A non-empty zero-indexed array A consisting of N non-negative integers is given
Its binarian is defined as:
binarian(A) =   pow2(A[0]) + pow2(A[1]) + ... + pow2(A[N−1])
pow2(K) =   2K
For example, the binarian of array A such that:
  A[0] = 1
  A[1] = 5
  A[2] = 4
equals 50:
binarian(A) =   pow2(A[0]) + pow2(A[1]) + pow2(A[2])
    =   pow2(1) + pow2(5) + pow2(4)
    =   2 + 32 + 16
    =   50
Write a function:
def solution(A)
that, given an array A consisting of N non-negative integers, returns the
length of the shortest array that has the same binarian as array A.
For example, given array A such that:
  A[0] = 1
  A[1] = 0
  A[2] = 2
  A[3] = 0
  A[4] = 0
  A[5] = 2
the function should return 3 because:
the binarian of A is 13,
array B such that B[0] = 3, B[1] = 2 and B[2] = 0 also has a binarian of 13,
there is no shorter array with a binarian of 13.
Assume that:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..10,000].
Complexity:
expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N), beyond input
storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

"""

def binarian(arr):
    # Overall time: O(N) and Overall Space: O(N)
    count_arr = [0]*100001
    # Time: O(N)
    for ele in arr:
        count_arr[ele] += 1
    # Time: O(len(count_arr))
    for index in xrange(len(count_arr)):
        while count_arr[index] > 1:
            count_arr[index] -= 2
            count_arr[index+1] += 1
    resultant_count = 0
    # Time: O(len(count_arr))
    for cur_count in count_arr:
        resultant_count += cur_count
    return resultant_count
    

def binarian_wrong(arr):
    from math import log
    final_arr = []
    res = 1
    for num in arr:
        res += pow(2, num)
    while(res != 0):
        unit = int(log(res, 2))
        final_arr.append(unit)
        res -= pow(2, unit)
    return final_arr

if __name__ == '__main__':
    arr = [1, 0, 2, 0, 0, 2]
    arr = [1, 5, 4]
    arr = [10000, 1000, 1243, 353, 2533, 546, 235, 532, 235, 666, 666, 23, 26, 233, 2323, 23, 23]
    # arr = [0, 0, 0, 0, 1] # 2
    # arr = [0]
    # arr = []
    # arr = [1, 1, 1, 1]
    arr = [0, 10000]
    arr = [10000, 10000]

    print binarian(arr)
