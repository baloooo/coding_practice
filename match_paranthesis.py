"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""
def match_paranthesis(paran_sequence):
    paran_map = {'}': '{', ']':'[' , ')': '('}
    paran_stack = []
    for paran in paran_sequence:
        if paran in ['{', '[', '(']:
            paran_stack.append(paran)
        else:
            matching_paran = paran_stack.pop()
            if matching_paran != paran_map[paran]:
                return 0
    if not paran_stack:
        return 1
    else:
        return 0

if __name__ == '__main__':
    paran_sequence = '{{{[{}}}}'
    paran_sequence = '{([])}'
    print match_paranthesis(paran_sequence)
