#import the necessary packages
import argparse
import cv2

#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#load the image, grab its dimensions and show it
image = cv2.imread(args["image"])
print image.shape
(h , w) = image.shape[:2]
cv2.imshow("Original", image)
#images are just numpy arrays. the top-left pixel can be found at (0,0)
(b,g,r) = image[0,0]
print "Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

image[0,0] = (0,0 , 255)
(b,g,r) = image[0,0]
print "Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

#compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w/2, h/2)

tl = image[0:cY, 0:cX] # slicing is like cutting image
# in a similar fashion, let's grab the top-right, bottom-right, and bottom-left
# corners and dispaly them
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", tl);
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

#make the top-left corner of the original image green
image[0:cY, 0:cX] = (0, 255, 0)

	
(b, g, r) = image[225,111]
print("newImage: blue:{b} green:{g} red:{r}".format(b=b, g=g, r=r) )


#show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)


