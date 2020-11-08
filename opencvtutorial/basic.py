import cv2 as cv

img = cv.imread('../how_performance_art_took_over_the_art_world_900x450_c.jpg')
# BGR - blue, green, red
cv.imshow('Art', img)

# CONVERT TO GREYSCALE
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
# convert a BGR image to 'grayscale'
# cv.imshow('Art', grey)

# BLUR - for reducing noise
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #kernel size as tuple = how much you want to blur
# cv.imshow('Blur', blur)

# EDGE CASCADE - try to find edges present in the image
canny = cv.Canny(img, 135, 175) #threshold values as tuple
canny2 = cv.Canny(blur, 135, 175) #pass in slightly blurred image to just find the main edges
# cv.imshow('Canny Edges', canny2)

# DILATE THE IMAGE
dilated = cv.dilate(canny, (7,7), iterations=3) #src, kernel, iterations
# cv.imshow('Dilated', dilated)

# ERODiNG
eroded = cv.erode(dilated, (3,3), iterations=1) # image, kernel sizes, iterations through
# cv.imshow('Eroded', eroded)

# RESIZE
resized = cv.resize(img, (200,200), interpolation=cv.INTER_AREA) #image to be resized, destination size - ignoring aspect ratio
# INTER_AREA - scaling down
# INTER_LINEAR - enlarging
# INTER_CUBIC - enlarging. slower, but higher quality
# cv.imshow('Resized', resized)

# CROP
cropped = img[100:200, 600:800]
# you're just getting a portion of the image -  image-y:image-y, image-x:image-x
cv.imshow('Cropped', cropped)

cv.waitKey(0) # quit the program by hitting any key
