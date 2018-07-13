"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.

Idea: 
As I understand, the idea is that we will add left brackets whenever possible. For a right bracket, we will add it only if the remaining number of right brackets is greater than the left one. If we had used all the left and right parentheses, we will add the new combination to the result. We can be sure that there will not be any duplicate constructed string.
So to speak the basic principle here is, add left brackets whenever you can and add right whenever valid(i.e
#f opening braces >= #f closing)
"""

class Solution():
    def __init__(self):
        self.cur_paran_combination = []
        self.balanced_paran = []

   def gen_paran_latest(self, open_paran_count, close_paran_count):
	"""
        Time: O(n*catlan(n)) = O(4^n / n^(3/2))
        Space: O(n*C(2n, n)/(n+1))
        Detail analysis: https://leetcode.com/articles/generate-parentheses/

        Idea: https://discuss.leetcode.com/topic/4485/concise-recursive-c-solution/33
	open_paran_count: No. of remaining open paranthesis. '('
	close_paran_count: No. of remaining closed paranthesis. ')'
	"""
        if open_paran_count == 0 and close_paran_count == 0:
            self.parans.append(''.join(self.cur_paran))
        else:
            if open_paran_count > 0:
                self.cur_paran.append('(')
                self.gen_paran(open_paran_count-1, close_paran_count)
                self.cur_paran.pop()
            if open_paran_count < close_paran_count:
		"""
		Since a close paran will only come when there is already a open paran in place,
		which would mean the count of remaining open parans should always be less than
		closed parans so as to satisfy the condition that they are well formed parans.
		"""
                self.cur_paran.append(')')
                self.gen_paran(open_paran_count, close_paran_count-1)
                self.cur_paran.pop()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.parans = []
        self.cur_paran = []
        self.gen_paran(n,n)
        return self.parans 

    def gen_balanced_paran_simplified(self, n):
        if n<1:
            return []
        def gen_paran(left_paran_stock, right_paran_stock):
            if left_paran_stock == 0 and right_paran_stock == 0:
                self.balanced_paran.append(''.join(self.cur_paran_combination))
            if left_paran_stock != 0:
                self.cur_paran_combination.append('(')
                gen_paran(left_paran_stock-1, right_paran_stock+1)
                self.cur_paran_combination.pop()
            if right_paran_stock != 0:
                self.cur_paran_combination.append(')')
                gen_paran(left_paran_stock, right_paran_stock-1)
                self.cur_paran_combination.pop()
        gen_paran(3, 0)
        return self.balanced_paran

    def gen_balanced_paran(self, n):
        def gen_paran(left_paran_stock, right_paran_stock):
            if left_paran_stock == 0 and right_paran_stock == 0:
                # add balanced condn
                self.balanced_paran.append(''.join(self.cur_paran_combination))
                # self.cur_paran_combination.pop()
            else:
                # conditions for keeping paran balanced
                # don't make left paran if no right paran left to cover it up
                if left_paran_stock != 0 and right_paran_stock != 0:
                    self.cur_paran_combination.append('(')
                    gen_paran(left_paran_stock-1, right_paran_stock)
                    self.cur_paran_combination.pop()
                # right paran should be always greater than left param to finally cover all left param added
                if right_paran_stock != 0 and right_paran_stock > left_paran_stock:
                    self.cur_paran_combination.append(')')
                    gen_paran(left_paran_stock, right_paran_stock-1)
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
    # print sol.gen_balanced_paran_simplified(n)
