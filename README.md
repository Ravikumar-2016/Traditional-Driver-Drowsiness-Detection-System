# 💤 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection** system that uses computer vision (OpenCV + Mediapipe) to monitor the driver’s eyes and alert them when drowsiness is detected.

## 🚗 Features
- Detects drowsiness using webcam in real-time.  
- Plays an alarm sound (`alarm.wav`) when the driver appears sleepy.  
- Lightweight and works on standard laptops.  
- Modular design with `utils.py` and `drowsiness_detector.py`.


## 🧩 Project Structure
📦 driver-drowsiness-detection

┣ 📜 alarm.wav # Alarm sound

┣ 📜 main.py # Entry point

┣ 📜 drowsiness_detector.py # Core detection logic

┣ 📜 utils.py # Helper functions

┣ 📜 requirements.txt # Dependencies

┗ 📜 README.md # Documentation

## ⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/Ravikumar-2016/Traditional-Driver-Drowsiness-Detection-System.git
cd Driver-Drowsiness-Detection-Traditional

2️⃣ Create and activate a virtual environment

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

▶️ Usage

Run the program: 
python main.py

# Make sure:

Your webcam is connected.
The program window has access to the camera.
When drowsiness is detected, an alert sound will play automatically.

🧠 Requirements

Python 3.8+
OpenCV
Mediapipe
Numpy
Pygame

💡 Future Improvements

Add blink frequency and yawning detection.
Log drowsy episodes with timestamps.
Integrate with vehicle hardware (e.g., vibration or seat alert).