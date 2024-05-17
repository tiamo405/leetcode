class Solution(object):
    def check_in(self, s_tmp, i, strs):
        for j in range(len(strs)):
            if s_tmp != strs[j][i]:
                return False
        return True
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = strs[0]
        for i in range(len(strs)):
            s = min(s, strs[i], key=len)
        
        if s == "": return ""
        ans = ""
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         s_tmp = s[i:j+1]
        #         if self.check_in(s_tmp, strs):
        #             ans = max(ans, s_tmp, key=len)
        #         else :
        #              return ans
        # return ans
        for i in range(len(s)):
            char = s[i]
            if self.check_in(char, i, strs):
                ans += char
            else :
                return ans
        return ans

a = Solution()
print(a.longestCommonPrefix(["flower"]))