import cv2
import mediapipe as mp
import numpy as np
from utils import play_alarm, stop_alarm

class DrowsinessDetector:
    def __init__(self, alarm_path):
        self.alarm_path = alarm_path
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(refine_landmarks=True)
        self.draw = mp.solutions.drawing_utils
        self.prev_time = 0
        self.alarm_on = False

    def eye_aspect_ratio(self, landmarks, eye_indices):
        p1, p2, p3, p4, p5, p6 = [landmarks[i] for i in eye_indices]
        A = np.linalg.norm(np.array(p2) - np.array(p6))
        B = np.linalg.norm(np.array(p3) - np.array(p5))
        C = np.linalg.norm(np.array(p1) - np.array(p4))
        ear = (A + B) / (2.0 * C)
        return ear

    def start(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        EAR_THRESH = 0.25
        EAR_CONSEC_FRAMES = 15
        COUNTER = 0

        LEFT_EYE = [33, 160, 158, 133, 153, 144]
        RIGHT_EYE = [263, 387, 385, 362, 380, 373]

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_frame)

            if results.multi_face_landmarks:
                mesh_points = np.array(
                    [[p.x * frame.shape[1], p.y * frame.shape[0]]
                     for p in results.multi_face_landmarks[0].landmark]
                )

                left_ear = self.eye_aspect_ratio(mesh_points, LEFT_EYE)
                right_ear = self.eye_aspect_ratio(mesh_points, RIGHT_EYE)
                ear = (left_ear + right_ear) / 2.0

                if ear < EAR_THRESH:
                    COUNTER += 1
                    if COUNTER >= EAR_CONSEC_FRAMES:
                        if not self.alarm_on:
                            self.alarm_on = True
                            play_alarm(self.alarm_path)
                        cv2.putText(frame, "DROWSINESS ALERT!", (100, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                else:
                    # Driver looks normal again
                    COUNTER = 0
                    if self.alarm_on:
                        stop_alarm()
                        self.alarm_on = False

                cv2.putText(frame, f"EAR: {ear:.2f}", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow("Driver Drowsiness Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        stop_alarm()  # stop alarm if still playing
