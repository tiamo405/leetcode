class Solution(object):
    def maxProfit(self, prices):
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
a = Solution()
print(a.maxProfit([7,6,4,3,1])) # 5