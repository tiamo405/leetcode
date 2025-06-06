class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i in range(len(columnTitle)):
            res = res * 26 + (ord(columnTitle[i]) - ord('A') + 1)
        return res
