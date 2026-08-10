class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(1, n + 1):
            result.append(str(i))
        result.sort()
        return [int(x) for x in result]