from djitellopy import tello
import cv2

import time
me = tello.Tello()
me.connect()
me.streamon()
img = me.get_frame_read().frame
print(img)
cv2.imshow("Tello", img)
time.sleep(1)
me.stream_off()
test = test - 1