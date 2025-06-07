class Solution(object):
    def tach_nguyen_to(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n < 2:
            return 0
        count = 0
        for i in range(2, n + 1):
            while i % k == 0:
                count += 1
                i //= k
        return count

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dem_5 = self.tach_nguyen_to(n, 5)
        dem_2 = self.tach_nguyen_to(n, 2)
        # The number of trailing zeroes is determined by the limiting factor
        return min(dem_5, dem_2)
a = Solution()
print(a.trailingZeroes(5))  # Output: 1
print(a.trailingZeroes(0)) 