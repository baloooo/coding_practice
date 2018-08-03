'''You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
'''
class Solution(object):
    def generatePossibleNextMoves(self, s): """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 1:
            return []
        moves = []
        for i in xrange(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                moves.append(s[:i-1] + '--' + s[i+1:])

        return moves

if __name__ == '__main__':
    print Solution().generatePossibleNextMoves('--++')

'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:S

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.
'''


class Solution(object):
    def _can_I_win(self, s, cache):
		'''
		Same logic with caching, gets 5x speed up
		'''
        for i in xrange(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                s[i], s[i-1] = '-', '-'
                cur_board = ''.join(s)
                if cur_board in cache:
                    other_player_wins = cache[cur_board]
                else:
                    other_player_wins = self._can_I_win(s) # Is next player able to win after cur move from me, if not I WIN.
                    cache[cur_board] = other_player_wins

                s[i], s[i-1] = '+', '+' # revert back changes for this iteration, Note: this is imp. since we want slate cleared before returning so as to give chance for trying all combinations above.

                if not other_player_wins:
                    return True

        return False # I was not able to win.

    def _can_I_win(self, s):
        for i in xrange(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                s[i], s[i-1] = '-', '-'

                other_player_wins = self._can_I_win(s) # Is next player able to win after cur move from me, if not I WIN.

                s[i], s[i-1] = '+', '+' # revert back changes for this iteration, Note: this is imp. since we want slate cleared before returning so as to give chance for trying all combinations above.

                if not other_player_wins:
                    return True

        return False # I was not able to win.

                

    def canWin2(self, s):
        """
        :type s: str
        :rtype: bool
        Time: Suppose originally the board of size N contains only '+' signs, then roughly we have:

        T(N) = (N-2) * T(N-2) = (N-2) * (N-4) * T(N-4) ... = (N-2) * (N-4) * (N-6) * ... ~ O(N!!)
        https://en.wikipedia.org/wiki/Double_factorial
        """
        if len(s) <= 1:
            return False
        # return self._can_I_win(list(s), {}) 
        return self._can_I_win(list(s)) 


if __name__ == '__main__':
    print Solution().canWin('++++')
