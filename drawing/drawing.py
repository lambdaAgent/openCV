#import the necessary packages
import numpy as np
import cv2

#initialize our canvas as 300x300 with 3 channels Red Green Blue with black bg
canvas = np.zeros((300,300,3), dtype="uint8")

#draw a greenline from top-left corner of canvas to the bottom-right
green = (0,225,0)
cv2.line(canvas, (0,0) , (300,300) , green)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

#now, draw a 3 pixel thick red line from the top-right corner to the bottom-left
red = (0,0,255)
cv2.line(canvas, (300,0), (0,300) , red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


#draw a green 50 x 50 pixel square, starting at 10 x 10 and ending at 60 x 60
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

#draw another rectangle, this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50,200), (200,255), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#let's draw one last rectangle: blue and filled in
blue = (255, 0 ,0 )
cv2.rectangle(canvas, (200,50), (225,125), blue, -1) # -1 means no border
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# reset our canvas and draw a white circle at the center of the canvas with
# increasing radii - from 25 pixels to 150 pixels
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] /2 )
white = (255,255,255)

for r in xrange(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)

# show 
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)