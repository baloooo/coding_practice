def permutations_recursive(arr):
    permutations = []
    def permute(arr, start, end):
        if start == end:
            permutations.append(arr[::])
            return
        for index in xrange(start, len(arr)):
            arr[start], arr[index] = arr[index], arr[start]
            permute(arr, start+1, end)
            arr[start], arr[index] = arr[index], arr[start]
    permute(arr, 0, len(arr)-1)
    return permutations


if __name__ == '__main__':
    arr = ['A', 'B', 'C', 'D']
    for each in  permutations_recursive(arr):
        print each
