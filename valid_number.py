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
        """
        states = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
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
        if cur_state not in [3, 5, 8, 9]:
            print 'cur_state finally is', cur_state
            return False
        return True
