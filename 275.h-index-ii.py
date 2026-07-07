class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = 0 
        r = len(citations) - 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= len(citations) - mid:
                res = len(citations) - mid
                r = mid - 1
            else:
                l = mid + 1
        return res
a = Solution()
print(a.hIndex([0, 1, 3, 5, 6]))  # Output: 3
print(a.hIndex([1, 2, 1000]))  # Output: 2