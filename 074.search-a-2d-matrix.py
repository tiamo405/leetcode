class Solution(object):
            
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row-1
        while top <= bottom:
            mid = (top+bottom)//2
            if matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid -1
            else:
                break
        mid = (top+bottom)//2
        print(mid)
        arr = matrix[mid]
        left, right = 0, col-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                return True
        return False
a = Solution()
print(a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 23)) # 1
        