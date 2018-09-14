"""
Remove Element

Given an array and a value, remove all the instances of that value in the array. 
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

 Example:
 If array A is [4, 1, 1, 2, 1, 3]
 and value elem is 1, 
 then new length is 3, and A is now [4, 2, 3] 
 Try to do it in less than linear additional space complexity.
"""
def remove_ele(arr, x):
    last = len(arr) - 1
    start = 0
    while(start<=last):
        if arr[start] == x:
            # get the first occurrence of x from tail of arr.
            while (arr[last] == x and last>start):
                last -= 1
            if start == last:
                return start
            arr[start], arr[last] = arr[last], arr[start]
        start+=1
    return start

def remove_ele_leet(A, elem):
    i, last = 0, len(A) - 1
    while i <= last:
	if A[i] == elem:
	    A[i], A[last] = A[last], A[i]
	    last -= 1
	else:
	    i += 1
    return last + 1

if __name__ == '__main__':
    # arr = [4, 1, 1, 2, 1, 3]
    # arr = [1, 1, 1, 1]
    # arr = [1, 1]
    # arr = [1]
    # arr = [1, 2, 3]
    # arr = [1, 2]
    # arr = []
    # arr = [4]
    # arr = [4,5]
    # arr = [4, 5, 6]
    # print remove_ele(arr, 1)
    print remove_ele_leet(arr, 1)
    print arr
