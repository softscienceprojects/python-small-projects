import cv2 as cv
import numpy as np

# img = cv.imread('../how_performance_art_took_over_the_art_world_900x450_c.jpg')
# cv.imshow('Art', img)

# create a blank image to work with
blank = np.zeros((500, 500, 3), dtype='uint8') # shape 500px, 500px, number of colour channels (3) and datatype - uint8 = an image
# cv.imshow('Blank', blank)

# PAINT
# blank[:] = 0,255,0 #paint each of the pixels a colour - in B,G,R 0-255
# blank[200:300, 300:400] = 0,0,255 # paint a red square in pixels y:200-x:300 and y:300-x:400
# cv.imshow('Square', blank)

# RECTANGLE
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) 
# #img, part1, part2, color, thickness=None (or a number, or -1 for Filled), linetype=None, shift=None
# cv.imshow('Rectangle', blank)

# CIRCLE
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3) 
#image, midpoint of circle - in this case middle of picture = blank-y /2 , blank-x/2; radius 
# cv.imshow('Circle', blank)

# LINE
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# draw a line - image, point from, point to, colour
# cv.imshow('Line', blank)

# TEXT
cv.putText(blank, 'Hello', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
# img, text to put, origin, fontFace, fontscale, colour
cv.imshow('Text', blank)

cv.waitKey(0)