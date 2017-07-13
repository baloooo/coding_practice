class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, arr, target):
        start = 0 
        end = len(arr)-1
        while start <= end:
          mid = start + (end-start)/2
          if arr[mid] == target:
              return mid
          if target < arr[start]:
              return start
          elif target > arr[end]:
              return end + 1
          if arr[mid] > target:
              end = mid - 1 
          else:
              start = mid + 1 
        return start

if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3, 4, 5], 4), 3),
        # ((range(200), 152), 149),
        res = Solution().searchInsert(test_case[0][0], test_case[0][1])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
