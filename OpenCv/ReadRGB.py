import os
import cv2

folderName = os.path.dirname(os.path.realpath(__file__))

image = cv2.imread(folderName + os.path.sep + 'nature.jpeg')

imgHeight , imgWidth , channel = image.shape

print("Image height = {} , Image width = {} , channel = {}".format(imgHeight,imgWidth,channel) )

blue , green , red = cv2.split(image)

print(red)
print(type(red))
img2 = cv2.merge([green,blue,red])

# cv2.imshow('Nature Photo before',image)
# cv2.imshow('Nature Photo after',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()