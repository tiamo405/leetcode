class Solution(object):
    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # b1: dem so -1, 1, neu ca 2 deu chan thi lay cai min, or cai chi 1 chia het cho 2
        count_neg = 0
        count_pos = 0
        so_can_bien_doi = 0
        for num in nums:
            if num < 0:
                count_neg += 1
            elif num > 0:
                count_pos += 1
        if count_neg % 2 == 0 and count_pos % 2 == 0:
            so_can_bien_doi = min(count_neg, count_pos)
        elif count_neg % 2 == 1 and count_pos % 2 == 1:
            return False
        else:
            so_can_bien_doi = min(count_neg, count_pos)
        # b2: neu so_can_bien_doi <= k thi tra ve True
        return so_can_bien_doi <= k
# Example usage:
a = Solution()
print(a.canMakeEqual([1,-1,1,-1,1], 3))  # Output: True
print(a.canMakeEqual([-1,-1,-1,1,1,1], 5))  # Output: False
print(a.canMakeEqual([-1,1,1,1,-1,-1,-1,1,1],))  # Output: False