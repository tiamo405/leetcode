class Solution(object):
    def thetich(self, height, i, j):

        return min(height[i], height[j])*(j-i)
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        aws = 0
        while right > left :
            aws =max(aws, self.thetich(height, left, right))
            if height[right] >= height[left]:
                left+=1
            else : right -=1
        return aws

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))