# -*- coding: utf-8 -*-

import numpy as np 
import cv2


image = cv2.imread('bird.jpg')
#cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('bird',image)

''' To know about image : IMAGE property :
    
image.shape - It returns a tuple of number of rows, columns and channels (if image is color)
Note this is even seen in variable part of the spyder
Total number of pixels is accessed by image.size 

NOTE : image.dtype is very important while debugging  because a large number of errors in 
OpenCV-Python code is caused by invalid datatype.
'''

print (image.shape)
print (image.size)


'''Image ROI- region of images'''




'''Access only one colour pixel and pixel value at some point '''
print (len(image))

# we can get the colour intensity of the image 
px = image[100:105,100:105]
print (px)
#cv2.imwrite('bird2.png',image)
# we can chnage the colour intensity 
image[100:105,100:105] = [255,255,255]
print (image[100:105,100:105])
#cv2.imwrite('bird3.png',image)


#blue = image[:,:,0]
#print (blue)


cv2.waitKey(0)  
cv2.destroyAllWindows()



