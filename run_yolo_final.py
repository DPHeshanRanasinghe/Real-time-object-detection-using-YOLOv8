from ultralytics import YOLO
import cv2

# Load the model
model = YOLO('yolov8n.pt') 

# Load the new YouTube video
cap = cv2.VideoCapture("normal_traffic.mp4")

# Get properties
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
out = cv2.VideoWriter('youtube_analysis.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

print("Processing YouTube CCTV footage... This is true traffic analysis!")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # .track() keeps track of IDs across frames
    results = model.track(frame, persist=True, conf=0.25, imgsz=640, verbose=False)

    # Annotated frame now includes IDs!
    annotated_frame = results[0].plot()

    out.write(annotated_frame)

cap.release()
out.release()
print("Success! Download 'youtube_analysis.mp4' to see your AI-powered CCTV.")
