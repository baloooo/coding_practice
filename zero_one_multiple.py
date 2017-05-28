"""
PS: Smallest Multiple With 0 and 1
You are given an integer N. You have to find smallest multiple of N which
consists of digits 0 and 1 only. Since this multiple could be large, return
it in form of a string.

Note:
- Returned string should not contain leading zeroes.

For example,

For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.

Algo:
"""


class Solution:
    def __init__(self):
        pass

    def zero_one_multiple_optimized(self, multiplicand):
        # Time: O(m) where m is the number of mod states for multiplicand
        # which is multiplicand itself. 0 to multiplicand - 1.
        # Space: O(m) for storing multiplicands(visited_remainders)
        # Check @Tuxdude solution only
        # https://stackoverflow.com/questions/28268786/how-to-solve-zero-one-multiple-coding-solution
        from Queue import Queue
        bfs_q = Queue()
        bfs_q.put(1)
        visited_remainders = set()
        # possible optimization is to use remainders instead of the numbers themselves.
        # Thereby storing l_mod instead of left_child in bfs_q, only catch is that
        # now you have to store original number or atleast part of it to reconstruct the
        # original number. Can check spoj_zero_one.py for this attempt
        while not bfs_q.empty():
            cur_num = bfs_q.get()
            left_child = cur_num * 10
            right_child = left_child + 1
            l_mod = left_child % multiplicand 
            r_mod = l_mod + 1
            if l_mod == 0:
                return left_child
            if r_mod == multiplicand:
                return right_child
            if l_mod not in visited_remainders:
                visited_remainders.add(l_mod)
                bfs_q.put(left_child)
            if r_mod not in visited_remainders:
                visited_remainders.add(r_mod)
                bfs_q.put(right_child)

    def all_zero_one(self, result):
        for digit in result:
            if digit not in ['0', '1']:
                return False
        return True

    def zero_one_multiple(self, multiplicand):
        multiplier_list = ['']
        iteration_index = 1
        while multiplier_list:
            new_multiplier_list = []
            for num in multiplier_list:
                for unit_place in xrange(10):
                    new_multiplier_list.append(
                        str(unit_place) + str(num))
            multiplier_list = new_multiplier_list
            new_multiplier_list = []
            for multiplier in multiplier_list:
                result = str(int(multiplier) * multiplicand)
                if not int(result):
                    continue
                if self.all_zero_one(result):
                    return result
                if result[-iteration_index] in ['0', '1']:
                    new_multiplier_list.append(multiplier)
            multiplier_list = new_multiplier_list
            iteration_index += 1


if __name__ == '__main__':
    # print Solution().zero_one_multiple(479)  # 100111
    # print Solution().zero_one_multiple(3456)  # 11011111110000000
    print Solution().zero_one_multiple_optimized(3456)  # 11011111110000000
    # print Solution().zero_one_multiple(325)  # 100100
