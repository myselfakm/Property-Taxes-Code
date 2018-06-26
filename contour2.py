# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:46:49 2018

@author: Amit
"""


import cv2
import numpy as np
import os
path = 'C://Users/Amit/Downloads'

image = cv2.imread('C://Users/Amit/Downloads/Elevation_export.tif')
blurred =cv2.pyrMeanShiftFiltering(image,31,91)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

ret ,threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


_,contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print ("Number of contours detected %d -> ",len(contours))
cv2.drawContours(image,contours,-1,(0,0,255),6)

cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',image)
cv2.waitKey()
cv2.imwrite(os.path.join(path ,'Elevation_export.tif'),image)


