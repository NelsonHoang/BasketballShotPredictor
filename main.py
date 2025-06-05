import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

# Initialize the Video
cap = cv2.VideoCapture('Videos/vid (1).mp4')

# Create the color Finder object
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 0, 'smin': 105, 'vmin': 0, 'hmax': 15, 'smax': 255, 'vmax': 255}

while True:
    # Grab the image
    success, img = cap.read()
    # img = cv2.imread("Ball.png")
    img = img[0:900, :]

    # Find the Color Ball
    imgColor, mask = myColorFinder.update(img, hsvVals)

    # Display
    imgColor = cv2.resize(src=imgColor, dsize=(640, 480), dst=None, fx=0.7, fy=0.7)
    #cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgColor)
    cv2.waitKey(50)
