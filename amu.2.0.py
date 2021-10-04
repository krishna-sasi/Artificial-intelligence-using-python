import cv2
from djitellopy import tello
import time
import KeyPressModule as kp

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey(("u")): me.flip_forward()
    if kp.getKey(("j")): me.flip_back()
    if kp.getKey(("h")): me.flip_left()
    if kp.getKey(("k")): me.flip_right()

    if kp.getKey(("l")): me.land()
    if kp.getKey(("t")): me.land()

    return [lr, fb, ud, yv]


me.takeoff()

while True:
    img = me.get_frame_read().frame
    cv2.imshow("Image", img)
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(0.05)
