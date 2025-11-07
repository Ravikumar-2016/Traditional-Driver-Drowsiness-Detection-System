```markdown
# 💤 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection** system that uses computer vision (**OpenCV + Mediapipe**) to monitor a driver’s eyes and alert them when signs of drowsiness are detected.

---

## 🚗 Features
- 👁️ Real-time drowsiness detection using webcam.  
- 🔊 Plays an alarm sound (`alarm.wav`) when drowsiness is detected.  
- 💻 Lightweight and works efficiently on standard laptops.  
- 🧩 Modular design with `utils.py` and `drowsiness_detector.py` for cleaner structure.

---

## 🧩 Project Structure
```

📦 driver-drowsiness-detection
┣ 📜 alarm.wav               # Alarm sound
┣ 📜 main.py                 # Entry point
┣ 📜 drowsiness_detector.py  # Core detection logic
┣ 📜 utils.py                # Helper functions
┣ 📜 requirements.txt        # Dependencies
┗ 📜 README.md               # Documentation

````

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ravikumar-2016/Traditional-Driver-Drowsiness-Detection-System.git
cd Driver-Drowsiness-Detection-Traditional
````

---

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
```

#### 🪟 Windows

```bash
venv\Scripts\activate
```

#### 🐧 macOS/Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

To run the system:

```bash
python main.py
```

---

## ✅ Make Sure

* Your **webcam** is connected and functional.
* The program window has **permission to access** the camera.
* When drowsiness is detected, the **alarm sound** (`alarm.wav`) will play automatically.

---

## 🧠 Requirements

| Dependency  | Purpose                   |
| ----------- | ------------------------- |
| Python 3.8+ | Programming language      |
| OpenCV      | Image processing          |
| Mediapipe   | Facial landmark detection |
| NumPy       | Numerical computation     |
| Pygame      | Playing alarm sound       |

---

## 💡 Future Improvements

* Add **blink frequency** and **yawning detection**.
* Log **drowsiness events with timestamps**.
* Integrate with vehicle hardware (e.g., vibration or seat alert).
* Add a **dashboard interface** for monitoring performance.