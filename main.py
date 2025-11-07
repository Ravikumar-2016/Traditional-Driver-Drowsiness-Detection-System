### command to run th eproject ###
# Bash:
#1.PowerShell (temporary policy bypass):
#cmd: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#2.venv\Scripts\Activate.ps1
#3.pip install -r requirements.txt
#4.python run_detection.py

from drowsiness_detector import DrowsinessDetector

if __name__ == "__main__":

    alarm_path = "alarm.wav"
    detector = DrowsinessDetector(alarm_path) # Creates an instance of the DrowsinessDetector class.

    detector.start()
