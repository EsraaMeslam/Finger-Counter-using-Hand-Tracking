import cv2
import mediapipe as mp

class handDetector:
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mp_Hands = mp.solutions.hands
        self.hands = self.mp_Hands.Hands(self.mode, self.maxHands,
                                         min_detection_confidence=self.detectionCon,
                                         min_tracking_confidence=self.trackCon)
        self.mp_draw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        img = cv2.flip(img, 1)
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res = self.hands.process(img_RGB)

        if self.res.multi_hand_landmarks:
            for hand_lms in self.res.multi_hand_landmarks:
                if draw:

                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_Hands.HAND_CONNECTIONS)
        return img

    def find_pos(self, img, draw=True):
        all_lmlists = []
        if self.res.multi_hand_landmarks:
            for hand_lms in self.res.multi_hand_landmarks:
                lmlist = []
                for id, lm in enumerate(hand_lms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmlist.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 6, (0, 0, 255), cv2.FILLED)
                all_lmlists.append(lmlist)
        return all_lmlists
