class Solution(object):
    def remove_arr(self, arrs):
        # Khởi tạo một tập hợp rỗng để lưu trữ các mảng đã xuất hiện
        seen = set()

        # Khởi tạo một danh sách mới để lưu trữ các mảng duy nhất
        unique_arrays = []

        # Duyệt qua các mảng trong arr
        for sub_arr in arrs:
            # Chuyển mảng thành tuple để có thể thêm vào tập hợp (set)
            tuple_arr = tuple(sorted(sub_arr))
            
            # Nếu mảng chưa xuất hiện, thêm vào danh sách kết quả và tập hợp đã thấy
            if tuple_arr not in seen:
                unique_arrays.append(sub_arr)
                seen.add(tuple_arr)
        return unique_arrays
    def find_ai_aj(self, arr, ak):
        left = 0
        right = len(arr)-1
        cap_ij = []
        while left < right:
            sum_ = arr[left] + arr[right] 
            if sum_ == ak:
                cap_ij.append([arr[left], arr[right]])
                left +=1
                right -=1
            elif sum_ > ak :
                right -=1
            else:
                left +=1
        return cap_ij
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for k in range(0, len(nums)-2):
            ak = nums[k]
            temp_arr = sorted(nums[k+1:])
            cap_ij = self.find_ai_aj(temp_arr, -ak)
            if len(cap_ij) !=0:
                for ij in cap_ij:
                    ai, aj = ij[0], ij[1]
                    ans.append([ai, aj, ak])
        return self.remove_arr(ans)
a = Solution()
print(a.threeSum([-3,-2,-1,0,1,2,3]))