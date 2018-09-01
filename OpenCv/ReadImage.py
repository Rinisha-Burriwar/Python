
import os
import cv2

scriptDir = os.path.dirname(os.path.realpath(__file__))

print(scriptDir)

img = cv2.imread(scriptDir + os.path.sep + 'nature.jpeg')

cv2.imshow("MY PHTO",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

