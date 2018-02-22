# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load an color image in grayscale
''' Second argument is a flag which specifies the way image should be read
cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
 1, 0 or -1 - numerical represnetation of above explained 
'''

img = cv2.imread('dhoni.jpg',0)
#img = cv2.imread('dhoni.jpg',1)
#img = cv2.imread('dhoni.jpg',-1)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
cv2.imwrite('dhoni_gray.png',img)

edges = cv2.Canny(img,100,200)
cv2.imshow('image',edges)

#cv2.waitKey() - waits till we press a key from the kepboard and waits for the given sec and closes
cv2.waitKey(0)  
cv2.destroyAllWindows()