class MedianFinder(object):

    def __init__(self):
        self.data = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.data.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        self.data.sort()
        n = len(self.data)
        if n % 2 == 1:
            return float(self.data[n // 2])
        else:
            mid1 = self.data[n // 2 - 1]
            mid2 = self.data[n // 2]
            return (mid1 + mid2) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()