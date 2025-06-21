class Solution(object):
    def tinhDienTich(self, A, B, C):
        if A[1] != B[1]: # AB song song truc hoanh
            return 0
        chieurong = abs(A[0] - B[0]) # chieu rong la khoang cach truc hoanh
        chieudai = abs(A[1] - C[1]) # chieu dai la khoang cach truc tung
        return chieurong * chieudai  # dien tich tam giac la 1/2 chieu rong * chieu dai (khong chia 2 vi de bai yeu cau tra ve dien tich * 2) (neu chia 2 o day co the se khong dung voi cac test case)
    def maxArea_x(self, coords):
        A = [coords[0][0], coords[0][1]] # A la diem dau tien
        B = [0, 0] # B la diem thu hai
        C = [0, 0] # C la diem thu ba
        max_area = 0
        for i in range(1, len(coords)):
            if coords[i][1] == A[1]: # if the x-coordinate is the same as A_y, AB song song Ox
                B = [coords[i][0], coords[i][1]] # B la diem thu hai
            else: # AB dang dai nhat, tim diem C xa nhat de dien tich lon nhat
                max_area = max(max_area, max(self.tinhDienTich(A, B, [coords[0][0], coords[0][1]]), self.tinhDienTich(A, B, [coords[len(coords)-1][0], coords[len(coords)-1][1]])))
                A = [coords[i][0], coords[i][1]]
        # Xet truong hop B la diem cuoi cung
        if i == len(coords) - 1:
            max_area = max(max_area, self.tinhDienTich(A, B, [coords[0][0], coords[0][1]]))
            max_area = max(max_area, self.tinhDienTich(A, B, [coords[len(coords)-1][0], coords[len(coords)-1][1]]))
        return max_area
                
            
    def maxArea(self, coords):
        # sort the coordinates by y and x
        coords.sort(key=lambda x: (x[1], x[0]))  # sort by y first, then by x
        max_area = 0
        max_area = max(max_area, self.maxArea_x(coords)) # max area with x-axis
        # dao nguoc lai cac toa do
        coords = [[y, x] for x, y in coords]  # swap x and y
        coords.sort(key=lambda x: (x[1], x[0]))  # sort by y first, then by x
        max_area = max(max_area, self.maxArea_x(coords))
        return int(max_area) if max_area > 0 else -1  # multiply by 2 to get the actual area

a = Solution()
print(a.maxArea([[1,1],[1,2],[3,2],[3,3]])) # Output: 2
print(a.maxArea([[1,1],[2,2],[3,3]])) # Output: -1
print(a.maxArea([[1,1],[6, 10],[6, 5]])) # Output: 25
print(a.maxArea([[8,7],[2,9],[2,4]])) # Output: 30
# ý tưởng : sắp xếp các tọa độ theo trục hoành rồi đến tung, sau đó tìm 2 điểm A, B cùng thuộc 1 đường // Ox avf dài nhất, AB sẽ mà max đáy tam giác, sau đó sẽ tìm điểm C . điểm C chỉ có thể là điểm thứ 0 hoặc n-1 thì mới cách xa nhất, sau đó tính diện tích tam giác ABC. Sau đó lặp lại với các điểm còn lại, cuối cùng sẽ tìm được diện tích tam giác lớn nhất.
# tuy nhiên còn case về song song Oy thì đảo ngược giá trị x,y từng điểm và lại lặp lại quá trình trên, cuối cùng sẽ tìm được diện tích tam giác lớn nhất.