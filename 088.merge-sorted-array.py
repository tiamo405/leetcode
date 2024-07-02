class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m+ n and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i,nums2[j])
                nums1.pop()
                j += 1
                i += 1

        if j < n:
            nums1[m+j:] = nums2[j:]
        return nums1
a = Solution()
print(a.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)) 