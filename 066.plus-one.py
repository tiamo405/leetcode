class Solution(object):
    def plusOne( self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sodu = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                sodu = 1
            else:
                digits[i] += 1
                sodu = 0
                break
        if sodu == 1:
            digits.insert(0, 1)
        return digits
a = Solution()
print(a.plusOne([9])) 