class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        tp = [[0 for i in range(len(triangle[j]))] for j in range(len(triangle))]
        tp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            tp[i][0] = tp[i-1][0] + triangle[i][0]
            tp[i][-1] = tp[i-1][-1] + triangle[i][-1]
            for j in range(1, len(triangle[i])-1):
                tp[i][j] = min(tp[i-1][j-1], tp[i-1][j]) + triangle[i][j]
        return min(tp[-1])
a = Solution()
print(a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11