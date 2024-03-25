from djitellopy import tello
import cv2
import numpy as np

from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

def empty():
    pass

me.streamon()

cv2.namedWindow("TRACKBARS")
cv2.resizeWindow("TRACKBARS", 640, 240)
cv2.createTrackbar("HUE Min", "TRACKBARS", 0, 179, empty)
cv2.createTrackbar("HUE Max", "TRACKBARS", 179, 179, empty)
cv2.createTrackbar("SAT Min", "TRACKBARS", 0, 255, empty)
cv2.createTrackbar("SAT Max", "TRACKBARS", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "TRACKBARS", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "TRACKBARS", 255, 255, empty)


def threshold(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "TRACKBARS")
    h_max = cv2.getTrackbarPos("HUE Max", "TRACKBARS")
    s_min = cv2.getTrackbarPos("SAT Min", "TRACKBARS")
    s_max = cv2.getTrackbarPos("SAT Max", "TRACKBARS")
    v_min = cv2.getTrackbarPos("VALUE Min", "TRACKBARS")
    v_max = cv2.getTrackbarPos("VALUE Max", "TRACKBARS")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    return result

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,(480,360))
    threshold_img = threshold(img)


    cv2.imshow("Image",threshold_img)
    cv2.waitKey(1)