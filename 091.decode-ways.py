class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        dp = [0] * (str_len + 1)
        dp[0] = 1
        if str_len == 0:
            return 0
        if str_len == 1:
            return 1 if s[0] != '0' else 0
        if str_len >=2:
            if s[0] == '0':
                return 0
            elif s[0] == '1':
                if s[1] == '0':
                    dp[1] = 1
                else :
                    dp[1] = 2
            elif s[0] == '2':
                if s[1] == '0':
                    dp[1] = 1
                elif s[1] <= '6':
                    dp[1] = 2
                else:
                    dp[1] = 1
            else:
                if s[1] == '0':
                    return 0
                else:
                    dp[1] = 1
        # dq[i] =  so cach decode tu 0 -> i
        for i in range(2, str_len):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                dp[i] += dp[i-2]
        return dp[str_len-1]
a = Solution()
print(a.numDecodings("99"))
            