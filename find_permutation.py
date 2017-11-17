'''
Solution article: https://leetcode.com/articles/find-permutation/
Idea is to start from sorted array and then manage D in consecutive groups as they're encountered
since arr is sorted I's will take care of themselves.
To generate the required arrangement, we can start off with the minmin number that can be formed for the given nn. Then, to satisfy the given pattern ss, we need to reverse only those subsections of the minmin array which have a D in the pattern at their corresponding positions.
'''

def sol_stack(pattern):
    # Time: O(n) Space: O(n)
    arr = range(1, len(pattern)+2)
    stack, j, res = [], 0, []
    for i, s in enumerate(pattern):
        stack.append(arr[i])
        if s == 'I':
            while (stack):
                res.append(stack.pop())
    stack.append(arr[-1])
    while stack:
        res.append(stack.pop())
    return res


def reverse(arr, i, j):
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def sol_rev(pattern):
    # Time: O(n) Space: O(1)
    arr = range(1, len(pattern)+2)
    i = j = 0
    while j < len(pattern):
        i = j
        while j < len(pattern) and pattern[j] == 'D':
            j += 1
        reverse(arr, i, j)
        j += 1
    return arr

if __name__ == '__main__':
    pattern = 'DDIIIID'
    print sol_stack(pattern)
    print sol_rev(pattern)
