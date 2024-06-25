class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        a = list(a)
        b = list(b)
        for i in range(len(a) - len(b)):
            b.insert(0, '0')
        for i in range(len(a)):
            a[i] = int(a[i])
            b[i] = int(b[i])
        sodu = 0
        for i in range(len(a)-1, -1,-1):
            a[i] = a[i] + b[i] + sodu
            if a[i] ==2:
                a[i] = 0
                sodu = 1
            elif a[i] == 3:
                a[i] = 1
                sodu = 1
            else:
                sodu = 0
        if sodu == 1:
            a.insert(0, 1)
        return ''.join(map(str, a))
a = Solution()
print(a.addBinary("1010", "1011")) # 10101