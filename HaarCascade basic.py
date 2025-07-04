###
# Real-time Haar Cascade tracking test
#  This script tests the Haar Cascades testing on a live
#  camera image stream, using the stock face-detection
#  cascade packed with the OpenCV utilities
#
#
###

#Vision and math imports
import cv2
import numpy as np
from scipy import ndimage

#Activate the camera capture at a low-res 120x180 resolution
cam = cv2.VideoCapture(1)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 120);
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 180);

#Load in the face cascade classifier
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Start up a display window
winName = "face tracking"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

#Loop forever
while (1):

    #Load image from the camera
    image = cam.read()[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convery to grayscale

    #Run the Haar classifier on the image
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=3,
        minSize=(0, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

    #Looping over all detected regions
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) #Plot the detected rectangle

    #Show the image with the detection region marked
    cv2.imshow( winName, image)

    #100Hz update rate
    key = cv2.waitKey(10)

    #On pressing the esc key, quit and close windows
    if key == 27:
       cv2.destroyWindow(winName)
       break
    



