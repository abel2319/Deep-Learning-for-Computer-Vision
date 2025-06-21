from pathlib import Path
import cv2

data = Path("data_video")
video_path = data / "video.mp4"

frames_dir = data / "extracted_frames_"
frames_dir.mkdir(exist_ok=True)

video_capture = cv2.VideoCapture(video_path)

frame_count = 0
while True:
    success, frame = video_capture.read()
    if not success:
        break

    frame_path = frames_dir / f"frame_{frame_count}.jpg"
    cv2.imwrite(frame_path, frame)

    frame_count += 1

video_capture.release()




