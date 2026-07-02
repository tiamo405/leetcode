class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        nmax = max(citations)
        n = len(citations)
        count = [0] * (nmax + 1)
        for c in citations:
            for i in range(c + 1):
                count[i] += 1
        for i in range(nmax, -1, -1):
            if count[i] >= i:
                return i

a = Solution()
citations = [3, 0, 6, 1, 5]
print(a.hIndex(citations))  # Output: 3