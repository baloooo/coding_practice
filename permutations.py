"""
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
 NOTE
 No two entries in the permutation sequence should be the same.
 For the purpose of this problem, assume that all the numbers in the collection
 are unique.
"""


# Time: O(n!)
# Space: O(len(arr)) // In the form of stack frames.
# Duplicates: Aallowed
# Lexicographic sorted: Yes
def permute_recursive_optimized(arr):
    pass


# Time: O(n*n!) (For each n! permutations we'll be copying arr of size n)
# Space: O(len(arr)) // In the form of stack frames.
# Duplicates: Not allowed
# Lexicographic sorted: Yes
def permute_recursive_best_naive(arr):
    permutations = []

    def permute(arr, low, high):
        if low == high:
            permutations.append(arr[::])
        else:
            for index in xrange(low, high):
                arr[low], arr[index] = arr[index], arr[low]
                permute(arr, low+1, high)
                arr[index], arr[low] = arr[low], arr[index]
    permute(arr, 0, len(arr))
    return permutations

# Time: O(n*n!)
# Space: O(1)
# Duplicates: Not allowed
# Lexicographic sorted: No


def permute_recursive_heap_naive(arr):
    # heap as in inventor heap
    permutations = []

    def permute(arr, cur_size, n):
        if cur_size == 1:
            permutations.append(arr[::])
        for index in xrange(cur_size):
            permute(arr, cur_size-1, n)
            # if cur_size is even
            if cur_size % 2 == 0:
                arr[0], arr[cur_size-1] = arr[cur_size-1], arr[0]
            else:
                arr[index], arr[cur_size-1] = arr[cur_size-1], arr[index]
    permute(arr, len(arr), len(arr))
    print len(permutations)
    return permutations

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    for x in permute_recursive_best_naive(arr):
        print x
    # for x in permute_recursive_heap_naive(arr):
    #     print x
