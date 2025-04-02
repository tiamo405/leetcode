
class Solution(object):
    def minCosts(self, cost):
        n = len(cost)
        
        dp = [101 for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(0, i+1):
                dp[i] = min(dp[i], cost[j])
        return dp
a = Solution()
print(a.minCosts([5,3,4,1,3,2]))
print(a.minCosts([1,2,4,6,7]))
        