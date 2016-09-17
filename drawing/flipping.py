# import
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#flip the image horizontally
flipped = cv2.flip(image, 1)
print flipped[235,259]
print "----"
cv2.imshow("Flipped horizontally", flipped)

rotated = imutils.rotate(flipped, 45)
flipped_ver = cv2.flip(rotated, 0)
print flipped_ver[189,441]
print "------"

#flip vertical
flipped = cv2.flip(image, 0)
cv2.imshow("flipped vertically", flipped)

#Flipped horizontally & vertically
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped horizontally & vertically", flipped)
cv2.waitKey(0)