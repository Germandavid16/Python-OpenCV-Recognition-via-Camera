
import cv2
import sys
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Gaussian_Blur')
cv2.createTrackbar('ksize', 'Gaussian_Blur', 0, 10, nothing)

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("lena512rgb.png")

while True:
    ksize  = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')

    blur = cv2.GaussianBlur(image, (2*ksize+1, 2*ksize+1), 0)
    cv2.imshow('Gaussian_Blur', blur)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
