class Solution(object):
    def chatNhiPhan(self, matrix, i, target):
        n = len(matrix[0])
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                if self.chatNhiPhan(matrix, i, target):
                    return True
        return False

a = Solution()
print(a.searchMatrix([[1, 4, 7, 11, 15],
                      [2, 5, 8, 12, 19],
                      [3, 6, 9, 16, 22],
                      [10, 13, 14, 17, 24],
                      [18, 21, 23, 26, 30]], 5))