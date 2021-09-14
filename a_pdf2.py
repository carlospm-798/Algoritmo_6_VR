#Algoritmo VI
#Paredes Márquez Carlos
#14 09 2021

import cv2
import numpy as np

im_rgb = cv2.imread('paint.png')

h = np.zeros((480, 640), dtype=np.uint8) + int(75/2) #Hue / Matiz
s = np.zeros((480, 640), dtype=np.uint8) + int((87*255)/100)
v = np.zeros((480, 640), dtype=np.uint8) + int((90*255)/100)

h1 = np.zeros((480, 640), dtype=np.uint8) + int(193/2) #Hue / Matiz
s1 = np.zeros((480, 640), dtype=np.uint8) + int((35*255)/100)
v1 = np.zeros((480, 640), dtype=np.uint8) + int((92*255)/100)

h2 = np.zeros((480, 640), dtype=np.uint8) + int(229/2) #Hue / Matiz
s2 = np.zeros((480, 640), dtype=np.uint8) + int((55*255)/100)
v2 = np.zeros((480, 640), dtype=np.uint8) + int((64*255)/100)

h3 = np.zeros((480, 640), dtype=np.uint8) + int(236/2) #Hue / Matiz
s3 = np.zeros((480, 640), dtype=np.uint8) + int((69*255)/100)
v3 = np.zeros((480, 640), dtype=np.uint8) + int((80*255)/100)

hsv = cv2.merge((h, s, v))
im = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

hsv1 = cv2.merge((h1, s1, v1))
im1 = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR)

hsv2 = cv2.merge((h2, s2, v2))
im2 = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)

hsv3 = cv2.merge((h3, s3, v3))
im3 = cv2.cvtColor(hsv3, cv2.COLOR_HSV2BGR)

cv2.imshow('Image0',im)
cv2.imshow('Image1',im1)
cv2.imshow('Image2',im2)
cv2.imshow('Image3',im3)
cv2.imshow('ImageRGB', im_rgb)
cv2.waitKey(0)