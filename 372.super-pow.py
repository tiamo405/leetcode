class Solution(object):
    MOD = 1337
    def getPow(self, a, k):
        if k == 0:
            return 1
        a %= self.MOD
        if k % 2 == 1:
            return (a * self.getPow(a, k - 1)) % self.MOD
        half = self.getPow(a, k // 2)
        return (half * half) % self.MOD
    
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = a % self.MOD
        result = 1
        for i in range(len(b)):
            result = (result * self.getPow(mod, b[i])) % self.MOD
            if i != len(b) - 1:
                result = self.getPow(result, 10)
        return result
    
a= Solution()
print(a.superPow(2, [1, 0]))
print(a.superPow(2, [3]))