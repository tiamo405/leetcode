class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ""
        ans = 0
        ans_tmp = 0
        for i in s:
            if i == '(' :
                
                tmp = tmp+ i
                
            else :
                if len(tmp) == 0 or tmp[-1] == ')':
                    ans = max(ans, ans_tmp)
                    tmp = ""
                    ans_tmp = 0
                elif tmp[-1] == '(' :
                    ans_tmp +=1
                    tmp = tmp[:-1]

        ans = max(ans, ans_tmp)
        return ans*2
a= Solution()
print(a.longestValidParentheses('()()'))

# chua ac