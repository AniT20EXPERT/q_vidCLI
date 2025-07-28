import cv2

def detect_blurriness(video_path, sample_rate=24):
    cap = cv2.VideoCapture(video_path)
    blur_scores = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % sample_rate == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            blur_scores.append(lap_var)
        frame_count += 1

    cap.release()
    return blur_scores
