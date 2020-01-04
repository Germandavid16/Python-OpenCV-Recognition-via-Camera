import cv2
import numpy as np

img = cv2.imread("lena256rgb.jpg")
cv2.imshow("Normal", img)
cv2.waitKey(0)

face = img[95:195, 100:180]
cv2.imshow("Face", face)
cv2.waitKey(0)
 
body = img[20:, 35:210]
cv2.imshow("Body", body)
cv2.waitKey(0)

cv2.destroyAllWindows()
