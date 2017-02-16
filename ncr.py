class Solution():
    def __init__(self):
        self.total_combinations = []
        self.cur_selection = []
    def combinations(self, n, k):
        def possible_combinations(i, n, k):
            if k == 0:
                self.total_combinations.append(self.cur_selection[::])
            else:
                for index in xrange(i, n-k+2):
                    self.cur_selection.append(index)
                    possible_combinations(index+1, n, k-1)
            try:
                self.cur_selection.pop()
            except IndexError:
                pass
        if k == 0 or n == 0:
            return 1
        possible_combinations(1, n, k)
        return self.total_combinations


if __name__ == '__main__':
    n, k = 5, 3
    n, k = 4, 2
    n, k = 0, 2
    n, k = 4, 0
    sol = Solution()
    print sol.combinations(n, k)
