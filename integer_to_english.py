import pytest

class Solution():
    '''
    Idea is to start from LSB and keep converting last three digits to english words
    and move towards MSB.
    '''
    # Note: Where each of the lists start from.
    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def number_to_words(self, num):
        if num == 0:
            return "Zero"
        words = []
        i = 0
        # 5, 165, 725, 525
        while num > 0:
            if num % 1000 != 0: # If cur num in not a multiple of 1000
                # Convert LSB 3 digits to words + Append MSB Unit + Append everything previous LSB's
                words.append(self.helper(num % 1000) + self.THOUSANDS[i] + " ")
                # words = self.helper(num % 1000) + self.THOUSANDS[i] + " " + words
            num = num / 1000
            i += 1
        return ''.join(reversed(words)).strip()  # Notice the strip in end

    def helper(self, num):
        """
        convert num to english words where num < 1000
        """
        if num == 0:  # prevents adding rendundant spaces ex: num = 50
            return ""
        if num < 20:
            return self.LESS_THAN_20[num] + " "
        if num < 100:
            return self.TENS[num / 10] + " " + self.helper(num % 10)
        else:
            return self.LESS_THAN_20[num / 100] + " Hundred " + self.helper(num % 100)

class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        ([123], "One Hundred Twenty Three"),
        ([5165725525], "Five Billion One Hundred Sixty Five Million Seven Hundred Twenty Five Thousand Five Hundred Twenty Five"),
        ([0], "Zero"),
        ([1], "One"),
        ([1000000], "One Million"),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.number_to_words(*args) == result
