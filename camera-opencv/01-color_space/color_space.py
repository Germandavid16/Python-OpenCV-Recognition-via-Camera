import cv2
import numpy as np

image = cv2.imread("lena256rgb.jpg")
cv2.imshow("Normal", image)
cv2.waitKey(0)

# Convert BGR to Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Threshold the gray image to binary image
# ...

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

# Convert HSV to RGB
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR", bgr)
cv2.waitKey(0)

cv2.destroyAllWindows()

