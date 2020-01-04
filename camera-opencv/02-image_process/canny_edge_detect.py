
import cv2 
import sys
import numpy as np


def nothing(x):
    pass


cv2.namedWindow('canny_demo')
cv2.createTrackbar('threshold',      'canny_demo', 0, 100, nothing)
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 5,   nothing)

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("lena512rgb.png")

while True:
    threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, apertureSize=3)
    cv2.imshow('canny_demo', edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("canny_demo.png", edges)
        break

cv2.destroyAllWindows()   
