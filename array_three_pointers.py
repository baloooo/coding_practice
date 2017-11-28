"""
Find three closest elements from three arrays.
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5
         With 10 from A, 15 from B and 10 from C.
"""


'''
check
http://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
for bruteforce and nlogn solutions.
A Simple Solution is to run three nested loops to consider all triplets from A, B and C. Compute the value of max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) for every triplet and return minimum of all values. Time complexity of this solution is O(n3)
'''
def min_max_diff_three_pointers(arr1, arr2, arr3):
    '''
    O(p + q + r) where p, q and r are sizes of arr1[], arr2[] and arr3[] respectively.
    The correctness argument goes something like this. Let's say the heads of X, Y, and Z are 10, 5, and 20, so that y=5 is the min. Consider all tuples (x, 5, z). Since X is sorted we know that x >= 10 for all x, and likewise all z >= 20. So now we know any solution involving y=5 has the form (x >= 10, 5, z >= 20). Since y=5 is less than 10 and 20, we clearly know the optimal solution for that form has to be (10, 5, 20), which we just evaluated. Therefore, since we have proven that we've already considered the optimal solution for y=5, we can advance the Y pointer beyond y=5 to find more optimal solutions over (X, Y, Z). It's also pretty easy to convince ourselves that the algorithm terminates in linear time, since we always exclude one element from one of the lists. (To be precise, it's O(Nm) time, where m=3, but we can treat as m as a constant in the current formulation.)

Even though it's pretty easy to prove the correctness of the algorithm, there is still risk in messing up the implementation. Fortunately, this problem has a trivial O(N^3) solution as well, so you can use your slow implementation to validate the fast implementation for a bunch of randomly generated small lists. This won't conclusively prove that the faster algorithm works, but it can help identify bugs in the implementation
    '''
    i, j, k = 0, 0, 0
    min_till_now = float('inf')
    while(i < len(arr1) and j < len(arr2) and k < len(arr3)):
        cur_min = min(arr1[i], arr2[j], arr3[k])
        cur_max = max(arr1[i], arr2[j], arr3[k])
        cur_diff = cur_max - cur_min
        if cur_diff < min_till_now:
            min_till_now = cur_diff
        if cur_min == arr1[i]:
            i += 1
        elif cur_min == arr2[j]:
            j += 1
        else:
            k += 1
    return min_till_now


if __name__ == '__main__':
    a = [1, 4, 10]
    b = [2, 15, 20]
    c = [10, 12]
    print min_max_diff_three_pointers(a, b, c)
