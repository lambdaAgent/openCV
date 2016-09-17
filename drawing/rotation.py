# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
 
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread("wynn.png")
print image
cv2.imshow("Original", image)


# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)
 
# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
 
# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

rotated = imutils.rotate(image, 330)
(b,g,r) = rotated[254,335]
print "r",r
print "g",g
print "b",b

rotated = imutils.rotate(image, 110)
(b,g,r) = rotated[136,312]
print "r",r
print "g",g
print "b",b

rotated = imutils.rotate(image, 88, center=(50,50))
(b,g,r) = rotated[10,10]

print "r",r
print "g",g
print "b",b

cv2.waitKey(0)