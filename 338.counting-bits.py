class Solution(object):
    def countBit(self, num):
        count = 0
        while num:
            count += num % 2
            num //= 2
        return count

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            result.append(self.countBit(i))
        return result
        