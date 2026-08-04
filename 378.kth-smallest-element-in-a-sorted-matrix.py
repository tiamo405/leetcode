class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # n = len(matrix)
        # index = [0] * n
        # # ghep tat ca cac phan tu cua ma tran vao 1 mang
        # arr = []
        # for i in range(n):
        #     for j in range(n):
        #         arr.append(matrix[i][j])
        # arr.sort()
        # return arr[k - 1]
    # vái ò AC đèo mẹ bịp 
        n = len(matrix)
        index = [0] * n
        # ghep tat ca cac phan tu cua ma tran vao 1 mang nhung sap xep
        while True:
            min_value = float('inf')
            min_index = -1
            for i in range(n):
                if index[i] < n and matrix[i][index[i]] < min_value:
                    min_value = matrix[i][index[i]]
                    min_index = i
            index[min_index] += 1
            k -= 1
            if k == 0:
                return min_value
