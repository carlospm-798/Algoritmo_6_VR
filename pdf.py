#Algoritmo VI
#Paredes Márquez Carlos
#10 09 2021

import cv2
import numpy as np

h = np.zeros((480, 640), dtype=np.uint8) + int(240/2) #Hue / Matiz
s = np.zeros((480, 640), dtype=np.uint8) + 225
v = np.zeros((480, 640), dtype=np.uint8) + 37

hsv = cv2.merge((h, s, v))
im = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Image0',im)
cv2.waitKey(0)