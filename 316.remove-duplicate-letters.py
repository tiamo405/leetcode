class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_count = {}
        for c in s:
            dict_count[c] = dict_count.get(c, 0) + 1
        stack = []
        for c in s:
            if dict_count[c] > 1 :
                dict_count[c] -= 1
            else:
                stack.append(c)
        return ''.join(stack)
a = Solution()
print(a.removeDuplicateLetters("bcabc"))
print(a.removeDuplicateLetters("cbacdcbc"))