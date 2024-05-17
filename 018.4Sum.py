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
    
    def find_ai_aj(self, arr, target):
        left = 0
        right = len(arr)-1
        cap_ij = []
        while left < right:
            sum_ = arr[left] + arr[right] 
            if sum_ == target:
                cap_ij.append([arr[left], arr[right]])
                left +=1
                right -=1
            elif sum_ > target :
                right -=1
            else:
                left +=1
        return cap_ij
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        for a in range(0, len(nums)-3):
            for b in range(a+1, len(nums)-2):
                temp_arr = nums[b+1:]
                cap_ij = self.find_ai_aj(temp_arr, target - nums[a]- nums[b])
                if len(cap_ij) !=0:
                    for cd in cap_ij:
                        c, d = cd[0], cd[1]  
                        ans.append([nums[a],nums[b],c,d])
        return self.remove_arr(ans)

a= Solution()
print(a.fourSum([1,0,-1,0,-2,2], 0))
                
