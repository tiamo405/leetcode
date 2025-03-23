class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        # ©leetcode
        numContainer = n * n
        return min(numContainer, maxWeight //w)
a = Solution()
print(a.maxContainers(2,3,15))
print(a.maxContainers(3,5,20))