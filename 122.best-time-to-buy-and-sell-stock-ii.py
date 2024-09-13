class Solution(object):
    def maxProfitOneArr(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price, min_price = [0]*len(prices), [0]*len(prices)
        min_price[0] = prices[0]
        max_price[-1] = prices[-1]
        for i in range(1, len(prices)):
            min_price[i] = min(min_price[i-1], prices[i])
        for i in range(len(prices)-2, -1, -1):
            max_price[i] = max(max_price[i+1], prices[i])
        res = 0
        for i in range(len(prices)):
            res = max(res, max_price[i]-min_price[i])
        return res
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0]*len(prices)
        dp[1] = max(0, prices[1]-prices[0])
        for i in range(2, len(prices)):
            tmp = dp[i-1]
            for j in range(0, i):
                tmp = max(dp[j], self.maxProfitOneArr(prices[j:i]))
            dp[i] = tmp
        return dp[-1]
a = Solution()
print(a.maxProfit([7,1,5,3,6,4])) # 5
        