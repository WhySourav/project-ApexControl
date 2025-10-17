import cv2
import numpy as np

def detect_lights_out(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    avg_brightness_prev = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_brightness = np.mean(gray)
        if avg_brightness - avg_brightness_prev > 25:
            timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
            print(f"Possible 'lights out' at {timestamp:.2f}s")
            break
        avg_brightness_prev = avg_brightness
        frame_count += 1
    cap.release()

if __name__ == "__main__":
    detect_lights_out("Bahrain_GP_2025.mp4")
