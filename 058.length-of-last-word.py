class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr_s = s.split()
        print(arr_s)
        return len(arr_s[-1])
a = Solution()
print(a.lengthOfLastWord("   Hello World    ")) # 5