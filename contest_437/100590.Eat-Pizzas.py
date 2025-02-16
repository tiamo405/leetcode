class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        n_day = len(pizzas)//4
        pizzas.sort()
        ans = 0
        n_le = (n_day+1) // 2
        n_chan = n_day - n_le
        n = len(pizzas) - 1 
        for i in range(n_le):
            ans += pizzas[n-i]
            pizzas.pop(n-i)

        n = len(pizzas)
        for i in range(n_chan):
            ans += pizzas[n-i*2-2]
        print(ans)
        return ans
            

a = Solution()
a.maxWeight([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
a.maxWeight([1,2,3,4,5,6,7,8,9,10,11,12])
# a.maxWeight([1,2,3,4,5,6,7,8])
# a.maxWeight([1,2,3,4])