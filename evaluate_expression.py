# -*- coding: utf-8 -*-
"""
Evaluate Expression
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another
expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


def evaluate(expression):
    result_stack = []
    def mul(operand1, operand2):
        return operand1*operand2
    def add(operand1, operand2):
        return operand1+operand2
    def sub(operand1, operand2):
        return operand2-operand1
    def div(operand1, operand2):
        return operand2/operand1
    operator_map = {'*': mul, '+': add, '-': sub, '/': div}
    for op in expression:
        if op not in ['+', '-', '*', '/']:
            result_stack.append(int(op))
        else:
            ele1 = result_stack.pop()
            ele2 = result_stack.pop()
            res = operator_map[op](ele1, ele2)
            result_stack.append(res)
    return result_stack[0]

if __name__ == '__main__':
    expression = ["2", "1", "+", "3", "*"]
    expression = ["4", "13", "5", "/", "+"]
    expression = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    print evaluate(expression)
