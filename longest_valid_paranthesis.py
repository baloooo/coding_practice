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
    def longest_valid_paranthesis_optimized(self, inp_str):
        # Time: O(n)
        # Space: O(1)
        pass

    """
    Algo:
    1) Create an empty stack and push -1 to it. The first element
       of stack is used to provide base for next valid string.

    2) Initialize result as 0.

    3) If the character is '(' i.e. str[i] == '('), push index
       'i' to the stack.
    2) Else (if the character is ')')
       a) Pop an item from stack (Most of the time an opening bracket)
       b) If stack is not empty, then find length of current valid
          substring by taking difference between current index and
          top of the stack. If current length is more than result,
          then update the result.
       c) If stack is empty, push current index as base for next
          valid substring.

    3) Return result.
    """
    def longest_valid_paranthesis(self, inp_str):
        # Time: O(n)
        # Space: O(n)
        longest, last, stack = 0, -1, []
        for index, char in enumerate(inp_str):
            if char == '(':
                stack.append(index)
            elif not stack:
                last = index
            else:
                stack.pop()
                if stack:
                    longest = max(longest, index-stack[-1])
                else:
                    longest = max(longest, index-last)
        return longest


if __name__ == '__main__':
    test_cases = [
        ("()", 2),
        (")()())", 4),
        ("()((()()))())()((()))", 12),
        ("(", 0),
        ("(()", 2),
        ("((((((", 0),
        ("))))))", 0),
        ("()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))(((", 30),  # noqa
        (")()))(())((())))))())()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))(((", 30),    # noqa
        ("()()()(((()()()()", 8),
        ("((()))", 6),
    ]
    for test_case in test_cases:
        res = Solution().longest_valid_paranthesis(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Expected: {1} but got {2}".format(test_case[0], test_case[1], res)  # noqa
