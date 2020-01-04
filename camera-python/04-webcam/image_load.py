
import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]

# Read the image
image = cv2.imread(imagePath)

cv2.imshow("preview", image)
cv2.waitKey(0)

cv2.destroyAllWindows()


