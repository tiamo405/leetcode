class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalTank = 0
        currTank = 0
        startIndex = 0
        for i in range(len(gas)):
            totalTank += gas[i] - cost[i]
            currTank += gas[i] - cost[i]
            if currTank < 0:
                startIndex = i + 1
                currTank = 0
        return startIndex if totalTank >= 0 else -1
a = Solution()
print(a.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
        
