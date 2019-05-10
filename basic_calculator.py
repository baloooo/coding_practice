
class Solution:
    def basic_calc(self, expression):
        '''
        Basic idea:
            https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack
        Implement the version which deals with consecutive digits with a little more finesse
        '''
        expr_val = 0
        stack = []
        sign = 1
        expr_idx = 0
        while expr_idx < len(expression):
            ch = expression[expr_idx]
            if ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch.isdigit():
                num = 0
                idx = expr_idx
                num_len = 0
                while idx < len(expression) and expression[idx].isdigit():
                    num_len += 1
                    idx += 1
                while num_len > 0:
                    ch = expression[expr_idx]
                    num += (int(ch) * (10 ** (num_len - 1)))
                    num_len -= 1
                    expr_idx += 1
                expr_val += (sign * num)
                continue
            elif ch == '(':
                stack.append(expr_val)
                stack.append(sign)
                # reset vars
                sign = 1
                expr_val = 0
            elif ch == ')':
                prev_sign = stack.pop()
                prev_val = stack.pop()
                prev_val += (prev_sign * expr_val)
                expr_val = prev_val

            expr_idx += 1

        return expr_val