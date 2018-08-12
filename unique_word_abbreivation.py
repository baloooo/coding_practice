'''
https://leetcode.com/problems/unique-word-abbreviation/solution/
'''
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abrvtn_wset_map = collections.defaultdict(set)
        for word in dictionary:
            abrvtn = self._get_abrvtn(word)
            self.abrvtn_wset_map[abrvtn].add(word)

    def _get_abrvtn(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]     

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abrvtn = self._get_abrvtn(word)
        if abrvtn not in self.abrvtn_wset_map:
            return True
        else:
			'''
			Note: This is the hear of the problem, check if abrvtn doesn't exist or
			if it does it has only this word and no other.'''
            return True if len(self.abrvtn_wset_map[abrvtn]) == 1 and word in self.abrvtn_wset_map[abrvtn] else False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
