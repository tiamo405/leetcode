class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[i])
                continue
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else :
                res.append(intervals[i])
        return res
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        return self.merge(intervals)

a = Solution()
print(a.insert([[1,3],[6,9]],[2,5])) # [[1,5],[6,9]]