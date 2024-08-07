import cv2
import os
import Module as htm

cap = cv2.VideoCapture(0)
cap.set(3, 390)
cap.set(4, 400)

folder = "images" #folder of images that will be changed depend on finger count
mylist = os.listdir(folder)
imgs_list = []
img_sz = 150

for img_path in mylist:
    img = cv2.imread(f'{folder}/{img_path}') #read the images
    img = cv2.resize(img, (img_sz, img_sz))#resize them
    img = cv2.flip(img, 1)
    imgs_list.append(img)

detector = htm.handDetector(detectionCon=0.5)

tip_IDs=[4,8,12,16,20]#landmark index of the top point for each finger

while True:
    ret, img = cap.read()

    img = detector.findHands(img)
    lmlist = detector.find_pos(img, draw=False)
    #print(lmlist)
    if len(lmlist) !=0:
        for hand_lms in lmlist:
            fingers = []
            #handindling thumb
            if hand_lms[tip_IDs[0]][1] > hand_lms[tip_IDs[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
                #handling the 4 fingers
            for id in range(1, 5):
                if hand_lms[tip_IDs[id]][2] < hand_lms[tip_IDs[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        #print(fingers)

        cnt_fingers=fingers.count(1)
        # print(cnt_fingers)

        h, w, c = imgs_list[0].shape
        img[0:h, 0:w] = imgs_list[cnt_fingers-1]

        cv2.putText(img, f"Number of Fingers: {cnt_fingers}",
                    (int(w / 2) + 100, 28),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow("Finger Counter using Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
