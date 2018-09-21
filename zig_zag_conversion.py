"""
https://leetcode.com/problems/zigzag-conversion/#/description
"""
class Solution(object):
    def convert_optimized(self, s, num_rows):
        # Idea: https://discuss.leetcode.com/topic/34573/python-o-n-solution-in-96ms-99-43/16
        zig_zag = [[] for _ in xrange(num_rows)]
        step = (num_rows == 1) - 1
        idx = 0
        for c in s:
            zig_zag[idx].append(c)
	        # Helps change direction when idx is at first or last index (only after first element has been placed)
            if idx == num_rows-1 or idx == 0:
                step = -step
            idx += step
        return ''.join([''.join(each) for each in zig_zag])

    def convert(self, given_string, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [[] for _ in range(num_rows)]
        start, index = 0, 0
        while index < len(given_string):
            # going down
            down = start
            while down < num_rows and index < len(given_string):
                arr[down].append(given_string[index])
                down += 1
                index += 1
            # going up
            up = num_rows-2 if num_rows >= 2 else 0
            while up > -1 and index < len(given_string):
                arr[up].append(given_string[index])
                up -= 1
                index += 1
            start = 1
        return ''.join([''.join(each) for each in arr])

if __name__ == '__main__':
    print Solution().convert("AB", 1)
    print Solution().convert("A", 1)
