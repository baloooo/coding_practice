"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
"""

class Solution():
    def __init__(self):
        self.cur_paran_combination = []
        self.balanced_paran = []

    def gen_balanced_paran(self, n):
        def gen_paran(left_paran, right_paran):
            if left_paran == 0 and right_paran == 0:
                # add balanced condn
                self.balanced_paran.append(''.join(self.cur_paran_combination))
                # self.cur_paran_combination.pop()
            else:
                # conditions for keeping paran balanced
                # don't make left paran if no right paran left to cover it up
                if left_paran != 0 and right_paran != 0:
                    self.cur_paran_combination.append('(')
                    gen_paran(left_paran-1, right_paran)
                    self.cur_paran_combination.pop()
                # right paran should be always greater than left param to finally cover all left param added
                if right_paran != 0 and right_paran > left_paran:
                    self.cur_paran_combination.append(')')
                    gen_paran(left_paran, right_paran-1)
                    self.cur_paran_combination.pop()
        if n < 1:
            return []
        # since first paran cannot be closing paran to be balanced paran combination
        self.cur_paran_combination.append('(')
        gen_paran(n-1, n)
        return self.balanced_paran

if __name__ == '__main__':
    sol = Solution()
    n = 0
    n = 3
    print sol.gen_balanced_paran(n)
