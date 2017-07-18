# http://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        """
        Since  "max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized"
        in a long way of saying find the 3 elements that are closest to each other, so 
        as we know 3 elements or any number of elements in general are as close to each
        other as the maximum of those element and minimum of those elements are apart,
        because they are the ones that decide the maximum difference and hence the fact
        that how close they as a group will be
        (similar to the fact that the strength of the entire chain depends on their weakest link)
        """
        i = j = k = 0
        min_so_far = float('inf')
        while i < len(A) and j < len(B) and k < len(C):
            cur_min = min(A[i], B[j], C[k])
            cur_max = max(A[i], B[j], C[k])
            cur_min_diff = cur_max - cur_min
            if cur_min_diff < min_so_far:
                min_so_far = cur_min_diff
            if min_so_far == 0:
                break
            if cur_min == A[i]:
                i += 1
            elif cur_min == B[j]:
                j += 1
            else:
                k += 1
        return min_so_far


class Solution:
    def b_s(self, arr, target):
        """
        finds closest ele <= target
        """
        low = 0
        high = len(arr)-1
        while low < high:
            mid = low + (high-low)/2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return arr[mid]
        return arr[low]
        
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        min_so_far = float('inf')
        for ele in A:
            x = self.b_s(B, ele)
            y = self.b_s(C, ele)
            min_so_far = min(min_so_far, max(ele-x, x-y, y-ele))
        for ele in B:
            x = self.b_s(A, ele)
            y = self.b_s(C, ele)
            min_so_far = min(min_so_far, max(ele-x, x-y, y-ele))
        for ele in C:
            x = self.b_s(A, ele)
            y = self.b_s(B, ele)
            min_so_far = min(min_so_far, max(ele-x, x-y, y-ele))
        return min_so_far
if __name__ == '__main__':
    A = [1, 4, 10]
    B = [2, 15, 20]
    C = [10, 12]
    A = [1]
    B = [1]
    C = [1]
    print Solution().minimize(A, B, C)
