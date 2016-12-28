"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 
"""
def remove_duplicates(arr):
    n = len(arr)
    i = 0
    j = i + 1
    end = n - 1
    while(j<=end):
        if arr[i] == arr[j]:
            index = temp_index = i+1
            count=0
            while(index<=end):
                if arr[i] == arr[index]:
                    index+=1
                    count+=1
                    continue
                arr[temp_index] = arr[index]
                index+=1
                temp_index+=1
            end -= count
        i += 1
        j += 1
    return len(arr[:end+1])

if __name__ == '__main__':
    # arr = [1,1]
    # arr = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8]
    # arr = [1, 1, 2, 3]
    # arr = [1]
    # arr = [1, 2, 3]
    arr = [0]
    print remove_duplicates(arr)
