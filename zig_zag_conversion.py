"""
https://leetcode.com/problems/zigzag-conversion/#/description
"""
class Solution(object):
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
