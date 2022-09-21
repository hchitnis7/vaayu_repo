# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())
# load the image
cap = cv2.VideoCapture(1)
while True:
	key = cv2.waitKey(1)
	_, frame = cap.read()
	# find all the 'black' shapes in the image
	lower = np.array([50, 52, 50])
	upper = np.array([85, 255, 255])
	shapeMask = cv2.inRange(frame, lower, upper)
	# find the contours in the mask
	cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

