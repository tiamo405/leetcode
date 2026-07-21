class Solution(object):
    def isUnique(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        return len(set(word1) & set(word2)) == 0
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_prod = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isUnique(words[i], words[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod