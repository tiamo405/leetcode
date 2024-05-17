import cv2

# Địa chỉ RTSP của camera
rtsp_url = "rtsp://admin:cxview2021@192.168.100.95:555/live"

import cv2

def record_rtsp(rtsp_url, output_file, duration_sec):
    # Mở luồng RTSP
    cap = cv2.VideoCapture(rtsp_url)

    # Kiểm tra xem luồng đã mở thành công chưa
    if not cap.isOpened():
        print("Không thể mở luồng RTSP")
        return

    # Xác định định dạng video và tốc độ khung hình
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Khởi tạo video writer để ghi video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    start_time = cv2.getTickCount()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Ghi frame vào tệp video
        out.write(frame)

        # Kiểm tra thời gian ghi và dừng ghi lại khi đạt đến thời gian quy định
        current_time = cv2.getTickCount()
        elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
        if elapsed_time >= duration_sec:
            break

    # Giải phóng tài nguyên
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    output_file = "recorded_video.mp4"
    duration_sec = 3  # Độ dài video ghi lại tính bằng giây

    record_rtsp(rtsp_url, output_file, duration_sec)

