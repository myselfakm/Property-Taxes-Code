# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:41:39 2018

@author: Amit
"""

import cv2
import numpy as np

img = cv2.imread('circle.png')
px = img[100,100]
print(px)