# Real-Time Object Detection using YOLOv8

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

A lightweight object detection and tracking system powered by YOLOv8n for video analysis.

## Features

- Real-time object detection and tracking
- Persistent object ID tracking across video frames
- Video processing with annotated output
- Optimized for traffic and CCTV footage analysis

## Prerequisites

- Python 3.8 or higher
- Webcam or video file for processing

## Installation

```bash
pip install ultralytics opencv-python
```

## Usage

1. Place your video file (e.g., `normal_traffic.mp4`) in the project directory
2. Run the detection script:

```bash
python run_yolo_final.py
```

3. The processed video will be saved as `youtube_analysis.mp4`

## Configuration

The script uses the following default parameters:
- **Model**: YOLOv8n (nano - fastest variant)
- **Confidence threshold**: 0.25
- **Image size**: 640px
- **Tracking**: Enabled with persistent IDs

## Project Structure

```
Object_Detection/
├── run_yolo_final.py    # Main detection script
├── yolov8n.pt           # Pre-trained YOLOv8 nano model
└── README.md            # Documentation
```
## Author

**Heshan Ranasinghe**  
Electronic and Telecommunication Engineering Undergraduate

- Email: hranasinghe505@gmail.com
- GitHub: [@DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)
- LinkedIn: [Heshan Ranasinghe](https://www.linkedin.com/in/heshan-ranasinghe-988b00290)
