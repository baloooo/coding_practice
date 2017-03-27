"""
Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()",
which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is
"()()", which has length = 4.
"""


# Time: O(n)
# Space: O(n) (in the form of stack)
class Solution:
    def __init__(self):
        self.max_valid_paran_len = 0

    def longest_valid_paranthesis(self, inp_str):
        stack = []
        last_succesfull_start = last_succesfull_end = 0
        for cur_index, char in enumerate(inp_str):
            cur_max_len = 0
            if char == ')':
                if not stack or stack[-1][0] == ')':
                    stack = []
                    last_succesfull_start = last_succesfull_end = 0
                else:  # stack[-1] is '(':
                    cur_opening_paran = stack.pop()[1]
                    if last_succesfull_end == 0:
                        last_succesfull_start = cur_opening_paran
                        last_succesfull_end = cur_index
                        cur_max_len = cur_index - cur_opening_paran + 1
                    elif cur_opening_paran == last_succesfull_end+1:
                        last_succesfull_end = cur_index
                        cur_max_len = cur_index - last_succesfull_start + 1
                    else:
                        cur_max_len = cur_index - cur_opening_paran + 1
                    self.max_valid_paran_len = max(
                        self.max_valid_paran_len, cur_max_len)
            else:
                stack.append((char, cur_index))
        return self.max_valid_paran_len


if __name__ == '__main__':
    inp_str, res = "()", 1
    inp_str, res = ")()())", 4
    inp_str, res = "()((()()))())()((()))", 12
    inp_str, res = "(", 0
    inp_str, res = "(()", 2
    inp_str, res = "((((((", 0
    inp_str, res = "))))))", 0
    inp_str, res = "()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))(((", 30
    inp_str, res = ")()))(())((())))))())()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))(((", 30
    inp_str, res = "()()()(((()()()()", 8
    # inp_str, res = "((()))", 6
    print Solution().longest_valid_paranthesis(inp_str)
