# -*- coding: utf-8 -*-

'''BGR ↔ Gray and BGR ↔ HSV.
Syntax : cv2.cvtColor(input_image, flag) - flag determines the type of conversion.
BGR → Gray conversion we use the flags cv2.COLOR_BGR2GRAY. 
BGR → HSV, we use the flag cv2.COLOR_BGR2HSV.
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread('bird.jpg',-1)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow('image',image)
cv2.imshow('image',image)

''' Below is the code display 2 subplots of same image'''
#plt.subplot(121)
#plt.imshow(image1 ,cmap = 'CMRmap')
#plt.title('Gray Image')
#plt.subplot(122)
#plt.imshow(image , cmap = 'copper')
#plt.title('Original Image')


#ax3 = fig.add_subplot(2,2,3)
#ax3.imshow(...)
#ax4 = fig.add_subplot(2,2,4)
#ax4.imshow(...)

# ******* Extraction of colour from the image *********
# define range of blue color in HSV
lower_blue = np.array([100,10,10])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(image,image, mask= mask)

cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)  
cv2.destroyAllWindows()



