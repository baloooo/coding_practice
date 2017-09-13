class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        inp_arr=A
        max_so_far_starting_index = max_so_far_ending_index = max_ending_here_starting_index = max_ending_here_ending_index =  0
        max_so_far = max_ending_here = -1
        for index, ele in enumerate(inp_arr):
            if ele>=0:
                if max_ending_here !=-1:
                    max_ending_here+=ele
                    max_ending_here_ending_index+=1
                else:
                    max_ending_here=ele+1
                    max_ending_here_starting_index=max_ending_here_ending_index=index
            else:
                if max_ending_here>max_so_far:
                    max_so_far = max_ending_here
                    max_so_far_starting_index = max_ending_here_starting_index
                    max_so_far_ending_index = max_ending_here_ending_index
                elif max_ending_here == max_so_far:
                    if (max_ending_here_ending_index -
                            max_ending_here_starting_index)>(max_so_far_ending_index -
                                    max_so_far_starting_index):
                                max_so_far_starting_index = max_ending_here_starting_index
                                max_so_far_ending_index = max_ending_here_ending_index
        
                max_ending_here = -1
        if max_ending_here>max_so_far:
            max_so_far = max_ending_here
            max_so_far_starting_index = max_ending_here_starting_index
            max_so_far_ending_index = max_ending_here_ending_index
        elif max_ending_here == max_so_far:
            if (max_ending_here_ending_index -
                    max_ending_here_starting_index)>(max_so_far_ending_index -
                            max_so_far_starting_index):
                        max_so_far_starting_index = max_ending_here_starting_index
                        max_so_far_ending_index = max_ending_here_ending_index
        if max_so_far_starting_index == max_so_far_ending_index and max_so_far==-1:
            return []
        return inp_arr[max_so_far_starting_index:max_so_far_ending_index+1]

    def maxset2(self, arr):
        # Idea: Two pointer
        # http://www.geeksforgeeks.org/longest-subarray-non-negative-integers/
        max_sum = cur_sum = -1
        i = j = cur_i = cur_j = index = -1
        while index < len(arr):
            index += 1
            cur_i = cur_j = index
            cur_sum = 0
            while index < len(arr) and arr[index] >= 0:
                cur_sum += arr[index]
                cur_j += 1
                index += 1
            if cur_sum >= max_sum:
                if cur_sum == max_sum:
                    if (cur_j-cur_i)>(j-i):
                        i, j, max_sum = cur_i, cur_j, cur_sum
                else:
                    i, j, max_sum = cur_i, cur_j, cur_sum
        return arr[i:j]

if __name__ == '__main__':
    # arr = [1, 2, 5, -7, 2, 5, 7]
    # arr = [1, 2, 5, -7, 2, 5]
    arr = [0, 0, -1, 0]
    print Solution().maxset2(arr)
