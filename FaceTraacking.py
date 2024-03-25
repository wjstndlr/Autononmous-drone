import time
import cv2
import numpy as np
from djitellopy import tello

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
me.takeoff()
me.send_rc_control(0, 0, 18, 0)
time.sleep(2.2)

w, h = 360, 240
fbrange = [4200,4800]
pid = [0.6,0.6,0]
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("opencvPython/haarcascade_frontalcatface.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 6)
## scaleFaactor : 영상축소비율, 기본값은 1.1
## minNegihbors : 얼마나 많은 이웃 사각형이 검출되어야 최종 검출 영역으로 선정할지를 결정
    myfacelistC = []
    myfaceListArea = []

    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x + w//2
        cy = y + h//2
        area = w * h
        cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
        myfacelistC.append([cx,cy])
        myfaceListArea.append(area)

    if len(myfaceListArea) != 0 :
        i = myfaceListArea.index(max(myfaceListArea))
        return img, [myfacelistC[i], myfaceListArea[i]]
    else:
        return img, [[0,0],0]

def trackface(me ,info, w, pid, pError):
    area = info[1]
    x,y = info[0]
    fb = 0
    error = x- w//2
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = int(np.clip(speed, -100, 100))

    if area > fbrange[0] and area < fbrange[1] :
        fb = 0
    elif area > fbrange[1]:
        fb = -20
    elif area < fbrange[0] and area !=0:
        fb = 20

    if x==0:
       speed = 0
       error = 0

    print(speed,fb)

    me.send_rc_control(0, fb, 0, speed)
    return error
## main

#cap = cv2.VideoCapture(0)
while True:
    #_,img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w,h))
    img, info = findFace(img)
    pError = trackface(me, info, w, pid, pError)
    print("center",info[0], "Area", info[1])
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        me.land()
        break