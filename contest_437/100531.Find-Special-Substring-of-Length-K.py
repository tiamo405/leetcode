class Solution(object):
    def checkString(self, s):
        # tat car ki tu trong s deu giong nhau
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                return False
        return s[0]
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        for i in range(len(s) - k + 1):
            s_tmp = s[i:i+k]
            if self.checkString(s_tmp):
                first_char = s_tmp[0]
                if i != 0 and i + k != len(s):
                    if s[i-1] != first_char and s[i+k] != first_char:
                        return True
                elif i == 0:
                    if i+k == len(s):
                        return True
                    elif s[i+k] != first_char:
                        return True                    
                else:
                    if s[i-1] != first_char:
                        return True
        return False
a = Solution()
print(a.hasSpecialSubstring("aaabaaa", 3))
print(a.hasSpecialSubstring("abc", 2))
print(a.hasSpecialSubstring("h",1))
print(a.hasSpecialSubstring("aa",2))

