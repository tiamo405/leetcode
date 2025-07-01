class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit * digit
                n //= 10
            return self.isHappy(sum)
# Example usage:
a = Solution()
print(a.isHappy(19))  # Output: True
print(a.isHappy(2))   # Output: False
print(a.isHappy(1))   # Output: True