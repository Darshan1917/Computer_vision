# -*- coding: utf-8 -*-

import cv2
import numpy as np 
import matplotlib.pyplot as plt



image = cv2.imread('bird.jpg',0)
#cv2.imshow('image',image)
cv2.imshow('image',image)


cv2.waitKey(0)  
cv2.destroyAllWindows()



