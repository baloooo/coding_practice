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
def zero_one_multiple_optimized(multiplicand):
        from Queue import Queue
        bfs_q = Queue()
        bfs_q.put((1, '1'))
        visited_remainders = set()
        while not bfs_q.empty():
            cur_remainder, cur_num = bfs_q.get()
            left_child = cur_remainder * 10
            right_child = left_child + 1 
            l_mod = left_child % multiplicand 
            r_mod = l_mod + 1 
            if l_mod == 0:
                return str(cur_num)+'0'
            if r_mod == multiplicand:
                return str(cur_num)+'1'
            if l_mod not in visited_remainders:
                visited_remainders.add(l_mod)
                bfs_q.put((l_mod, cur_num+'0'))
            if r_mod not in visited_remainders:
                visited_remainders.add(r_mod)
                bfs_q.put((r_mod, cur_num+'1'))

n = int(raw_input())
for _ in xrange(n):
    m = int(raw_input())
    print zero_one_multiple_optimized(m)

#     print Solution().zero_one_multiple(3456)  # 11011111110000000
# if __name__ == '__main__':
#     # print Solution().zero_one_multiple(479)  # 100111
#     print Solution().zero_one_multiple(3456)  # 11011111110000000
#     # print Solution().zero_one_multiple(325)  # 100100
