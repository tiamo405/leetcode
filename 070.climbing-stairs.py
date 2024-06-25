class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dq = [0 for i in range(n+1)]
        dq[0] = 1
        dq[1] = 1
        for i in range(2,n+1):
            dq[i] = dq[i-1] + dq[i-2]
        return dq[n]

a = Solution()
print(a.climbStairs(2)) # 2