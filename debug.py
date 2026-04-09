# import cv2

# # Địa chỉ RTSP của camera
# rtsp_url = "rtsp://admin:cxview2021@192.168.100.95:555/live"

# import cv2

# def record_rtsp(rtsp_url, output_file, duration_sec):
#     # Mở luồng RTSP
#     cap = cv2.VideoCapture(rtsp_url)

#     # Kiểm tra xem luồng đã mở thành công chưa
#     if not cap.isOpened():
#         print("Không thể mở luồng RTSP")
#         return

#     # Xác định định dạng video và tốc độ khung hình
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = int(cap.get(cv2.CAP_PROP_FPS))

#     # Khởi tạo video writer để ghi video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

#     start_time = cv2.getTickCount()
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Ghi frame vào tệp video
#         out.write(frame)

#         # Kiểm tra thời gian ghi và dừng ghi lại khi đạt đến thời gian quy định
#         current_time = cv2.getTickCount()
#         elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
#         if elapsed_time >= duration_sec:
#             break

#     # Giải phóng tài nguyên
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":

#     output_file = "recorded_video.mp4"
#     duration_sec = 3  # Độ dài video ghi lại tính bằng giây

#     record_rtsp(rtsp_url, output_file, duration_sec)

# code lại hàm sort nổi bọt
# logic: đi qua từng phần tử của mảng, so sánh nó với phần tử tiếp theo và hoán đổi chúng nếu chúng không theo thứ tự. Quá trình này được lặp lại cho đến khi toàn bộ mảng được sắp xếp.
arr = [64, 34, 25, 12, 22, 11, 90, 89, 78, 56]
print("Original array is:", arr)
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Pass", i+1, ":", arr)
print("Sorted array is:", arr)

# code lại hàm sort chèn
# logic : đi qua từng phần tử của mảng, so sánh nó với các phần tử trước đó và chèn nó vào vị trí đúng trong phần đã được sắp xếp của mảng. Quá trình này được lặp lại cho đến khi toàn bộ mảng được sắp xếp.
arr = [12, 11, 13, 5, 6]
print("Original array is:", arr)
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print("Pass", i, ":", arr)
print("Sorted array is:", arr)