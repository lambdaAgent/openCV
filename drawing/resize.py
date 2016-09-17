import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image");
args = vars(ap.parse_args())

#load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#aspect ratio
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

#perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized);
cv2.waitKey(0)

# params width/height will define target width/height, and auto ratio will be implemented
resized = imutils.resize(image, width=100, inter=cv2.INTER_NEAREST)
print resized[74,20]
print "----"

h,w = image.shape[:2]
resized = imutils.resize(image, width=w*2, inter=cv2.INTER_CUBIC)
print resized[367,170]
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)