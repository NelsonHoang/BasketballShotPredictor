import cv2
import cvzone

cap = cv2.VideoCapture('Videos/vid (1).mp4')

while True:
    success, img = cap.read()
    img = cv2.resize(src=img, dsize=(640, 480), dst=None, fx=0.7, fy=0.7)
    cv2.imshow("Image", img)
    cv2.waitKey(50)
