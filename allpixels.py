# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:50:48 2018

@author: ace
"""

from PIL import Image
im = Image.open('4244.jpg')
width, height = im.size

def rgb_of_pixel(x, y):
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


all_pixels = []
for x in range(width):
    for y in range(height):
        all_pixels.append(rgb_of_pixel(x, y))

        