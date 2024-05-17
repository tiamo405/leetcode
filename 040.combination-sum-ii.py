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
    
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(start+1, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        result = self.remove_arr(result)
        print(result)
        return result

a= Solution()
a.combinationSum2([10,1,2,7,6,1,5], 8)