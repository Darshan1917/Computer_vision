# -*- coding: utf-8 -*-

import cv2
import dlib
import numpy as np 
import matplotlib.pyplot as plt



image = cv2.imread('forest.jpg')
#cv2.imshow('image',image)
cv2.imshow('image',image)
#hist = cv2.calcHist([image],0,None,[256],[0,256])
#colour pixel value
color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()
#plt.hist(image.ravel(),256,[0,256])
#plt.show()



cv2.waitKey(0)  
cv2.destroyAllWindows()
    


