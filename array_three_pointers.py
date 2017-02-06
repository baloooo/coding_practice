"""
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


# O(p + q + r) where p, q and r are sizes of arr1[], arr2[] and arr3[] respectively.
def min_max_diff_three_pointers(arr1, arr2, arr3):
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
