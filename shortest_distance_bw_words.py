class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = idx2 = None
        min_diff = float('inf')
        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
            if word == word2:
                idx2 = idx

            if idx1 is not None and idx2 is not None:
                min_diff = min(min_diff, abs(idx1-idx2))

        return min_diff

########################################################################################################################

class WordDistance2(object):
	'''
	Cache the result in the event the same pairs are queried again
	Bail out immediately once you find that the min diff is 1 since you can never do better than that
	'''
    def __init__(self, words):
        """
        :type words: List[str]
        """
        # {word: set of indexes where this word was seen}
        self.word_map = collections.defaultdict(list)

        # since the items in list will be sorted(as we traverse from 0 to len(words)) we can do merge sort later for indexes
        for idx, word in enumerate(words):
            self.word_map[word].append(idx)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1_list = self.word_map[word1]
        index2_list = self.word_map[word2]

        idx1 = idx2 = 0
        shortest_distance = float('inf')
        while idx1 < len(index1_list) and idx2 < len(index2_list):
            shortest_distance = min(shortest_distance, abs(index1_list[idx1] - index2_list[idx2]))
            if index1_list[idx1] < index2_list[idx2]:
                idx1 += 1
            elif index1_list[idx1] > index2_list[idx2]:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
                
        return shortest_distance

########################################################################################################################

https://leetcode.com/problems/shortest-word-distance-iii/discuss/67097/12-16-lines-Java-C++
