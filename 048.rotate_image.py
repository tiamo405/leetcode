class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(A[0])
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n-1-i] = A[i][j]
        
        A = res
        return A


a = Solution()
print(a.rotate([[1,2,3],[4,5,6],[7,8,9]]))