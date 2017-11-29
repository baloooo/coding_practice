"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one
"""

class Solution(object):
    def isNumber(self, s):
        """
        Idea: https://discuss.leetcode.com/topic/30058/a-simple-solution-in-python-based-on-dfa/26?page=1
              https://en.wikipedia.org/wiki/Scientific_notation#E-notation
        Key points: Space/blank is the initial state.
        """
        # Indexes of the array states are treated as state numbers.
        states = [{}, 
              # State (1) - initial state (scan ahead thru blanks)
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              # State (2) - found sign (expect digit/dot)
              {'digit':3, '.':4},
              # State (3) - digit consumer (loop until non-digit)
              {'digit':3, '.':5, 'e':6, 'blank':9},
              # State (4) - found dot (only a digit is valid)
              {'digit':5},
              # State (5) - after dot (expect digits, e, or end of valid input)
              {'digit':5, 'e':6, 'blank':9},
              # State (6) - found 'e' (only a sign or digit valid)
              {'sign':7, 'digit':8},
              # State (7) - sign after 'e' (only digit)
              {'digit':8},
              # State (8) - digit after 'e' (expect digits or end of valid input) 
              {'digit':8, 'blank':9},
              # State (9) - Terminal state (fail if non-blank found)
              {'blank':9}]
        cur_state = 1
        for c in s:
            if c in '0123456789':
                c = 'digit'
            elif c in '+-':
                c = 'sign'
            elif c in ' \t\n':
                c = 'blank'
            if c not in states[cur_state]:
                print 'Intermediate cur_state is', c
                return False
            cur_state = states[cur_state][c]
        # The only valid terminal states are ending on digit, digit after dot, digit after e, or white space after valid input
        if cur_state not in [3, 5, 8, 9]:
            print 'cur_state finally is', cur_state
            return False
        return True
