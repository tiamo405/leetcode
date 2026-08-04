class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2) and len(res)< k:
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and j + 1 < len(nums2):
                if nums1[i + 1] + nums2[j] < nums1[i] + nums2[j + 1]:
                    i += 1
                else:
                    j += 1
            elif i + 1 < len(nums1):
                i += 1
            elif j + 1 < len(nums2):
                j += 1
            else:
                break
        return res