class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
	Idea: https://discuss.leetcode.com/topic/36160/python-o-n-1-pass-in-place-solution-with-explanation/5
        """
        red = white = 0
        blue = len(arr)-1
        while white <= blue:
            if arr[white] == 0:
                arr[white], arr[red] = arr[red], arr[white]
                white += 1
                red += 1
            elif arr[white] == 1:
                white += 1
            else:
                arr[white], arr[blue] = arr[blue], arr[white]
                blue -= 1
