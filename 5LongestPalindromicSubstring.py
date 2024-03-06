class Solution(object):
    def checkPalindromic(self, s:str):
        s_reverse = s[::-1]
        if s_reverse == s :
            return True
        return False
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     max_len = 0
    #     max_str = ""
    #     for i in range(len(s)):
    #         for j in range(i, len(s)+1):
    #             new_str = s[i:j]
    #             if self.checkPalindromic(new_str) :
    #                 if max_len < len(new_str):
    #                     max_str = new_str
    #                     max_len =  len(new_str)
    #     return max_str
    def extend(self, s, left, right):
        ans = ""
        while left >=0 and right <len(s):
            if s[left]!= s[right]:
                break
            ans = s[left:right+1]
            left -=1
            right +=1
        return ans
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            ans = max(ans, self.extend(s,i,i), self.extend(s,i,i+1), key= len)
        return ans


a= Solution()
print(a.longestPalindrome(s="aaaa"))