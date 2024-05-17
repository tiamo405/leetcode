class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[i])
                continue
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else :
                res.append(intervals[i])
        return res
    
a = Solution()
print(a.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [[1,10]]