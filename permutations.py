'''
Time: O(n!)
Space: O(len(arr)) // In the form of stack frames.
Duplicates: allowed
Lexicographic sorted: Yes
'''
class Solution(object):
    def dfs(self, arr, cur, used, perms):
        if len(cur) == len(arr):
            perms.append(cur[:])
        else:
            for i in xrange(len(arr)):
                ''' If current index ele is already used or cur index ele is same as previous
                index ele and previous index ele is already used, skip this index. '''
                if used[i] or (i > 0 and arr[i] == arr[i-1] and used[i-1]):
                    continue
                used[i] = True
                cur.append(arr[i])
                self.dfs(arr, cur, used, perms)
                cur.pop()
                used[i] = False
        
    def permute2(self, nums):
        """
        Without using additional set as below.
        Idea: https://discuss.leetcode.com/topic/31445/really-easy-java-solution-much-easier-than-the-solutions-with-very-high-vote
        same as https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/57
        """
        perms = []
        if len(nums) == 0: return perms
        used = [False] * len(nums)
        nums.sort()
        self.dfs(nums, [], used, perms)
        return perms
        

class Solution(object):
    def generate_permutations(self, arr, start):
        if start == len(arr):
            self.permutations.append(arr[::])
        else:
            for index in xrange(start, len(arr)):
                if index > start and arr[index] == arr[index-1]:
                    continue
                arr[start], arr[index] = arr[index], arr[start]
                self.generate_permutations(arr, start+1)
                arr[start], arr[index] = arr[index], arr[start]

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permutations = []
        nums.sort()
        self.generate_permutations(nums, 0)
        '''
        This removes duplicates list solutions within generated permutations, Notice that duplicates within a list solution
        are removed by if index > start and arr[index] == arr[index-1]:
        '''
        b_set = set(map(tuple,self.permutations))
        b = map(list,b_set)
        return b


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
