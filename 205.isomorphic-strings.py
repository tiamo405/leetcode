class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = t[i]
            if t[i] not in dict_t:
                dict_t[t[i]] = s[i]
            if dict_s[s[i]] != t[i] or dict_t[t[i]] != s[i]:
                return False
        return True
a = Solution()
print(a.isIsomorphic("egg", "add"))  # Output: True
print(a.isIsomorphic("foo", "bar"))  # Output: False
print(a.isIsomorphic("paper", "title"))  # Output: True
print(a.isIsomorphic("badc", "baba")) # False