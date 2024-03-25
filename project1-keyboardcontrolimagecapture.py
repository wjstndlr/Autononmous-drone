from djitellopy import tello
import keypressmodule as kp
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getkey("LEFT"):
        lr = -speed
    elif kp.getkey("RIGHT"):
        lr = speed
    if kp.getkey("UP"):
        fb = speed
    elif kp.getkey("DOWN"):
        fb = -speed
    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = -speed
    if kp.getkey("a"):
        yv = -speed
    elif kp.getkey("d"):
        yv = speed
    if kp.getkey("q"):
        me.land()
        time.sleep(3)
    if kp.getkey("e"):
        me.takeoff()

    if kp.getkey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (480, 360))
    cv2.imshow("Image", img)
    cv2.waitKey(1)