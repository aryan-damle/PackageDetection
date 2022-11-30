import numpy as np 
import cv2 as cv

vid = cv.VideoCapture('tobbers.mov')

while vid.isOpened():
    ret, frame = vid.read()

    if not ret:
        print("Stream error, exiting program.")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

vid.release()
cv.destroyAllWindows()