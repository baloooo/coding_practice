'''
The broad idea is to treat the conversion as converting string integer to integer or vice versa with
the difference being, we're dealing with a base 26 number rather than 10
Idea: https://discuss.leetcode.com/topic/6245/python-solution-with-explanation
'''
class Solution(object):
    '''
    Given a positive integer, return its corresponding column title as appear in an Excel sheet.

    For example:

        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB 
    '''
    #  https://discuss.leetcode.com/topic/6245/python-solution-with-explanation
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = list(string.uppercase)
        res = []
        while n > 0:
            res.append(capitals[(n-1)%26])
            n = (n-1) /26
        res.reverse()
        return ''.join(res)

    def column_title_to_number(title):
        """
        Given a column title as appears in an Excel sheet, return its corresponding column number.
        Example:

            A -> 1
            
            B -> 2
            
            C -> 3
            
            ...
            
            Z -> 26
            
            AA -> 27
            
            AB -> 28 
        """
        res = 0
        for ch in title:
            '''
            As everytime you go one place more you have covered order of 26 items
            like from AA to AAA you would go AA -> AZ, and then to BA -> BZ ... untill ZA ->ZZ and then AAA
            Also the logic is similar to converting a string number to integer, the only difference is
            in integers with one unit place number are increased by an order of 10 instead of 26 as in
            this case for alphabets.
            '''
            res = res * 26  
            res = res + ord(ch) - ord('A') + 1
        return res
